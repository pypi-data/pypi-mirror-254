import json
import logging
import os
from pathlib import Path

from dbt.cli.main import dbtRunner

logger = logging.getLogger(__name__)

MANIFEST = "manifest.json"


def load_manifest(project_dir: str, target_dir: str, profiles_dir: str | None = None):
    """Load a dbt Manifest using dbt variables"""

    manifest_path = Path(project_dir) / target_dir / MANIFEST

    if not manifest_path.exists():
        compile_manifest(project_dir, target_dir, profiles_dir)

    with manifest_path.open(encoding="utf8") as manifest_stream:
        manifest_dict = json.load(manifest_stream)

    logger.info("Manifest loaded from %s", manifest_path)

    return manifest_dict


def compile_manifest(
    project_dir: str,
    target_path: str,
    profiles_dir: str | None = None,
) -> None:
    os.environ["DBT_PROJECT_DIR"] = project_dir
    os.environ["DBT_TARGET_PATH"] = target_path
    if profiles_dir:
        os.environ["DBT_PROFILES_DIR"] = profiles_dir

    try:
        dbtRunner().invoke(["compile", "--no-introspect", "--no-populate-cache"])
        logger.info("dbt manifest created in folder '%s'", target_path)
    except:
        logger.error("Error while compiling dbt manifest")
        raise
