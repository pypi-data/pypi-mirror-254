Editable installation
=====================

This page shows how to install the package in `editable (or development) mode <https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode>`_.
With this installation option, you will be able to work on the package source files and quickly test the changes.

.. note::

   If you have not already done so, please install `Git <https://git-scm.com>`_ on your computer.

Clone the project from its `GitLab repository <https://gitlab.com/x-rays/numlpa>`_ with the command below.

.. code-block:: bash

   git clone https://gitlab.com/x-rays/numlpa.git

The `makefile <https://gitlab.com/x-rays/numlpa/-/blob/main/makefile>`_ has been specially created to automate certain operations such as the editable installation of the package in development mode.
To install the package, simply run the command:

.. code-block:: bash

   make
