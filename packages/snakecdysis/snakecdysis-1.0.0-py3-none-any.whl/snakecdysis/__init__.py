from .snake_wrapper import SnakEcdysis, SnakeInstaller
from .cli_wrapper import main_wrapper
from .useful_function import *


__version__ = Path(__file__).parent.resolve().joinpath("VERSION").open("r").readline().strip()

__doc__ = """
Are you looking for a simplified installation process for your Snakemake workflows, including the various Python packages and the multitude of tools used by your pipelines? 

Would you like to simplify the use of your workflows with user-friendly commands and subcommands that even non-bioinformatician users can easy use? Look no further - Snakecdysis is the solution for you!

"""


dico_tool = {
        "soft_path":  Path(__file__).resolve().parent.joinpath("templates", "PKGNAME"),
        "url": "https://forge.ird.fr/phim/sravel/snakecdysis",
        "docs": "https://snakecdysis.readthedocs.io/en/latest/index.html",
        "description_tool": """ 
    Welcome to Snakecdysis version: VERSION! Created on January 2022
    @author: Sebastien Ravel (CIRAD), Theo Durand, Simon Bache
    @email: sebastien.ravel@cirad.fr
    Please cite our github: GIT_URL
    Licencied under CeCill-C (http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html)
    and GPLv3 Intellectual property belongs to CIRAD and authors.
    Documentation avail at: DOCS""",
        "singularity_url_files": [('http://nas-bgpi.myds.me/DOC/rattleSNP/Singularity.rattleSNP_tools.sif',
                                   'INSTALL_PATH/containers/Singularity.rattleSNP_tools.sif'),
                                  ('http://nas-bgpi.myds.me/DOC/rattleSNP/Singularity.report.sif',
                                   'INSTALL_PATH/containers/Singularity.report.sif')
                                  ],
        "datatest_url_files": (
            "http://nas-bgpi.myds.me/DOC/rattleSNP/data_test_rattleSNP.zip", "data_test_rattleSNP.zip"),
    "snakemake_scripts": Path(__file__).resolve().parent.joinpath("templates", "PKGNAME", "snakemake_scripts")
    }