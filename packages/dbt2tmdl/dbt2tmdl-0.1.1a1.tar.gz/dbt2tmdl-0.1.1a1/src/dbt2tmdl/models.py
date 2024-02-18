import typing as t
from enum import Enum

from pydantic import BaseModel, Field
from tmdl.models import TmdlColumn, TmdlModel, TmdlTable
from tmdl.models.column import DataType


class Materialization(str, Enum):
    TABLE = "table"
    VIEW = "view"


class ResourceType(str, Enum):
    MODEL = "model"
    TEST = "test"


class DbtManifestMetadata(BaseModel):
    adapter_type: str
    project_name: str


class DbtModelColumn(BaseModel):
    name: str
    description: str = ""
    data_type: t.Optional[str] = "String"

    def to_tmdl(self) -> TmdlColumn:
        return TmdlColumn(
            name=self.name.capitalize(),
            source_column=self.name,
            description=self.description,
            data_type=DataType(self.data_type),
        )


class DbtModelConfig(BaseModel):
    enabled: bool = True
    materialized: Materialization = Materialization.VIEW


class DbtTest(BaseModel):
    resource_type: t.Literal[ResourceType.TEST]


class DbtModel(BaseModel):
    resource_type: t.Literal[ResourceType.MODEL] = Field(init_var=True, repr=False)
    name: str
    alias: str
    project_id: str = Field(..., alias="database")
    dataset: str = Field(..., alias="schema")
    description: t.Optional[str] = ""
    columns: t.Dict[str, DbtModelColumn]
    sql: str = Field(..., alias="compiled_code", repr=False)

    @property
    def table_id(self) -> str:
        return f"{self.project_id}.{self.dataset}.{self.name}"

    def to_tmdl(self) -> TmdlTable:
        return TmdlTable(
            name=self.name,
            columns=[column.to_tmdl() for column in self.columns.values()],
        )


class DbtManifest(BaseModel):
    metadata: DbtManifestMetadata
    nodes: t.Dict[
        str,
        t.Annotated[t.Union[DbtModel, DbtTest], Field(discriminator="resource_type")],
    ]

    @property
    def name(self) -> str:
        return self.metadata.project_name

    @property
    def models(self) -> t.List[DbtModel]:
        return [node for node in self.nodes.values() if isinstance(node, DbtModel)]

    def __getitem__(self, key: str) -> DbtModel | DbtTest:
        return self.nodes[key]

    def __contains__(self, key: str) -> bool:
        return key in self.nodes

    def to_tmdl(self):
        return TmdlModel(
            name=self.name,
            tables=[model.to_tmdl() for model in self.models],
        )
