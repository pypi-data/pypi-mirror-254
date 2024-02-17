import os
import re
import shutil
import sys

import click
import requirements
import tomli
import tomli_w

from nrp_devtools.commands.check import check_failed
from nrp_devtools.commands.utils import install_python_modules, run_cmdline
from nrp_devtools.config import OARepoConfig


def clean_previous_installation(config: OARepoConfig, **kwargs):
    destroy_venv(config)


def create_empty_venv(config):
    install_python_modules(config, config.pdm_dir, "setuptools", "pip", "wheel", "pdm")
    install_python_modules(
        config,
        config.venv_dir,
        "setuptools",
        "pip",
        "wheel",
    )


def destroy_venv(config):
    if config.pdm_dir.exists():
        shutil.rmtree(config.pdm_dir)
    if config.venv_dir.exists():
        shutil.rmtree(config.venv_dir)


def build_requirements(config, **kwargs):
    destroy_venv(config)
    create_empty_venv(config)
    create_pdm_file(config, ".nrp/oarepo-pdm")
    lock_python_repository(config, ".nrp/oarepo-pdm")
    oarepo_requirements = export_pdm_requirements(config, ".nrp/oarepo-pdm")

    lock_python_repository(config)
    all_requirements = export_pdm_requirements(config)

    oarepo_requirements = list(requirements.parse(oarepo_requirements))
    all_requirements = list(requirements.parse(all_requirements))

    # get the current version of oarepo
    oarepo_requirement = [x for x in oarepo_requirements if x.name == "oarepo"][0]

    # now make the difference of those two (we do not want to have oarepo dependencies in the result)
    # as oarepo will be installed to virtualenv separately (to handle system packages)
    oarepo_requirements_names = {x.name for x in oarepo_requirements}
    non_oarepo_requirements = [
        x for x in all_requirements if x.name not in oarepo_requirements_names
    ]

    # remove local packages
    non_oarepo_requirements = [
        x for x in non_oarepo_requirements if "file://" not in x.line
    ]

    # and generate final requirements
    resolved_requirements = "\n".join(
        [oarepo_requirement.line, *[x.line for x in non_oarepo_requirements]]
    )
    (config.repository_dir / "requirements.txt").write_text(resolved_requirements)


def lock_python_repository(config, subdir=None):
    write_pdm_python(config)
    run_pdm(config, "lock", subdir=subdir)


def check_invenio_callable(config, will_fix=False, **kwargs):
    try:
        run_cmdline(
            config.venv_dir / "bin" / "invenio",
            "oarepo",
            "version",
            raise_exception=True,
            grab_stdout=True,
        )
    except:
        check_failed(
            f"Virtualenv directory {config.venv_dir} does not contain a callable invenio installation",
            will_fix=will_fix,
        )


def install_python_repository(config, **kwargs):
    write_pdm_python(config)
    run_pdm(config, "install", "--dev", "--no-lock")

    # fixup for uritemplate / uritemplate.py
    run_cmdline(
        config.venv_dir / "bin" / "pip",
        "install",
        "-U",
        "--force-reinstall",
        "--upgrade-strategy",
        "eager",
        "uritemplate",
    )


def create_pdm_file(config: OARepoConfig, output_directory: str):
    original_pdm_file = tomli.loads(
        (config.repository_dir / "pyproject.toml").read_text()
    )
    dependencies = original_pdm_file["project"]["dependencies"]
    oarepo_dependency = [
        x
        for x in dependencies
        if re.match(
            r"^\s*oarepo\s*(\[[^\]]+\])?\s*==.*", x
        )  # take only oarepo package, discard others
    ][0]

    original_pdm_file["project"]["dependencies"] = [oarepo_dependency]

    output_path = config.repository_dir / output_directory
    output_path.mkdir(parents=True, exist_ok=True)

    (output_path / "pyproject.toml").write_text(tomli_w.dumps(original_pdm_file))


def remove_virtualenv_from_env():
    current_env = dict(os.environ)
    virtual_env_dir = current_env.pop("VIRTUAL_ENV", None)
    if not virtual_env_dir:
        return current_env
    current_env.pop("PYTHONHOME", None)
    current_env.pop("PYTHON", None)
    path = current_env.pop("PATH", None)
    split_path = path.split(os.pathsep)
    split_path = [x for x in split_path if not x.startswith(virtual_env_dir)]
    current_env["PATH"] = os.pathsep.join(split_path)
    return current_env


def run_pdm(config, *args, subdir=None, **kwargs):
    write_pdm_python(config)

    cwd = config.repository_dir
    if subdir:
        cwd = cwd / subdir

    if (cwd / "__pypackages__").exists():
        shutil.rmtree(cwd / "__pypackages__")

    environ = {
        "PDM_IGNORE_ACTIVE_VENV": "1",
        "PDM_IGNORE_SAVED_PYTHON": "1",
        **remove_virtualenv_from_env(),
    }
    venv_path = config.venv_dir
    if venv_path.exists():
        environ.pop("PDM_IGNORE_ACTIVE_VENV", None)
        environ["VIRTUAL_ENV"] = str(venv_path)
        print(f"Using venv for pdm: {environ['VIRTUAL_ENV']}")

    return run_cmdline(
        config.pdm_dir / "bin" / "pdm",
        *args,
        cwd=cwd,
        environ=environ,
        no_environment=True,
        raise_exception=True,
        **kwargs,
    )


def export_pdm_requirements(config, subdir=None):
    return run_pdm(
        config,
        "export",
        "-f",
        "requirements",
        "--without-hashes",
        grab_stdout=True,
        subdir=subdir,
    )


def install_local_packages(config, local_packages=None):
    if not local_packages:
        return
    for lp in local_packages:
        run_cmdline(
            config.venv_dir / "bin" / "pip",
            "install",
            "--config-settings",
            "editable_mode=compat",
            "-e",
            lp,
            cwd=config.repository_dir,
        )


def check_virtualenv(config: OARepoConfig, will_fix=False, **kwargs):
    if not config.venv_dir.exists():
        click.secho(
            f"Virtualenv directory {config.venv_dir} does not exist", fg="red", err=True
        )
        sys.exit(1)

    try:
        run_cmdline(
            config.venv_dir / "bin" / "python",
            "--version",
            raise_exception=True,
        )
    except:  # noqa
        check_failed(
            f"Virtualenv directory {config.venv_dir} does not contain a python installation",
            will_fix=will_fix,
        )

    try:
        run_cmdline(
            config.venv_dir / "bin" / "pip",
            "list",
            raise_exception=True,
            grab_stdout=True,
        )
    except:  # noqa
        check_failed(
            f"Virtualenv directory {config.venv_dir} does not contain a pip installation",
            will_fix=will_fix,
        )


def fix_virtualenv(config: OARepoConfig, **kwargs):
    destroy_venv(config)
    create_empty_venv(config)


def check_requirements(config: OARepoConfig, will_fix=False, **kwargs):
    reqs_file = config.repository_dir / "requirements.txt"
    if not reqs_file.exists():
        check_failed(f"Requirements file {reqs_file} does not exist")

    # if any pyproject.toml is newer than requirements.txt, we need to rebuild
    pyproject = config.repository_dir / "pyproject.toml"

    if pyproject.exists() and pyproject.stat().st_mtime > reqs_file.stat().st_mtime:
        check_failed(
            f"Requirements file {reqs_file} is out of date, {pyproject} has been modified",
            will_fix=will_fix,
        )


def write_pdm_python(config: OARepoConfig):
    pdm_python_file = config.repository_dir / ".pdm-python"
    if pdm_python_file.exists():
        previous_content = pdm_python_file.read_text().strip()
    else:
        previous_content = None
    new_content = str(config.venv_dir / "bin" / "python")
    if new_content != previous_content:
        pdm_python_file.write_text(new_content)
