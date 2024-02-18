import signal, grpc, time, math
from concurrent import futures
from profiles_rudderstack.wht_service import init_wht_service, ClientTokenAuthInterceptor
from profiles_rudderstack.utils import RefManager
from profiles_rudderstack.service import ProfilesRpcService
from profiles_rudderstack.logger import Logger
from profiles_rudderstack.tunnel.tunnel_pb2 import PingRequest, PingResponse, SetPythonPortRequest
from profiles_rudderstack.tunnel.tunnel_pb2_grpc import PythonServiceStub, add_PythonServiceServicer_to_server, WhtServiceStub

class ProfilesRPCServer:
    def __init__(self, token: str, go_rpc_addr: str, current_supported_schema_version: int, pb_version: str):
        self.go_rpc_addr = go_rpc_addr
        self.__server_init(token, current_supported_schema_version, pb_version)
    
    def __is_wht_rpc_up(self, token: str):
        max_retries = 10
        base_delay = 0.1 # seconds
        interceptors = [ClientTokenAuthInterceptor(token)]
        for i in range(max_retries):
            sec_retry = math.pow(2, i)
            delay = base_delay + sec_retry
            try:
                with grpc.insecure_channel(self.go_rpc_addr) as channel:
                    intercept_channel = grpc.intercept_channel(channel, *interceptors)
                    stub = WhtServiceStub(intercept_channel)
                    response: PingResponse = stub.Ping(PingRequest())
                    if response.message == "ready":
                        return True
            except Exception as e:
                print(f"Error: connecting to WHT RPC server: {e}. Retrying in {delay} seconds")
            time.sleep(delay)

        return False
        
    def __server_init(self, token: str, current_supported_schema_version: int, pb_version: str):
        refManager = RefManager()
        if not self.__is_wht_rpc_up(token):
            raise Exception("WHT RPC server is not up")
        
        wht_service, channel = init_wht_service(self.go_rpc_addr, token)
        self.channel = channel
        service = ProfilesRpcService(
            ref_manager=refManager,
            wht_service=wht_service,
            current_supported_schema_version=current_supported_schema_version,
            pb_version=pb_version,
        )

        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=[ServerTokenAuthInterceptor(token)])
        add_PythonServiceServicer_to_server(service, server)
        # [::]:0 will bind to a free port
        python_rpc_port = server.add_insecure_port("[::]:0")
        server.start()
        
        wht_service.SetPythonPort(SetPythonPortRequest(port=python_rpc_port, token=token))

        self.logger = Logger("ProfilesRPCServer")
        self.logger.info("Initialized Python RPC Server")
        self.server = server

        def signal_handler(sig, frame):
            self.stop()
            exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        server.wait_for_termination()

    def stop(self):
        # self.logger.info("Stopping Python RPC Server")
        self.channel.close()
        self.server.stop(0)


class ServerTokenAuthInterceptor(grpc.ServerInterceptor):
    def __init__(self, token: str):
        self.token = token

    def intercept_service(self, continuation, handler_call_details):
        metadata = dict(handler_call_details.invocation_metadata)
        token = metadata.get('authorization', '')

        if token != self.token:
            context = handler_call_details.invocation_context
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid credentials")
        else:
            return continuation(handler_call_details)
