Energy evaluation data format
=============================

An energy evaluation is the result of the calculation of the strain energy density over the region of interest.
The data related to an energy evaluation is contained in a dictionary whose structure is given below.

.. code-block:: python

   {
       'metadata': {
           'type': 'energy-evaluation',
           'date': 'YYYY-MM-DDTHH:MM:SS+00:00',
           'version': version_tuple,
       },
       'distribution': {
           ...
       },
       'region': {
           ...
       },
       'evaluation': {
           'module': 'numlpa.kits.evaluators.name',
           'z_uvw': [u, v, w],
           'b_uvw': [u, v, w],
           'g_hkl': [h, k, l],
           'type': 'dislocation-type',
           'cell': cell,
           'b_len': b_len,
           'poisson': poisson,
           'shear': shear,
           'core': core,
           'energy_mean': energy_mean,
           'energy_deviation': energy_deviation,
           'square_strain': square_strain,
           'factor': factor,
           'cutoff': cutoff,
           'samples': samples,
           'replicate': replicate,
           'duration': duration,
           'points': points,
           ...
       },
   }


Description of mandatory entries:

* ``metadata``: Section containing general information related to the nature of the data.

  * ``type``: Identifier associated with the data category.

  * ``date``: Date of data generation, in `ISO 8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`_ standard.

  * ``version``: Version of NumLPA.

* ``distribution``: Section containing data related to the dislocation probability distribution.

  * See :doc:`dislocation sample data format <dislocation-sample>`.

* ``region``: Section containing data related to the region of interest.

  * See :doc:`dislocation sample data format <dislocation-sample>`.

* ``evaluation``: Section containing data related to the strain energy evaluation.

  * ``module``: Name of the module used for the evaluation.

  * ``z_uvw``: Direction of the line vector (uvw).

  * ``b_uvw``: Direction of the Burgers vector (uvw).

  * ``g_hkl``: Direction of the diffraction vector (hkl).

  * ``type``: Dislocation type (``'screw'`` or ``'edge'``).

  * ``cell``: Lattice constant (in metre).

  * ``b_len``: Burgers vector length (in metre).

  * ``poisson``: Poisson number.

  * ``shear``: Shear modulus (in pascal).

  * ``core``: Core radius (in metre).

  * ``energy_mean``: Average strain energy density (in joule per cubic meter).

  * ``energy_deviation``: Strain energy density standard deviation (in joule per cubic meter).

  * ``square_strain``: Mean square strain along the diffraction vector.

  * ``factor``: Multiplication factor of the strain energy density for the calculation of the outer radius cut-off (cubic meter per joule).

  * ``cutoff``: Outer cut-off radius (in metre).

  * ``samples``: Number of dislocation samples used.

  * ``replicate``: Number of replication of the region of interest.

  * ``duration``: Calculation time (in second).

  * ``points``: Number of random points for the Monte Carlo method.
