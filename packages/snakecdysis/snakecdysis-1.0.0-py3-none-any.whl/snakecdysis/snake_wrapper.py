import pandas as pd
import yaml
import pprint
import os
import re
import subprocess
import click
from pathlib import Path
from shutil import rmtree
from collections import OrderedDict
from click import progressbar, secho
from snakemake.io import load_configfile
from .useful_function import multiprocessing_download


class SnakeInstaller:
    """
    This class is used to install Snakemake workflows.

    Args:
        soft_path (str): The path of the wrapped workflow installation.
        url (str): URL of versioning repository (GitHub or GitLab).
        docs (str): URL of documentation.
        description_tool (str): The header printed on the terminal when running the program.
            Please include string values 'VERSION', 'GIT_URL', and 'DOCS', and the wrapper automatically replaces them with the correct values.
        singularity_url_files (list(tuple())): List of tuples with downloaded URL and install destination with INSTALL_PATH, like INSTALL_PATH/containers/Singularity.CulebrONT_tools.sif.
        datatest_url_files (tuple): Tuple with 2 values, first the URL of datatest, second download name.
        snakefile (str): Path to the main Snakemake script file (default: snakefiles/snakefile).
        snakemake_scripts (str): Path to the main Snakemake script file (default: snakefiles/snakefile).
        default_profile (str): Path to create the cluster 'default_profile' directory (default: default_profile/).
        git_config_path (str): Path to the default config file YAML (default: install_files/config.yaml).
        git_tools_path (str): Path to the default tools config YAML (default: install_files/tools_path.yaml).
        git_cluster_config (str): Path to the SLURM cluster config file (default: install_files/cluster_config_SLURM.yaml).
        tools_version_path (str): Path to the csv with soft and command to get version (default: report_template/versions.csv).
    """

    def __init__(self, soft_path=None, url=None, docs=None, description_tool=None, singularity_url_files=None,
                 datatest_url_files=None, **kargs):
        """
        Initialize SnakeInstaller.

        Args:
        - soft_path (str): The path of the wrapped workflow installation.
        - url (str): URL of versioning repository (GitHub or GitLab).
        - docs (str): URL of documentation.
        - description_tool (str): The header printed on the terminal when running the program.
            Please include string values 'VERSION', 'GIT_URL', and 'DOCS', and the wrapper automatically replaces them with the correct values.
        - singularity_url_files (list(tuple())): List of tuples with downloaded URL and install destination with INSTALL_PATH, like INSTALL_PATH/containers/Singularity.CulebrONT_tools.sif.
        - datatest_url_files (tuple): Tuple with 2 values, first the URL of datatest, second download name.
        - snakefile (str): Path to the main Snakemake script file (default: snakefiles/snakefile).
        - snakemake_scripts (str): Path to the main Snakemake script file (default: snakefiles/snakefile).
        - default_profile (str): Path to create the cluster 'default_profile' directory (default: default_profile/).
        - git_config_path (str): Path to the default config file YAML (default: install_files/config.yaml).
        - git_tools_path (str): Path to the default tools config YAML (default: install_files/tools_path.yaml).
        - git_cluster_config (str): Path to the SLURM cluster config file (default: install_files/cluster_config_SLURM.yaml).
        - tools_version_path (str): Path to the csv with soft and command to get version (default: snakemake_scripts/report_template/versions.csv).
        - kargs: Additional keyword arguments.
        """

        self.tools_config = None
        self.install_path = soft_path
        self._current_file = self.user_tools_path.parent.joinpath('.current.txt')
        self.git_url = url
        self.docs = docs
        self.description_tool = description_tool
        self.singularity_url_files = singularity_url_files
        self.datatest_url_files = datatest_url_files
        self.dico_args = kargs
        self._latest_version = None
        self._lasted_file = None

        # autobuild attributs
        self.install_mode_file = self.install_path.joinpath(".mode.txt")

        # Snakemake settings
        self.snakefile = self.install_path.joinpath("snakefiles", "snakefile") if "snakefile" not in self.dico_args else \
            self.dico_args["snakefile"]
        self.snakemake_scripts = self.install_path.joinpath("scripts",
                                                            "snakemake_only") if "snakemake_scripts" not in self.dico_args else \
            self.dico_args["snakemake_scripts"]
        self.default_profile = self.install_path.joinpath(
            "default_profile") if "default_profile" not in self.dico_args else self.dico_args["default_profile"]
        self.git_config_path = self.install_path.joinpath("install_files",
                                                          "config.yaml") if "git_config_path" not in self.dico_args else \
            self.dico_args["git_config_path"]

        # Tools settings
        self.git_tools_path = self.install_path.joinpath("install_files",
                                                         "tools_path.yaml") if "git_tools_path" not in self.dico_args else \
            self.dico_args["git_tools_path"]

        self.tools_version_path = self.snakemake_scripts.joinpath("report_template",
                                                                  "versions.csv") if "tools_version_path" not in self.dico_args else \
            self.dico_args["tools_version_path"]

        # cluster settings
        self.git_cluster_config = self.install_path.joinpath("install_files",
                                                             "cluster_config_SLURM.yaml") if "git_cluster_config" not in self.dico_args else \
            self.dico_args["git_cluster_config"]
        self._lasted_file = self.user_tools_path.parent.joinpath('.latest.txt')


    @property
    def soft_name(self) -> str:
        """The wrapped workflow name."""
        return self._install_path.stem

    @property
    def install_path(self) -> Path:
        """The path of wrapped workflow installation."""
        return Path(self._install_path)

    @install_path.setter
    def install_path(self, path: Path = None):
        """
        Set the installation path.

        Args:
        - path (Path): The installation path.
        """

        if not path:
            raise ValueError("ERROR 'soft_path' is empty but mandatory.")
        elif not Path(path).exists():
            raise NotADirectoryError(f"ERROR 'soft_path', the path '{path}' doesn't exist")
        elif not Path(path).is_absolute():
            raise ValueError(f"ERROR 'soft_path', the path '{path}' is not on absolute path")
        else:
            self._install_path = Path(path)

    @property
    def git_url(self) -> str:
        """Url of versioning repository (GitHub or GitLab)"""
        return self._git_url

    @git_url.setter
    def git_url(self, url) -> str:
        if not url or not isinstance(url, str):
            raise ValueError("ERROR 'url' is empty or not a string value.")
        self._git_url = url

    @property
    def docs(self) -> str:
        """Url of documentation"""
        return self._docs

    @docs.setter
    def docs(self, docs) -> str:
        if not docs or not isinstance(docs, str):
            raise ValueError("ERROR 'docs' is empty or not a string value.")
        self._docs = docs

    @property
    def description_tool(self) -> str:
        """The header print on terminal when run programme

        Please add string values 'VERSION', 'GIT_URL' and 'DOCS' and wrapper automatically replace by the good values
        """
        return self._description_tool

    @description_tool.setter
    def description_tool(self, description_tool) -> str:
        if not description_tool or not isinstance(description_tool, str):
            raise ValueError("ERROR key 'description_tool' is empty or not a string value on 'dico_tool'.")
        self._description_tool = description_tool.replace("VERSION", self.version).replace("GIT_URL",
                                                                                           self.git_url).replace("DOCS",
                                                                                                                 self.docs)

    @property
    def singularity_url_files(self) -> list:
        """List of tuple with downloaded url and install destination with INSTALL_PATH. like INSTALL_PATH/containers/Singularity.CulebrONT_tools.sif"""
        return self._singularity_url_files

    @singularity_url_files.setter
    def singularity_url_files(self, list_url):
        if not list_url:
            raise AttributeError("ERROR 'singularity_url_files' is empty but mandatory")
        if not isinstance(list_url, list):
            raise ValueError(f"ERROR 'singularity_url_files' must be a list of tuple but is {type(list_url)}")
        self._singularity_url_files = [(url, path_install.replace("INSTALL_PATH", self.install_path.as_posix())) for
                                       url, path_install in list_url]

    @property
    def datatest_url_files(self) -> tuple:
        """Tuple with 2 values, first the url of datatest, second download name."""
        return self._datatest_url_files

    @datatest_url_files.setter
    def datatest_url_files(self, tuple_test):
        if not isinstance(tuple_test, tuple) or not len(tuple_test) == 2:
            raise ValueError("ERROR 'datatest_url_files' must be a tuple of 2 values")
        self._datatest_url_files = tuple_test

    @property
    def install_mode(self):
        """Detect install mode of the soft, can be 'No install', 'local' or 'cluster'"""
        if not self.install_mode_file.exists():
            self._install_mode = "No install"
        else:
            self._install_mode = self.install_mode_file.open("r").readline().strip()
        return self._install_mode

    @property
    def tools_mode(self):
        """Detect install mode of the tools soft, can be 'modules' or 'singularity'"""
        if not self.install_mode_file.exists():
            self._tools_mode = "No install"
        else:
            try:
                self._tools_mode = self.install_mode_file.open("r").readlines()[1].strip()
            except IndexError:
                self._tools_mode = f"""Not avail, please update Snakecdysis with  'python3 -m pip install snakecdysis>=0.0.6'
                        \t\tand then reinstall {self.soft_name} with
                        \t\t'{self.soft_name} -r && {self.soft_name} install_{self.install_mode}'"""
        return self._tools_mode

    @property
    def version(self):
        """The current workflow version, read on VERSION file"""
        from datetime import datetime, timedelta

        def update():
            process = subprocess.run(f"python3 -m pip list --format freeze| grep -i {self.soft_name}", shell=True,
                                     check=False, capture_output=True, encoding="UTF-8")
            try:
                version = process.stdout.rstrip().split("==")[1]
            except IndexError as e:
                version = self.install_path.joinpath("VERSION").open("r").readline().strip()
            self._current_file.parent.mkdir(exist_ok=True, parents=True)
            self._current_file.open("w").write(version)
            return version

        if not self._current_file.exists():
            version = update()
        else:
            # get modification time
            file_mod_time = datetime.fromtimestamp(self._current_file.stat().st_mtime)  # This is a datetime.datetime object!
            now = datetime.today()
            max_delay = timedelta(days=15)
            if now - file_mod_time > max_delay:
                version = update()
            elif self._current_file.exists():
                version = self._current_file.open("r").read().strip()
        return version

    @property
    def snakecdysis_version(self):
        """The current workflow version, read on VERSION file"""
        process = subprocess.run(f"python3 -m pip list --format freeze |grep -i snakecdysis", shell=True, check=False,
                                 capture_output=True, encoding="UTF-8")
        return process.stdout.rstrip().split("==")[1]
        #return Path(__file__).parent.joinpath("VERSION").open().read().strip()

    @property
    def latest_version(self):
        """The latest workflow version, read on repository"""
        self.__update_latest_file()
        return self._latest_version

    # SNAKEMAKE SETTINGS
    @property
    def snakefile(self) -> Path:
        """Path to the main snakemake file.
        Search on INSTALL_PATH/snakefiles/snakefile
        """
        return self._snakefile

    @snakefile.setter
    def snakefile(self, snake_path):
        if not Path(snake_path).exists():
            raise FileNotFoundError(f"ERROR  the snakefile '{snake_path}' doesn't exist")
        self._snakefile = Path(snake_path)

    @property
    def snakemake_scripts(self) -> Path:
        """Path to the scripts used on snakemake rules.
        Search on INSTALL_PATH/snakemake_scripts
        """
        return self._snakemake_scripts

    @snakemake_scripts.setter
    def snakemake_scripts(self, script_path) -> Path:
        if not Path(script_path).exists():
            raise FileNotFoundError(f"ERROR  the snakemake_scripts '{script_path}' doesn't exist")
        self._snakemake_scripts = Path(script_path)

    @property
    def default_profile(self) -> Path:
        """Path to the directory of cluster coockiecutter default profile.
        install on INSTALL_PATH/default_profile
        """
        return self._default_profile

    @default_profile.setter
    def default_profile(self, default_profile) -> Path:
        # if not Path(default_profile).exists():
        #     raise NotADirectoryError(f"ERROR  the default_profile '{default_profile}' doesn't exist")
        self._default_profile = Path(default_profile)

    @property
    def git_config_path(self) -> Path:
        """Path to the directory of default config.yaml file.
        default to INSTALL_PATH/install_files/config.yaml
        """
        return self._git_config_path

    @git_config_path.setter
    def git_config_path(self, git_config_path) -> Path:
        if not Path(git_config_path).exists():
            raise FileNotFoundError(f"ERROR  the git_config_path '{git_config_path}' doesn't exist")
        self._git_config_path = Path(git_config_path)

    @property
    def git_tools_path(self) -> Path:
        """Path to the directory of default config.yaml file.
        default to INSTALL_PATH/install_files/tools_path.yaml
        """
        return self._git_tools_path

    @git_tools_path.setter
    def git_tools_path(self, git_tools_path) -> Path:
        if not Path(git_tools_path).exists():
            raise FileNotFoundError(f"ERROR  the git_tools_path '{git_tools_path}' doesn't exist")
        self._git_tools_path = Path(git_tools_path)

    @property
    def user_tools_path(self) -> Path:
        """Path to the user tools path setting.
        default to ~/.config/SOFTNAME/tools_path.yaml
        """
        return Path(f"~/.config/{self.soft_name}/tools_path.yaml").expanduser()

    @property
    def args_tools_path(self) -> Path:
        """Path to the user tools path setting.
        default to ~/.config/SOFTNAME/tools_path_args.yaml
        """
        return Path(f"~/.config/{self.soft_name}/tools_path_args.yaml").expanduser()

    @property
    def user_cluster_config(self) -> Path:
        """Path to the user cluster config path setting.
        default to ~/.config/SOFTNAME/cluster_config.yaml
        """
        return Path(f"~/.config/{self.soft_name}/cluster_config.yaml").expanduser()

    @property
    def args_cluster_config(self) -> Path:
        """Path to the snakemake args cluster config setting.
        default to ~/.config/SOFTNAME/cluster_config_args.yaml
        """
        return Path(f"~/.config/{self.soft_name}/cluster_config_args.yaml").expanduser()

    def get_last_version(self) -> str:
        """Function for know the last version of program (can be GitHub or GitLab repository)
        """
        from urllib.request import urlopen
        from re import search
        try:
            if "github" in self.git_url:
                HTML = urlopen(f"{self.git_url}/tags").read().decode('utf-8')
                str_search = f"{self.git_url.replace('https://github.com', '')}/releases/tag/.*"
                last_release = search(str_search, HTML).group(0).split('"')[0].split("/")[-1]
                self._latest_version = last_release
            else:
                from gitlab import Gitlab
                project_name_with_namespace = "/".join(self.git_url.split("//")[1].split("/")[1:])
                # print(project_name_with_namespace)
                gl = Gitlab(self.git_url.replace(f'/{project_name_with_namespace}', ""))
                project = gl.projects.get(f"{project_name_with_namespace}", lazy=True)
                releases_list = project.releases.list()
                if not releases_list:
                    last_release = "There aren’t any releases"
                else:
                    last_release = releases_list[0].name
                self._latest_version = last_release
        except Exception as e:
            print(e)
            if "403" in f"{e}":
                secho(f"\n    Forbidden access to release version, please check setting on repository\n\n",
                                              fg="red")
                last_release = "Forbidden access"
                self._latest_version = last_release
            elif "404" in f"{e}":
                secho(f"\n    Project Not Found! please check setting URL:{self.git_url}\n\n",
                                              fg="red")
                last_release = "Project Not Found"
                self._latest_version = last_release
            else:
                secho(f"\n    Unable to check release:{e}\n\n",
                                              fg="red")
                last_release = "Unable"
                self._latest_version = last_release

    def __update_latest_file(self, delta_days=30):
        from datetime import datetime, timedelta
        if not Path(self._lasted_file).exists():
            self.get_last_version()
            self._lasted_file.parent.mkdir(exist_ok=True,parents=True)
            self._lasted_file.open("w").write(self._latest_version)
        else:
            # get modification time
            file_mod_time = datetime.fromtimestamp(self._lasted_file.stat().st_mtime)  # This is a datetime.datetime object!
            now = datetime.today()
            max_delay = timedelta(days=delta_days)
            if now - file_mod_time > max_delay:
                #print(f"CRITICAL:last modified on {file_mod_time}. Threshold set to {max_delay} minutes.")
                self.get_last_version()
                self._lasted_file.open("w").write(self._latest_version)
            elif self._lasted_file.exists():
                self._latest_version = self._lasted_file.open("r").read().strip()

    def get_epilog(self) -> str:
        """Function for know the last version of program (can be GitHub or GitLab repository)
           check every 30 days to skip request of if no internet connection

        Return: epilogTool print at the end of header

        """
        self.__update_latest_file()
        epilogTools = "\n"
        if str(self.version) != self._latest_version:
            if self._latest_version < str(self.version):
                epilogTools = click.style(
                    f"\n    ** NOTE: This {self.soft_name} version ({self.version}) is higher than the production version ({self._latest_version}), you are using a dev version\n\n",
                    fg="yellow", bold=True)
            elif self._latest_version > str(self.version) and self._latest_version != "There aren’t any releases":
                epilogTools = click.style(
                    f"\n    ** NOTE: The Latest version of {self.soft_name} {self._latest_version} is available at {self.git_url}\n\n",
                    fg="yellow", underline=True)
            elif self._latest_version == "There aren’t any releases":
                epilogTools = click.style(f"\n    ** NOTE: There aren’t any releases at the moment\n\n", fg="red",
                                          underline=False)
            else:
                epilogTools = click.style(f"\n    ** NOTE: Can't check if new release are available\n\n", fg="red",
                                          underline=False)
        return epilogTools

    def create_bash_completion(self):
        """Add bash completion for version > 4.4"""
        major, minor = None, None
        bashrc_file = Path("~/.bashrc").expanduser().as_posix()
        output = subprocess.run(
            ["bash", "-c", "echo ${BASH_VERSION}"], stdout=subprocess.PIPE
        )
        match = re.search(r"^(\d+)\.(\d+)\.\d+", output.stdout.decode())
        if match is not None:
            major, minor = match.groups()
        if major < "4" or (major == "4" and minor < "4"):
            click.secho(f"\n    WARNING Shell completion is not supported for Bash versions older than 4.4.\n\n",
                        fg="red", nl=False)
            # raise RuntimeError("Shell completion is not supported for Bash versions older than 4.4.")
        else:
            if not Path(f"{self.install_path}/{self.soft_name}-complete.sh").exists():
                build_completion = f"_{self.soft_name.upper()}_COMPLETE=bash_source {self.soft_name} > {self.install_path}/{self.soft_name}-complete.sh"
                os.system(build_completion)
                path_bash = None
                with open(bashrc_file, "r") as bash_file_read:
                    for line in bash_file_read:
                        if f"{self.soft_name.upper()}" in line:
                            path_bash = bash_file_read.readline().strip()
                if path_bash:
                    load = f"{path_bash[2:]}"
                    if f"{self.install_path}/{self.soft_name}-complete.sh" != load:
                        click.secho(
                            f"\n    WARNING autocompletion for {self.soft_name.upper()} already found on {bashrc_file}, with other path please fix the good:",
                            fg="red", nl=False)
                        click.secho(
                            f"\n    Load on bashrc: {load}\n    New install:    {self.install_path}/{self.soft_name}-complete.sh",
                            fg='bright_red')
                else:
                    with open(bashrc_file, "a") as bash_file_open:
                        append_bashrc = f"\n#Add autocompletion for {self.soft_name.upper()}\n. {self.install_path}/{self.soft_name}-complete.sh"
                        bash_file_open.write(append_bashrc)
                        click.secho(
                            f"\n    INSTALL autocompletion for {self.soft_name.upper()} on {bashrc_file} with command {append_bashrc}\nUpdate with command:\nsource ~/.bashrc",
                            fg="yellow")

    def clean_home(self):
        """Reset home's parameters of previous installation"""
        if Path(f"~/.config/{self.soft_name}/").expanduser().exists():
            rmtree(Path(f"~/.config/{self.soft_name}/").expanduser().as_posix())

    def fail(self):
        """If installation fail, reset already install files"""
        rmtree(self.default_profile, ignore_errors=True)
        self.install_mode_file.unlink(missing_ok=True)
        self.clean_home()
        click.secho(f"\n    INSTALL FAIL remove already install files: {self.default_profile} ", fg="red", err=True)
        raise SystemExit

    def write_user_tools_path(self):
        """Check if file is created and then write with modification of singularity path"""
        if not self.user_tools_path.exists():
            self.user_tools_path.parent.mkdir(parents=True, exist_ok=True)
            self.user_tools_path.write_text(
                self.git_tools_path.read_text().replace("INSTALL_PATH", self.install_path.as_posix()))

    def check_and_download_singularity(self):
        """Download singularity/apptainer files if provided"""
        # check if already download if true pop from list
        self.write_user_tools_path()
        SINGULARITY_URL_FILES_DOWNLOAD = []
        for url, path_install in self.singularity_url_files:
            if not Path(path_install).exists():
                Path(path_install).parent.mkdir(parents=True, exist_ok=True)
                SINGULARITY_URL_FILES_DOWNLOAD.append((url, path_install))
                click.secho(f"    File: {path_install} is being downloaded.", fg="yellow", nl=True)
            else:
                click.secho(f"    File: {path_install} already downloaded, done.", fg="yellow", nl=True)
        multiprocessing_download(SINGULARITY_URL_FILES_DOWNLOAD)
        click.secho(
            f"\n    WARNING please check if binding is active on your singularity/apptainer configuration, see https://apptainer.org/docs/user/main/bind_paths_and_mounts.html\n"
            f"    Or use: --singularity-args '--bind $HOME'  on the command line",
            fg="bright_red")

    @property
    def get_active_tools_path(self):
        """return the active path of tools config"""
        if self.user_tools_path.exists() and not self.args_tools_path.exists():
            return self.user_tools_path
        elif self.args_tools_path.exists():
            return self.args_tools_path
        else:
            return self.git_tools_path

    def get_tool_configfile(self):
        """Test path of tools_path.yaml on default install path, home or argument"""
        self.tools_config = load_configfile(self.get_active_tools_path)

    def tools_version_to_df(self, csv_file=None, active_tools_list=None, output_file=None):
        """check how tools install and get version to save on file"""
        if not csv_file:
            click.secho("\n    CODE error, please provide file or active_tools_list", fg="red", err=True)
            raise SystemExit
        self.get_tool_configfile()
        run_all = False
        if not active_tools_list:
            run_all = True
        df = pd.read_csv(csv_file)
        df.fillna('', inplace=True)
        df.sort_values(by=df.columns[0], axis=0, inplace=True)
        df.reset_index(inplace=True,drop=True)
        dico_version_cmd = df.to_dict(orient="index")
        dico_version_value = df.drop(columns=[df.columns[2]]).to_dict(orient="index")

        try:
            with progressbar(dico_version_cmd.items()) as bar:
                for index, dico in bar:
                    tool = dico[df.columns[0]]
                    secondary = dico[df.columns[1]]
                    cmd_version = dico[df.columns[2]]
                    #print(f"\n{tool}, {secondary} {type(secondary)}, {cmd_version}\n")
                    if run_all:
                        active_tools_list.append(tool)
                        active_tools_list.append(secondary)
                    if tool in active_tools_list or secondary in active_tools_list:
                        if self.tools_mode == "singularity":
                            sif_path = self.tools_config["SINGULARITY"]["TOOLS"]
                            run_version_cmd = f"singularity exec {sif_path} {cmd_version}"
                        elif self.tools_mode == "modules":
                            tools_module = self.tools_config["ENVMODULE"]
                            if secondary and secondary.upper() in tools_module.keys():
                                run_version_cmd = f"module load {tools_module[secondary.upper()]} && {cmd_version}"
                            else:
                                run_version_cmd = f"module load {tools_module[tool.upper()]} && {cmd_version}"

                        process = subprocess.run(run_version_cmd, shell=True, check=False, capture_output=True,
                                                 encoding="UTF-8")
                        if int(process.returncode) >= 1:
                            raise SystemExit(f"Error with command line:\n'{run_version_cmd}'\n'{process.stderr.rstrip()}'\n")
                        else:
                            dico_version_value[index]["Version"] = process.stdout.strip()
                    else:
                        dico_version_value.pop(index)
        except UnboundLocalError as e:
            raise SystemExit(f"Error getting mode tools:'{self.tools_mode}\n{self.install_path}\n{self.install_mode_file}\n{self.install_mode}\n")
        except KeyError as e:
            raise SystemExit(f"Error getting Tool '{e}\n, not on avail list: {tools_module.keys()}\n")



        df_version = pd.DataFrame.from_dict(dico_version_value, orient="index")
        desired_order = [df.columns[0], df.columns[1], 'Version', df.columns[3]]
        df_version = df_version[desired_order]
        if output_file:
            # check parent dir
            Path(output_file).parent.mkdir(exist_ok=True, parents=True)
            with open(output_file, "w") as out:
                df_version.to_csv(out, sep=",", index=False)
        return df_version

    def __repr__(self):
        return f"{self.__dict__}"


class SnakEcdysis(SnakeInstaller):
    """ test generic wrapper class

        Args:
            soft_path (str): The path of wrapped workflow installation
            url (str): Url of versioning repository (GitHub or GitLab)
            docs (str): Url of documentation
            description_tool (str):The header print on terminal when run programme. Please add string values 'VERSION', 'GIT_URL' and 'DOCS' and wrapper automatically replace by th good values
            singularity_ur_files (list(tuple()): List of tuple with downloaded url and install destination with INSTALL_PATH. like INSTALL_PATH/containers/Singularity.CulebrONT_tools.sif
            datatest_url_files (tuple): Tuple with 2 values, first the url of datatest, second download name.

    """

    def __init__(self, dico_tool=None, workflow=None, config=None, **kargs):
        if dico_tool:
            super().__init__(**dico_tool)
        else:
            super().__init__(**kargs)
        # workflow is available only in __init__
        # print("\n".join(list(workflow.__dict__.keys())))
        # print(workflow.__dict__)
        self.tools_config = None
        if workflow.overwrite_configfiles:
            self.path_config = workflow.overwrite_configfiles[0]
        else:
            self.path_config = None
        self.config = config

        self.use_env_modules = workflow.use_env_modules
        self.use_conda = workflow.use_conda
        self.use_singularity = workflow.use_singularity
        # test if cluster_config.yaml pass to snakemake
        if not workflow.overwrite_clusterconfig and self.install_mode == "cluster":
            self.cluster_config = load_configfile(self.default_profile.joinpath("cluster_config.yaml"))
        elif not workflow.overwrite_clusterconfig and self.install_mode == "local":
            self.cluster_config = None
        else:
            self.cluster_config = workflow.overwrite_clusterconfig

        self.get_tool_configfile()

    def get_config_value(self, level1, level2=None, level3=None):
        """get value on config_file"""
        if level3:
            return self.config[level1][level2][level3]
        elif level2:
            return self.config[level1][level2]
        else:
            return self.config[level1]

    def set_config_value(self, level1, level2=None, value=None, level3=None):
        """Set config value on config_file"""
        if level3:
            self.config[level1][level2][level3] = value
        elif level2:
            self.config[level1][level2] = value
        else:
            self.config[level1] = value

    def write_config(self, path):
        """Write the corrected config file to path"""
        p = Path(path).parent
        p.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as config_open:
            config_open.write(self.export_use_yaml)

    def check_dir_or_string(self, level1, level2, mandatory=(), level3=None, check_string=False):
        """Check if the specified directory or string exists and is valid in the configuration.

            Parameters:
            - level1 (str): First level in the configuration hierarchy.
            - level2 (str): Second level in the configuration hierarchy.
            - mandatory (tuple): Tuple of mandatory items for the tool.
            - level3 (str): Optional third level in the configuration hierarchy.
            - check_string (bool): Flag to indicate whether to check for a string value.

            Raises:
            - NotADirectoryError: If the specified path does not exist or is not a valid directory.
            - ValueError: If the path is empty when it is expected to be a string.
            """
        path_value = self.get_config_value(level1=level1, level2=level2, level3=level3)
        if path_value:
            path = Path(path_value).resolve().as_posix() + "/"
            # it is a path
            if path_value != "" and "/" in path_value:
                if (not Path(path).exists() or not Path(path).is_dir()) and level2 not in ["OUTPUT"]:
                    raise NotADirectoryError(
                        f'CONFIG FILE CHECKING FAIL : in section:{level1}, {f"subsection:{level2} directory:{level3}" if level3 else f"directory:{level2}"}, "{path}" {"does not exist" if not Path(path).exists() else "is not a valid directory"}')
                else:
                    self.set_config_value(level1=level1, level2=level2, level3=level3, value=path)
            # it is not a path
            elif path_value and "/" not in path_value and check_string:
                self.set_config_value(level1=level1, level2=level2, level3=level3, value=path_value)
            # it is empty
            elif path_value and "/" not in path_value and check_string:
                raise ValueError(
                    f'CONFIG FILE CHECKING FAIL : in section:{level1}, {f"subsection:{level2} value:{level3}" if level3 else f"value:{level2}"}, "{path_value}" is empty')
        elif len(mandatory) > 0:
            raise NotADirectoryError(
                f'CONFIG FILE CHECKING FAIL : in section:{level1}, {f"subsection:{level2} directory:{level3}" if level3 else f"directory:{level2}"}, "{path_value}" {"does not exist" if not Path(path_value).exists() else "is not a valid directory"} but is mandatory for tool: "{",".join(mandatory)}"')

    def check_file_or_string(self, level1, level2, mandatory=(), level3=None, check_string=False):
        """Check if path is a file if not empty
        :return absolute path file"""
        path_value = self.get_config_value(level1=level1, level2=level2, level3=level3)
        path = Path(path_value).resolve().as_posix()
        # it is a path
        if path_value != "" and "/" in path_value:
            if not Path(path).exists() or not Path(path).is_file():
                raise FileNotFoundError(
                    f'CONFIG FILE CHECKING FAIL : in section:{level1}, {f"subsection:{level2}, file {level3}" if level3 else f"file {level2}"}, "{path}" {"does not exist" if not Path(path).exists() else "is not a valid file"}')
            else:
                self.set_config_value(level1=level1, level2=level2, level3=level3, value=path)
        # it is not a path
        elif path_value != "" and "/" not in path_value and check_string:
            self.set_config_value(level1=level1, level2=level2, level3=level3, value=path_value)
        # it is empty
        elif path_value == "" and "/" not in path_value and check_string:
            raise ValueError(
                f'CONFIG FILE CHECKING FAIL : in section:{level1}, {f"subsection:{level2}, value {level3}" if level3 else f"value:{level2}"}, "{path_value}" is empty')
        elif len(mandatory) > 0:
            raise FileNotFoundError(
                f'CONFIG FILE CHECKING FAIL : in  section:{level1} , {f"subsection:{level2}, value {level3}" if level3 else f"value:{level2}"}, "{path_value}" {"does not exist" if not Path(path_value).exists() else "is not a valid file"} but is mandatory for tool: "{",".join(mandatory)}"')

    @property
    def export_use_yaml(self):
        """Use to print a dump config.yaml with corrected parameters"""

        def represent_dictionary_order(yamldef, dict_data):
            return yamldef.represent_mapping('tag:yaml.org,2002:map', dict_data.items())

        def setup_yaml():
            yaml.add_representer(OrderedDict, represent_dictionary_order)

        setup_yaml()
        return yaml.dump(self.config, default_flow_style=False, sort_keys=False, indent=4)

    @property
    def string_to_dag(self):
        """ return command line for rule graph """
        return f"""snakemake -s {self.snakefile} {'--use-singularity' if self.use_singularity else ''} {'--use-envmodules' if self.use_env_modules else ''}  --rulegraph"""

    def __repr__(self):
        return f"{self.__class__}({pprint.pprint(self.__dict__)})"
