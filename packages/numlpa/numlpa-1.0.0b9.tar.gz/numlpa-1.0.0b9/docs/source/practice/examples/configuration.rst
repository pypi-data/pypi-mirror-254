Configuration
=============

There are two ways to configure options:

* By using a customized configuration file.
* By specifying options in the command (from a terminal) or function call (from a Python script).

.. note::

   * When a configuration file is used, the parameters it contains replace the default ones.

   * When options are passed in the command or function call, they replace default parameters and parameters defined in the configuration file.

Command-line interface with options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What will be your best ally in configuring the features is the ``-h`` or ``--help`` option.
This option will show you what can be configured at each stage of the construction of a command.
Start by running the following command:

.. code-block:: bash

   numlpa -h

You will then see what you can put after "numlpa" in the command line.

In the previous page we generated some samples of dislocations with the ``draw`` subparser.
If you want to know what options are available for this subparser, run the ``numlpa draw -h`` command.
You will discover that there is a positional argument just after ``output_path`` that can take different values (``dipoles``, ``images`` ...).
Then, you can use the ``images`` distribution with the following command:

.. code-block:: bash

   numlpa draw samples images

To discover the options proposed by the ``images`` subparser you can run ``numlpa draw images -h``.
For example, if you want to change the number of dislocations in the region of interest, execute the following command:

.. code-block:: bash

   numlpa draw samples-400p images --number 400

.. note::

   The command-line interface (CLI) uses nested subparsers.
   Therefore, options for a given parser must be placed just after the parser name and before its potential subparsers.

In the options available for the ``draw`` parser, there is ``--size``, the number of samples.
If you want to change this option, you have to add the value **after** the ``draw`` subparser, and **before** the ``images`` subpaser:

.. code-block:: bash

   numlpa draw samples-400p-100 --size 100 images --number 400

Command-line interface with a configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Everything that can be configured via the CLI can also be configured from a configuration file.
The default configuration of the package is defined in the `default.conf <https://gitlab.com/x-rays/numlpa/-/blob/main/src/numlpa/default.conf?ref_type=heads>`_ file.
The easiest way to create your own configuration file is to copy this file and modify its content.

Let's now assume that you have named your own configuration file ``custom.conf``.
To use the ``images`` distribution, without specifying it in the command line, change the value of the ``distribution`` entry in the ``numlpa.main.draw`` section of the configuration file and run:

.. code-block:: bash

   numlpa --config custom.conf draw custom-samples

It is not necessary to keep all the sections in the configuration file.
You can delete all the sections and options you have not modified.
If you look at the structure of the package, you will notice that the names of the sections correspond to the names of the modules to which the options are attached.

Python script with options
~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the Python script equivalent of the commands passed to the command-line interface above.

.. code-block:: python

   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-

   import numlpa.api

   # with keywords
   numlpa.api.draw('samples', distribution='images')

   # with expanded dictionaries
   numlpa.api.draw('samples-400p', **{'distribution': 'images', 'number': 400})

   # with bigger expanded dictionaries
   parameters = {
       'output_path': 'samples-400p-100',
       'size': 100,
       'distribution': 'images',
       'number': 400,
   }
   numlpa.api.draw(**parameters)

Python script with a configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To load a configuration file ``custom.conf`` from a Python script, proceed as follows:

.. code-block:: python

   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-

   import numlpa.api

   # load the configuration file
   numlpa.api.load_config('custom.conf')

   # the default options are now those in the configuration file
   numlpa.api.draw('custom-samples')
