import shutil
from pathlib import Path

import click
from tqdm import tqdm

from nrp_devtools.config import OARepoConfig

from .assets import load_watched_paths


def copy_assets_to_webpack_build_dir(config: OARepoConfig):
    # assets = (config.site_dir / "assets").resolve()
    static = (config.ui_dir / "static").resolve()

    watched_paths = load_watched_paths(
        config.invenio_instance_path / "watch.list.json",
        [f"{static}=static"],
    )
    kinds = {"assets", "static"}

    existing = {k: set() for k in kinds}
    for kind, target in tqdm(
        _list_files(kinds, config.invenio_instance_path),
        desc="Enumerating existing paths",
    ):
        relative_path = target.relative_to(config.invenio_instance_path / kind)
        if relative_path.parts[0] in ("node_modules", "patches", "build", "dist"):
            continue
        if len(relative_path.parts) == 1:
            continue
        existing[kind].add(target)

    copied = {k: {} for k in kinds}

    for kind, source_path, source_file in tqdm(
        _list_source_files(watched_paths), desc="Checking paths"
    ):
        target_file = (
            config.invenio_instance_path / kind / source_file.relative_to(source_path)
        )
        copied[kind][source_file] = target_file
        if target_file in existing[kind]:
            existing[kind].remove(target_file)

    for kind, existing_data in existing.items():
        to_remove = [target for target in existing_data if target.exists()]
        if to_remove:
            click.secho(
                f"Error: following {kind} are not in the source directories, "
                "will remove those from .venv assets",
                fg="red",
            )
            for target in to_remove:
                if target.exists():
                    click.secho(f"  {target}", fg="red")
                    if target.is_dir():
                        shutil.rmtree(target)
                    else:
                        target.unlink()

    for kind, source_file, target_file in tqdm(
        _list_copied_files(copied), desc="Linking assets and statics"
    ):
        target_file.parent.mkdir(parents=True, exist_ok=True)
        try:
            target_file.unlink()
        except FileNotFoundError:
            pass
        # copy source file to target file
        shutil.copy(source_file, target_file)


def _list_files(kinds, base_path):
    for kind in kinds:
        for file_or_dir in Path(base_path / kind).glob("**/*"):
            if file_or_dir.is_dir():
                continue
            yield kind, file_or_dir


def _list_source_files(watched_paths):
    for source_path, kind in watched_paths.items():
        for source_file in Path(source_path).glob("**/*"):
            if source_file.is_dir():
                continue
            yield kind, source_path, source_file


def _list_copied_files(linked):
    for kind, linked_data in linked.items():
        for source_file, target_file in linked_data.items():
            yield kind, source_file, target_file
