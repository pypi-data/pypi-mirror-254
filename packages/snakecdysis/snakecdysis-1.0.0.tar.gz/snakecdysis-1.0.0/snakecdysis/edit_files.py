import click
from shutil import copyfile
from pathlib import Path


def __edit_tools(snake_installer, restore):
    if restore:
        if snake_installer.user_tools_path.exists():
            snake_installer.user_tools_path.unlink()
            click.secho(f"""\n    Success reset your own tools_path.yaml on path '{snake_installer.user_tools_path}'
                                  with default tools_path.yaml '{snake_installer.git_tools_path}""", fg="yellow")
    if not snake_installer.user_tools_path.exists():
        snake_installer.write_user_tools_path()
    click.edit(require_save=True, extension='.yaml', filename=snake_installer.user_tools_path)
    click.secho(f"    Success install your own tools_path.yaml on path '{snake_installer.user_tools_path}'", fg="yellow")
    click.secho(f"    {snake_installer.soft_name} used '{snake_installer.user_tools_path}' at default now !!\n\n", fg="bright_red")


def __show_tools(snake_installer):
    click.secho(f"""\
    - Tools version was read using file: \t{snake_installer.get_active_tools_path}
    - Install mode is:   \t{snake_installer.install_mode}
    - Tools install mode is: \t{snake_installer.tools_mode}
    , please wait""", fg="yellow")
    df = snake_installer.tools_version_to_df(csv_file=snake_installer.tools_version_path, active_tools_list=[], output_file=None)
    click.secho(f"    Tools version are:\n{df.to_string(index=False)}", fg="yellow")


def __create_config(snake_installer, configyaml):
    configyaml = Path(configyaml)
    configyaml.parent.mkdir(parents=True, exist_ok=True)
    copyfile(snake_installer.git_config_path.as_posix(), configyaml.as_posix())
    click.edit(require_save=True, extension='.yaml', filename=configyaml.as_posix())
    click.secho(f"    Success create config file on path '{configyaml}'\n    add to command:", fg="yellow")
    mode = snake_installer.install_mode
    click.secho(f"    {snake_installer.soft_name} {'run_cluster' if mode == 'cluster' else 'run_local'} --config {configyaml}\n\n", fg="bright_blue")


def __edit_cluster_config(snake_installer):
    f"""Edit file on {snake_installer.user_cluster_config}"""
    snake_installer.user_cluster_config.parent.mkdir(parents=True, exist_ok=True)
    if not snake_installer.user_cluster_config.exists():
        copyfile(snake_installer.git_cluster_config.as_posix(), snake_installer.user_cluster_config.as_posix())
    click.edit(require_save=True, extension='.yaml', filename=snake_installer.user_cluster_config.as_posix())
    click.secho(f"    See '{snake_installer.docs}' to adapt on your cluster\n", fg="yellow")
    click.secho(f"    Success edit cluster_config file on path '{snake_installer.user_cluster_config}'\n\n", fg="yellow")
