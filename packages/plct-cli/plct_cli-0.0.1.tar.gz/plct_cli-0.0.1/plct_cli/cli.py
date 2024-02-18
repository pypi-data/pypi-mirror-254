
from typing import Union
import click
import shutil
import yaml
import os

from paver.easy import sh

DEFAULT_BUILDER = "html"
EXTENSIONS = (".rst", ".md", ".txt")

@click.group()
def main():
    """
    Petlja learning content tool command-line interface.

    For help on specific command, use: plct [COMMAND] --help
    """
    pass


@main.command()
@click.option("-so", "--sphinx-options", default=[], multiple=True, help="Sphinx options")
@click.option("-sf", "--sphinx-files", default=[],  multiple=True, help="Sphinx-build filenames")
def build(sphinx_options, sphinx_files) -> None:
    config_dict = _get_source_and_output_dirs_or_print_error()
    if config_dict is None:
        return
    source_dir = config_dict["source_dir"]
    output_dir = config_dict["output_dir"]
    builder = config_dict["builder"]
    options = " ".join(sphinx_options)
    files = " ".join(sphinx_files)
    sh(f'sphinx-build -M {builder} {options} "{source_dir}" "{output_dir}" {files}')


@main.command()
@click.option("-so", "--sphinx-options", default=[], multiple=True, help="Sphinx options")
def preview(sphinx_options) -> None:
    config_dict = _get_source_and_output_dirs_or_print_error()
    if config_dict is None:
        return
    source_dir = config_dict["source_dir"]
    output_dir = config_dict["output_dir"]
    builder = config_dict["builder"]

    options = " ".join(sphinx_options)
    options += f" -b {builder}"
    options += f" -d {output_dir}/doctrees"
    options += f" --open-browser"

    # mimicing sphinx-build -M option
    if builder != "plct_builder":
        output_dir = os.path.join(output_dir, builder)
    else:
        #hacking since sphinx autobuild does not support difrent arguments for build and serve
        output_dir = os.path.join(output_dir, builder, "static_website")
        

    sh(f'sphinx-autobuild "{source_dir}" "{output_dir}" {options} ')



@main.command()
def publish() -> None:
    config_dict = _get_source_and_output_dirs_or_print_error()
    if config_dict is None:
        return
    shutil.copytree(os.path.join(config_dict["output_dir"], config_dict["builder"]), "docs")


@main.command()
def clean() -> None:
    config_dict = _get_source_and_output_dirs_or_print_error()
    if config_dict is None:
        return
    shutil.rmtree(config_dict["output_dir"], ignore_errors=True)

@main.command()
def get_markdown() -> None:
    project_dir = os.getcwd()
    config_dict = _get_source_and_output_dirs_or_print_error()
    if config_dict is None:
        return
    build_dir_source_copy_path = os.path.join(config_dict["output_dir"], "_sources")
    source_dir = build_dir_source_copy_path if os.path.isdir(build_dir_source_copy_path) else config_dict["source_dir"]
    package_dir = os.path.join(project_dir, "markdown_files")
    if not os.path.isdir(package_dir):
        os.makedirs(package_dir)
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(EXTENSIONS):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(package_dir, file)
                shutil.copy2(src_file, dst_file)
    shutil.make_archive("package", "zip", package_dir)
    shutil.rmtree(package_dir, ignore_errors=True)


def _get_config_from_yaml() -> Union[dict[str, str], None]:
    if os.path.isfile("plct_config.yaml"):
        with open("plct_config.yaml") as f:
            config = yaml.safe_load(f)
        return config
    return None


def _get_config_from_sphinx_project() -> tuple[str, str, str]:
    project_dir = os.getcwd()
    source_dir = os.path.join(project_dir, "source")
    build_dir = os.path.join(project_dir, "build")
    if os.path.isdir(source_dir):
        _ensure_dir(build_dir)
        return source_dir, build_dir, DEFAULT_BUILDER
    else:
        source_dir = os.path.join(project_dir)
        build_dir = os.path.join(project_dir, "_build")
        if os.path.isfile(os.path.join(source_dir, "conf.py")):
            _ensure_dir(build_dir)
            return source_dir, build_dir, DEFAULT_BUILDER
        else:
            raise ValueError(
                "Unknown Sphinx project directory structure. Please specify source and build directories in plct_config.yaml")


def _get_source_and_output_dirs() -> dict[str, str]:
    config = _get_config_from_yaml()
    if config:
        source_dir = config.get("source_dir")
        output_dir = config.get("output_dir")
        builder = config.get("builder")
        if source_dir is None or output_dir is None or builder is None:
            raise ValueError("Invalid configuration file.")
    else:
        source_dir, output_dir, builder = _get_config_from_sphinx_project()
    return {'source_dir' : source_dir, 'output_dir' : output_dir, 'builder' : builder}


def _get_source_and_output_dirs_or_print_error() -> Union[dict[str, str], None]:
    try:
        config_dict = _get_source_and_output_dirs()
    except ValueError as error:
        print(error)
        return None
    return config_dict

def _ensure_dir(path: str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path)