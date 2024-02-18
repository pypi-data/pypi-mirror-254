#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .global_variables import *
from PKGNAME.module import PKGNAME
from pathlib import Path
from .global_variables import GIT_URL, DOCS, DATATEST_URL_FILES, SINGULARITY_URL_FILES

logo = Path(__file__).parent.resolve().joinpath('PKGNAME_logo.png').as_posix()

__version__ = Path(__file__).parent.resolve().joinpath("VERSION").open("r").readline().strip()


__doc__ = """BLABLA"""

description_tools = f"""
    Welcome to PKGNAME version: {__version__} ! Created on XXXX 20XX
    @author: Sebastien Ravel (CIRAD)
    @email: Sebastien.ravel@cirad.fr

    Please cite our github: GIT_URL
    Licencied under MIT and Intellectual property belongs to XXXX and authors.
    Documentation avail at: DOCS"""

dico_tool = {
    "soft_path": Path(__file__).resolve().parent.as_posix(),
    "url": GIT_URL,
    "docs": DOCS,
    "description_tool": description_tools,
    "singularity_url_files": SINGULARITY_URL_FILES,
    "datatest_url_files": DATATEST_URL_FILES,
    "snakefile": Path(__file__).resolve().parent.joinpath("snakefiles", "Snakefile"),
    "snakemake_scripts": Path(__file__).resolve().parent.joinpath("snakemake_scripts")
}
