from functools import partial

import click

from ..commands.invenio import install_invenio_cfg
from ..commands.pdm import (
    build_requirements,
    check_requirements,
    clean_previous_installation,
    create_empty_venv,
    install_python_repository,
)
from ..commands.ui import build_production_ui, collect_assets, install_npm_packages
from ..commands.utils import make_step, no_args, run_fixup
from ..config import OARepoConfig
from .base import command_sequence, nrp_command


@nrp_command.command(name="build")
@command_sequence()
def build_command(*, config: OARepoConfig, **kwargs):
    """Builds the repository"""
    return build_command_internal(config=config, **kwargs)


def build_command_internal(*, config: OARepoConfig, **kwargs):
    return (
        no_args(
            partial(click.secho, "Building repository for production", fg="yellow")
        ),
        make_step(clean_previous_installation),
        make_step(create_empty_venv),
        run_fixup(check_requirements, build_requirements, fix=True),
        install_python_repository,
        install_invenio_cfg,
        collect_assets,
        install_npm_packages,
        build_production_ui,
        no_args(partial(click.secho, "Successfully built the repository", fg="green")),
    )
