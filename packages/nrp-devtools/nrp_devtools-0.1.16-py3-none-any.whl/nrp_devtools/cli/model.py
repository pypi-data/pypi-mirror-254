import tempfile
from pathlib import Path

import click

from ..commands.model.compile import (
    add_model_to_i18n,
    add_requirements_and_entrypoints,
    compile_model_to_tempdir,
    copy_compiled_model,
    install_model_compiler,
)
from ..commands.model.create import create_model
from ..commands.pdm import install_python_repository
from ..commands.utils import make_step
from ..config import OARepoConfig, ask_for_configuration
from ..config.model_config import ModelConfig
from .base import command_sequence, nrp_command


@nrp_command.group(name="model")
def model_group():
    """
    Model management commands
    """


@model_group.command(name="create", help="Create a new model")
@click.argument("model_name")
@command_sequence(save=True)
def create_model_command(*, config: OARepoConfig, model_name, **kwargs):
    for model in config.models:
        if model.model_name == model_name:
            click.secho(f"Model {model_name} already exists", fg="red", err=True)
            return

    def set_model_configuration(config: OARepoConfig, *args, **kwargs):
        config.add_model(
            ask_for_configuration(
                config, ModelConfig, initial_values={"model_name": model_name}
            )
        )

    return (
        set_model_configuration,
        make_step(create_model, model_name=model_name),
    )


@model_group.command(name="compile", help="Compile a model")
@click.argument("model_name")
@command_sequence()
def compile_model_command(*, config: OARepoConfig, model_name, **kwargs):
    model = config.get_model(model_name)
    # create a temporary directory using tempfile
    tempdir = str(Path(tempfile.mkdtemp()).resolve())

    return (
        make_step(install_model_compiler, model=model),
        make_step(compile_model_to_tempdir, model=model, tempdir=tempdir),
        make_step(copy_compiled_model, model=model, tempdir=tempdir),
        make_step(add_requirements_and_entrypoints, model=model, tempdir=tempdir),
        make_step(install_python_repository),
        make_step(add_model_to_i18n, model=model),
    )
