Vanilla example
===============

There are two ways to run numlpa:

* Using the command-line interface (through a terminal).
* Using a Python script (in which the package is imported).

NumLPA contains a default configuration of almost all parameters.
You will see later how to replace the default values.
For now, and thanks to all the preconfigured parameters, you will be able to test the package features with a minimum of effort.

Using the command-line interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to a blank working directory and run the following commands in a terminal:

.. code-block:: bash

   # generate dislocation samples
   numlpa draw samples.tar

   # evaluate strain energy
   numlpa evaluate samples.tar evaluations.tar

   # merge energy evaluations
   numlpa merge evaluations.tar evaluation.tar

   # compute Fourier transforms
   numlpa diffract samples.tar transforms.tar

   # merge Fourier transforms
   numlpa merge transforms.tar transform.tar

   # fit a model
   numlpa fit transform.tar adjustments.tar

   # generate figures
   numlpa export samples.tar fig-samples
   numlpa export transforms.tar fig-transforms
   numlpa export transform.tar fig-transform
   numlpa export adjustments.tar fig-adjustments

   # show the density accuracy of the model
   numlpa extract adjustments.tar -e parameters.relative.0 --mean

Here the figures are sent directly to folders for easy viewing, and the raw data is sent to tarballs.
But all input/output file containers can take the form of a zip file, a tarball or a folder.
The choice is yours.
Just remove the `.tar`, or replace it with a `.zip`, if you want to store the files in a different kind of container.

Using a Python script
~~~~~~~~~~~~~~~~~~~~~

Go to a blank working directory and create a Python script ``vanilla.py`` as follows:

.. code-block:: python

   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-

   import numlpa.api

   # generate dislocation samples
   numlpa.api.draw('samples.tar')

   # evaluate strain energy
   numlpa.api.evaluate('samples.tar', 'evaluations.tar')

   # merge energy evaluations
   numlpa.api.merge('evaluations.tar', 'evaluation.tar')

   # compute Fourier transforms
   numlpa.api.diffract('samples.tar', 'transforms.tar')

   # merge Fourier transforms
   numlpa.api.merge('transforms.tar', 'transform.tar')

   # fit a model
   numlpa.api.fit('transform.tar', 'adjustments.tar')

   # generate figures
   numlpa.api.export('samples.tar', 'fig-samples')
   numlpa.api.export('transforms.tar', 'fig-transforms')
   numlpa.api.export('transform.tar', 'fig-transform')
   numlpa.api.export('adjustments.tar', 'fig-adjustments')

   # show the density accuracy of the model
   accuracy = numlpa.api.extract(
      'adjustments.tar',
      entry='parameters.relative.0',
      mean=True,
   )

Now simply run the script:

.. code-block:: bash

   python3 vanilla.py
