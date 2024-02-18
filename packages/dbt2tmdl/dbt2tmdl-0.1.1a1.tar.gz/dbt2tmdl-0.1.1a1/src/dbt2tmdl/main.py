import argparse
import logging
from pathlib import Path

from .generator import tmdl_project_from_dbt_manifest
from .loader import load_manifest
from .models import DbtManifest as Manifest

DEFAULT_OUTPUT_DIR = "./tmdl"
DEFAULT_TARGET_DIR = "target/"

logger = logging.getLogger(__name__)


def main(project_dir: str, target_dir: str, output_dir: str):

    manifest = Manifest(**load_manifest(project_dir, target_dir))

    tmdl_project = tmdl_project_from_dbt_manifest(manifest)

    (Path(output_dir) / "tables").mkdir(exist_ok=True, parents=True)

    # Export Tables
    for table in tmdl_project.tables:
        table_filepath: Path = Path(output_dir) / "tables" / table.filename
        with table_filepath.open("w") as table_io:
            table_io.write(table.content)
        logger.info(
            "TMDL created for table '%s' at %s",
            table_filepath.stem,
            table_filepath,
        )

    # Export relationships

    # Export Model and Database from dbt_project.yaml
    model_filepath = Path(output_dir) / tmdl_project.model.filename
    with model_filepath.open("w") as model_io:
        model_io.write(tmdl_project.model.content)
    logger.info("TMDL created for model at %s", model_filepath)


def cli():

    cwd = Path().cwd()
    parser = argparse.ArgumentParser(
        "dbt2tmdl", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--dbt-project-dir", default=str(cwd), help="dbt project directory"
    )
    parser.add_argument(
        "--dbt-target-dir",
        default=DEFAULT_TARGET_DIR,
        help="target directory name in dbt project directory",
    )
    parser.add_argument(
        "dir",
        nargs="?",
        default=Path().cwd() / DEFAULT_OUTPUT_DIR,
        help="Directory where to export TMDL files",
    )
    args = parser.parse_args()

    Path(args.dir).mkdir(parents=True, exist_ok=True)

    main(
        project_dir=args.dbt_project_dir,
        target_dir=args.dbt_target_dir,
        output_dir=args.dir,
    )


if __name__ == "__main__":
    cli()
