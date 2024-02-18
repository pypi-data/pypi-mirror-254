import typing as t
from dataclasses import dataclass

from tmdl.models import TmdlColumn, TmdlTable
from tmdl.models.column import DataType
from tmdl.models.model import Model as TmdlModel

from .models import DbtManifest, DbtModel


@dataclass
class TmdlFile:
    filename: str
    content: str


@dataclass
class TmdlProject:
    model: TmdlFile
    tables: t.List[TmdlFile]
    relationships: t.Optional[TmdlFile] = None


def tmdl_table_from_dbt_model(model: DbtModel) -> TmdlFile:

    filename = f"{model.name}.tmdl"

    columns = [
        TmdlColumn(
            name=name,
            source_column=column.name,
            description=column.description,
            data_type=(
                DataType(column.data_type) if column.data_type else DataType.STRING
            ),
        )
        for name, column in model.columns.items()
    ]

    table = TmdlTable(name=model.name, columns=columns)

    return TmdlFile(filename=filename, content=table.dump())


def tmdl_model_from_dbt_manifest(manifest: DbtManifest) -> TmdlFile:

    filename = "model.tmdl"

    model = TmdlModel(name=manifest.name)

    return TmdlFile(filename=filename, content=model.dump())


def tmdl_project_from_dbt_manifest(manifest: DbtManifest) -> TmdlProject:

    return TmdlProject(
        model=tmdl_model_from_dbt_manifest(manifest),
        tables=[tmdl_table_from_dbt_model(model) for model in manifest.models],
        relationships=None,
    )
