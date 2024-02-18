#!/usr/bin/env python3
from snakecdysis import main_wrapper
from pathlib import Path

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
main = main_wrapper(**dico_tool)

if __name__ == '__main__':
    main()
