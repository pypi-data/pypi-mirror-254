from typing import Tuple, Optional, List
from abc import ABC, abstractmethod
from profiles_rudderstack.recipe import PyNativeRecipe
from profiles_rudderstack.contract import Contract, build_contract

class MaterializationSpec:
    def __init__(self, output_type: str = "", run_type: str = "", requested_enable_status: str = ""):
        self.output_type = output_type
        self.run_type = run_type
        self.requested_enable_status = requested_enable_status

class EntityId:
	def __init__(self, select: str, type: str, entity: str, to_default_stitcher: bool = False):
		self.select = select
		self.type = type
		self.entity = entity
		self.to_default_stitcher = to_default_stitcher   

class BaseModelType(ABC):
    TypeName = "base_model_type"
    # Json Schema
    BuildSpecSchema = {}

    contract: Optional[Contract] = None
    entity_key: Optional[str] = None
    materialization: Optional[MaterializationSpec] = None
    ids: Optional[List[EntityId]] = None

    def __init__(self, build_spec: dict, schema_version: int, pb_version: str) -> None:
        self.build_spec = build_spec
        self.schema_version = schema_version
        self.pb_version = pb_version

        if build_spec.get("entity_key", None) is not None:
            self.entity_key = build_spec["entity_key"]

        if build_spec.get("contract", None) is not None:
            self.contract = build_contract(build_spec["contract"])

        mzn = build_spec.get("materialization", None)
        if mzn is not None:
            self.materialization = MaterializationSpec(mzn.get("output_type", ""), mzn.get("run_type", ""), mzn.get("enable_status", ""))

        if build_spec.get("ids", None) is not None:
            self.ids = []
            for id in build_spec["ids"]:
                self.ids.append(EntityId(id["select"], id["type"], id["entity"], id.get("to_default_stitcher", False)))
    
    @abstractmethod
    def get_material_recipe(self) -> PyNativeRecipe:
        """Define the material recipe of the model

        Returns:
            Recipe: Material recipe of the model
        """
        raise NotImplementedError()
    
    @abstractmethod
    def validate(self) -> Tuple[bool, str]:
        """Validate the model

        Returns:
            Tuple[bool, str]: Validation result and error message
        """
        if self.schema_version < 43:
            return False, "schema version should >= 43"
        return True, ""
