How to convert my snakemake workflow into a Python package combined to Snakecdysis  ?
=====================================================================================

.. contents::
   :depth: 3
   :backlinks: entry
   :local:

Generating the python package tree
----------------------------------

The first step is to structure your Git repository as a Python package. To help you in this process, you can use the snackecdysis command `generate_template` with the following parameters:

* `-p GitHub_Repo_Name`. In lower case, corresponding to the name of the repo (e.g.: culebrONT for http://...)
* `-n package_Name`. In lowcase case (python nomenclature) (e.g.: culebrONT )

.. code-block:: bash

    generate_template -p GitHub_Repo_Name -n package_Name

Running this command generates all the files and directories needed to create a python package.
This package is then ready to be used by snakecdysis, simplifying the installation and use of your snakemake pipeline.

.. image:: _images/directory.png
  :alt: directory

now I will explain what you have to modify in the files to create your package.
You must adapt the highlighted lines on example files, to your project.


Configuring your files
----------------------

Include specific configurations and settings here.

pyproject.toml file
~~~~~~~~~~~~~~~~~~~

This file is used to create a python package as described `here in the official documentation <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_.

.. dropdown:: click to open pyproject.toml
    :octicon:`tools;1em;sd-text-info`

    .. literalinclude:: ../../snakecdysis/templates/pyproject.toml
       :language: toml
       :emphasize-lines: 18,20,22-23,26-60,118-119
       :linenos:


The __init__.py file
~~~~~~~~~~~~~~~~~~~~

This file is the entry point of the python package.

.. dropdown:: click to open __init__.py
    :octicon:`package;1em;sd-text-info`

    .. literalinclude:: ../../snakecdysis/templates/PKGNAME/__init__.py
       :language: python
       :emphasize-lines: 4,8,13,15-33
       :linenos:

global_variables.py file
~~~~~~~~~~~~~~~~~~~~~~~~

This file allows to group the variables to be used in the wrapper

.. dropdown:: click to open global_variables.py
    :octicon:`key-asterisk;1em;sd-text-info`

    .. literalinclude:: ../../snakecdysis/templates/PKGNAME/global_variables.py
       :language: python
       :emphasize-lines: 3,4,7-11
       :linenos:

main.py file
~~~~~~~~~~~~

This is the main script of the workflow.
You have to check that its path is in the setup.py file.
Normally it is already included with the instruction line 75:

.. code-block:: python

        entry_points={
            'console_scripts': [f"{NAME} = {NAME}.main:main"],
        },

This is the main script of the workflow.
You have to check that its path is in the setup.py file.
Normally it is already included with the instruction line 75:

.. dropdown:: click to open main.py
    :octicon:`play;1em;sd-text-info`

    .. literalinclude:: ../../snakecdysis/templates/PKGNAME/main.py
       :language: python
       :linenos:



Transferring your snakemake workflow
------------------------------------
Include blabla on how to transfer your Snakemake workflow into the newly generated Python package.


module.py file
~~~~~~~~~~~~~~

This file is used on :ref:`snakefile file` to add more control of the configuration file and checking user values.
The goal is to create a new class that inherits from :ref:`SnakEcdysis <SnakEcdysis>` in order to use the attributes in order
to have access to, for example, the paths of the scripts, the default/user configuration files, ...



.. dropdown:: click to open module.py
    :octicon:`shield-check;1em;sd-text-info`

    .. literalinclude:: ../../snakecdysis/templates/PKGNAME/module.py
       :language: python
       :linenos:


snakefile file
~~~~~~~~~~~~~~

.. dropdown:: click to open snakefile
    :octicon:`file-code;1em;sd-text-info`

    .. literalinclude:: ../../snakecdysis/templates/PKGNAME/snakefiles/snakefile
       :language: python
       :linenos:

update documentation comming soon
---------------------------------
# USER manual - How to install my workflow after developping the python package of my workflow