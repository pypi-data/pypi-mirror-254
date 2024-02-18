import click
from pathlib import Path
from snakecdysis.global_variable import pkg_templates_path
import shutil


@click.command("generate_template")
@click.option("--path", "-p", default=".", type=click.Path(exists=False, file_okay=False, dir_okay=True, readable=True, resolve_path=True, path_type=Path),
              required=True, show_default=True, help='Path to create template python wrapped package (')
@click.option("--name", '-n', type=str, required=True, help='The wrapper workflow name')
def main(path, name):
    """Generate the template of repository to create python package"""
    install_path = Path(path)
    click.secho(f"\n    Create path '{path}'", fg="yellow")
    try:
        install_path.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        files_list = list(install_path.glob("*"))
        if len(files_list) > 0:
            raise FileExistsError(f"Error: directory {install_path} already existed and is not empty!!")

    click.secho(f"\n    Copy templates files from {pkg_templates_path} to {install_path}", fg="yellow")
    pkg_name_dest = install_path.joinpath(name)
    if pkg_name_dest.exists():
        shutil.rmtree(pkg_name_dest)
    shutil.copytree(pkg_templates_path, install_path, dirs_exist_ok=True, copy_function=shutil.copy2)
    install_path.joinpath("PKGNAME").rename(pkg_name_dest)

    for file in install_path.glob("**/*"):
        if file.is_file() and "__pycache__" not in file.parent.as_posix():
            print(file)
            file.write_text(file.read_text().replace("PKGNAME",name))





if __name__ == "__main__":
    main()
