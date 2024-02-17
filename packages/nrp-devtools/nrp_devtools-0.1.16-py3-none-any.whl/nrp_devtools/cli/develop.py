import click

from ..commands.develop import Runner
from ..commands.develop.controller import run_develop_controller
from ..commands.ui.link_assets import copy_assets_to_webpack_build_dir
from ..commands.utils import make_step
from ..config import OARepoConfig
from .base import command_sequence, nrp_command
from .check import check_commands


@nrp_command.command(name="develop")
@click.option(
    "--extra-library",
    "-e",
    "local_packages",
    multiple=True,
    help="Path to a local package to install",
)
@click.option(
    "--checks/--skip-checks",
    default=True,
    help="Check the environment before starting (default is to check, disable to get a faster startup)",
)
@command_sequence()
def develop_command(
    *, config: OARepoConfig, local_packages=None, checks=True, **kwargs
):
    """Starts the development environment for the repository."""
    runner = Runner(config)
    context = {}
    return (
        *(check_commands(context, local_packages, fix=True) if checks else ()),
        copy_assets_to_webpack_build_dir,
        make_step(
            lambda config=None, runner=None: runner.start_python_server(
                development_mode=True
            ),
            runner=runner,
        ),
        make_step(
            lambda config=None, runner=None: runner.start_webpack_server(),
            runner=runner,
        ),
        make_step(
            lambda config=None, runner=None: runner.start_file_watcher(), runner=runner
        ),
        make_step(run_develop_controller, runner=runner, development_mode=True),
    )
