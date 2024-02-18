# -*- coding: utf-8 -*-

"""Strain energy evaluators.

This package gathers the implementations of the strain energy
evaluators. These return the value of the strain energy density and
the outer cut-off radius. According to the elasticity theory [1]_ [2]_,
the strain energy is written:

.. math::

   dE = \\frac{1}{2} dV \\sum_{i=x,y,z} \\sum_{j=x,y,z} \\sigma_{ij}
   \\varepsilon_{ij}

With:

* :math:`E` strain energy (:math:`\\mathrm{J}`).

* :math:`V` volume (:math:`\\mathrm{m}^3`).

* :math:`\\sigma` stress tensor (:math:`\\mathrm{Pa}`).

* :math:`\\varepsilon` strain tensor.

The following quantities are also introduced:

* :math:`b` Burgers vector length (:math:`\\mathrm{m}`).

* :math:`x` position x-coordinate in the dislocation reference frame
  (:math:`\\mathrm{m}`).

* :math:`y` position y-coordinate in the dislocation reference frame
  (:math:`\\mathrm{m}`).

* :math:`\\nu` Poisson's number.

* :math:`G` shear modulus (:math:`\\mathrm{Pa}`).

For screw dislocations, the directions :math:`(\\mathbf{e}_x,
\\mathbf{e}_y, \\mathbf{e}_z)` of the dislocation reference frame are
constructed as follows:

* :math:`\\mathbf{e}_z` is parallel to the dislocation line direction

* :math:`\\mathbf{e}_x` is parallel to the cross product of
  :math:`\\mathbf{e}_z` and the diffraction vector :math:`\\mathbf{g}`

* :math:`\\mathbf{e}_y` is given by the cross product of
  :math:`\\mathbf{e}_z` and :math:`\\mathbf{e}_x`

The strain field induced by a single screw dislocation is written in
the dislocation reference frame:

.. math::

   \\varepsilon_{xx} &= \\varepsilon_{yy} = \\varepsilon_{zz} = 0

   \\varepsilon_{xy} &= \\varepsilon_{yx} = 0

   \\varepsilon_{yz} &= \\varepsilon_{zy} = \\frac{b}{4 \\pi}
   \\frac{x}{x^2 + y^2}

   \\varepsilon_{zx} &= \\varepsilon_{xz} = - \\frac{b}{4 \\pi}
   \\frac{y}{x^2 + y^2}

The stress field induced by a single screw dislocation is written in
the dislocation reference frame:

.. math::

   \\sigma_{xx} &= \\sigma_{yy} = \\sigma_{zz} = 0

   \\sigma_{xy} &= \\sigma_{yx} = 0

   \\sigma_{yz} &= \\sigma_{zy} = \\frac{G b}{2 \\pi} \\frac{x}{
   x^2 + y^2}

   \\sigma_{zx} &= \\sigma_{xz} = - \\frac{G b}{2 \\pi} \\frac{y}{
   x^2 + y^2}

For edge dislocations, the directions :math:`(\\mathbf{e}_x,
\\mathbf{e}_y, \\mathbf{e}_z)` of the dislocation reference frame are
constructed as follows:

* :math:`\\mathbf{e}_z` is parallel to the dislocation line direction

* :math:`\\mathbf{e}_x` is parallel to the Burgers vector
  :math:`\\mathbf{b}`

* :math:`\\mathbf{e}_y` is given by the cross product of
  :math:`\\mathbf{e}_z` and :math:`\\mathbf{e}_x`

The strain field induced by a single edge dislocation is written in
the dislocation reference frame:

.. math::

   \\varepsilon_{xx} &= - \\frac{b}{4 \\pi (1 - \\nu)}
   \\frac{y}{x^2 + y^2}
   \\left( \\frac{x^2 - y^2}{x^2 + y^2} + 2 (1 - \\nu) \\right)

   \\varepsilon_{yy} &= \\frac{b}{4 \\pi (1 - \\nu)}
   \\frac{y}{x^2 + y^2}
   \\left( \\frac{3x^2 + y^2}{x^2 + y^2} - 2 (1 - \\nu) \\right)

   \\varepsilon_{zz} &= 0

   \\varepsilon_{xy} &= \\varepsilon_{yx} = \\frac{b}{4 \\pi (1 - \\nu)}
   \\frac{x (x^2 - y^2)}{(x^2 + y^2)^2}

   \\varepsilon_{yz} &= \\varepsilon_{zy} = 0

   \\varepsilon_{zx} &= \\varepsilon_{xz} = 0

The stress field induced by a single edge dislocation is written in
the dislocation reference frame:

.. math::

   \\sigma_{xx} &= - \\frac{G b}{2 \\pi (1 - \\nu)} \\frac{y (3x^2 +
   y^2)}{(x^2 + y^2)^2}

   \\sigma_{yy} &= \\frac{G b}{2 \\pi (1 - \\nu)} \\frac{y (x^2 - y^2)
   }{(x^2 + y^2)^2}

   \\sigma_{zz} &= \\nu(\\sigma_{xx} + \\sigma_{yy})

   \\sigma_{xy} &= \\sigma_{yx} = \\frac{G b}{2 \\pi (1 - \\nu)}
   \\frac{x (x^2 - y^2)}{(x^2 + y^2)^2}

   \\sigma_{yz} &= \\sigma_{zy} = 0

   \\sigma_{zx} &= \\sigma_{xz} = 0

We introduce the effective outer cut-off ratio :math:`R_e` with the
following expressions:

.. math::

   E_{\\text{screw}} &= V \\frac{G b^2}{4 \\pi} \\rho \\ln\\left(
   \\frac{R_e}{r_0} \\right)

   E_{\\text{edge}} &= V \\frac{G b^2}{4 \\pi (1 - \\nu)} \\rho
   \\ln\\left( \\frac{R_e}{r_0} \\right)

With:

* :math:`\\rho` dislocation density (:math:`\\mathrm{m}^{-2}`).

* :math:`R_e` outer cut-off radius (:math:`\\mathrm{m}`).

* :math:`r_0` dislocation core radius (:math:`\\mathrm{m}`).

Finally, we define the mean square strain
:math:`\\langle {\\varepsilon_0}^2 \\rangle` as the average of the
square of the projected strain tensor :math:`\\varepsilon`
along the direction :math:`\\mathbf{e}_g` of the diffraction vector
:math:`\\mathbf{g}`:

.. math::

   \\langle {\\varepsilon_0}^2 \\rangle = \\langle (\\mathbf{e}_g
   \\varepsilon \\mathbf{e}_g)^2 \\rangle

References
----------

.. [1] D. Hull and D. J. Bacon.
   Introduction to dislocations. Elsevier, 2011. ISBN:
   978-0-08-096672-4. DOI: 10.1016/C2009-0-64358-0.

.. [2] F. R. N. Nabarro.
   Theory of crystal dislocations. Oxford Clarendon Press, 1967.

"""
