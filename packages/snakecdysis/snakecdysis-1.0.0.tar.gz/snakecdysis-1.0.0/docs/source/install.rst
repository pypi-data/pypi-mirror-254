Install Snakecdysis python package
==================================

.. contents::
   :depth: 3
   :backlinks: entry
   :local:

Requirement
-----------

Snakecdysis requires |PythonVersions| and a snakemake workflow to wrapped.

Some wrapped workflow examples:

- https://culebront-pipeline.readthedocs.io/
- https://rattlesnp.readthedocs.io
- https://podiumasm.readthedocs.io/en/latest/


------------------------------------------------------------------------

Install the lastest release from PyPI  - RECOMMENDED
----------------------------------------------------

Install the latest release of Snakecdysis package using pip

.. code-block:: bash

    python3 -m pip install snakecdysis

Now, follow this documentation to wrapped command line of your favorite workflow !!!!


Install the development version directly from the github repository
-------------------------------------------------------------------

You can test new futures not yet included in the latest release !

.. warning::
   Caution, still in development mode

.. code-block:: bash

   python3 -m pip install snakecdysis@git+https://forge.ird.fr/phim/sravel/snakecdysis.git@main

You can replace `main` with the name of the Git branch you are testing

.. |PythonVersions| image:: https://img.shields.io/badge/python-3.8%2B-blue
   :target: https://www.python.org/downloads
   :alt: Python 3.8+