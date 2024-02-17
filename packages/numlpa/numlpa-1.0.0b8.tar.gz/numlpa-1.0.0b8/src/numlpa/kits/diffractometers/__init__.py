# -*- coding: utf-8 -*-

"""Numerical diffractometers.

This package gathers the implementations of the X-ray diffraction
simulators. These return the amplitude of the Fourier transform of
the diffracted intensity. According to the kinematical theory of
X-ray scattering [1]_, the Fourier transform is calculated from
the displacement field of the defects:

.. math::

   A(L) = \\frac{1}{V} \\int_V \\exp\\left(2 \\pi i \\mathbf{g} \\cdot
   \\left[\\mathbf{u}(\\mathbf{r}+\\mathbf{L}) -
   \\mathbf{u}(\\mathbf{r})\\right] \\right) \\mathrm{d}\\mathbf{r}

With:

* :math:`A` Fourier transform amplitude.

* :math:`\\mathbf{L}` Fourier variable vector, perpendicular to the
  diffracting lattice planes (:math:`\\mathrm{m}`).

* :math:`V` volume of the region of interest (:math:`\\mathrm{m}^{3}`).

* :math:`\\mathbf{g}` diffraction vector (:math:`\\mathrm{m}^{-1}`).

* :math:`\\mathbf{u}` displacement field (:math:`\\mathrm{m}`).

For screw dislocations, the directions :math:`(\\mathbf{e}_x,
\\mathbf{e}_y, \\mathbf{e}_z)` of the dislocation reference frame are
constructed as follows:

* :math:`\\mathbf{e}_z` is parallel to the dislocation line direction

* :math:`\\mathbf{e}_x` is parallel to the cross product of
  :math:`\\mathbf{e}_z` and the diffraction vector :math:`\\mathbf{g}`

* :math:`\\mathbf{e}_y` is given by the cross product of
  :math:`\\mathbf{e}_z` and :math:`\\mathbf{e}_x`

For edge and mixed dislocations, the directions :math:`(\\mathbf{e}_x,
\\mathbf{e}_y, \\mathbf{e}_z)` of the dislocation reference frame are
constructed as follows:

* :math:`\\mathbf{e}_z` is parallel to the dislocation line direction

* :math:`\\mathbf{e}_x` is parallel to the projection of the Burgers
  vector :math:`\\mathbf{b}` on the plane perpendicular to
  :math:`\\mathbf{e}_z`

* :math:`\\mathbf{e}_y` is given by the cross product of
  :math:`\\mathbf{e}_z` and :math:`\\mathbf{e}_x`

The resulting displacement field at a point is obtained by summing
the contributions of each dislocation. The displacement field induced
by a single dislocation is given in the dislocation reference frame
by: [2]_

.. math::

   \\mathbf{u} = \\left( \\begin{array}{c}
   \\frac{b_e}{2 \\pi} \\left( \\arctan\\left(\\frac{y}{x}\\right) +
   \\frac{xy}{2(1-\\nu)(x^2+y^2)} \\right) \\\\
   - \\frac{b_e}{8 \\pi (1 - \\nu)} \\left( (1-2\\nu) \\ln\\left(
   \\frac{x^2 + y^2}{b^2} \\right) - \\frac{2 y^2}{x^2 + y^2}
   \\right) \\\\
   \\frac{b_s}{2 \\pi} \\arctan\\left(\\frac{y}{x}\\right)
   \\end{array} \\right)

With:

* :math:`b_e` length of the projection of the Burgers vector
  :math:`\\mathbf{b}` on the plane perpendicular to
  :math:`\\mathbf{e}_z` (:math:`\\mathrm{m}`).

* :math:`b_s` length of the projection of the Burgers vector
  :math:`\\mathbf{b}` on the axis
  :math:`\\mathbf{e}_z` (:math:`\\mathrm{m}`).

* :math:`x` position x-coordinate in the dislocation reference frame
  (:math:`\\mathrm{m}`).

* :math:`y` position y-coordinate in the dislocation reference frame
  (:math:`\\mathrm{m}`).

* :math:`\\nu` Poisson's number.

Finally, we define a quantity :math:`\\langle {\\varepsilon_L}^2
\\rangle` equal to the mean square strain :math:`\\langle
{\\varepsilon_0}^2 \\rangle` when :math:`L` tends towards :math:`0`:

.. math::

   \\langle {\\varepsilon_L}^2 \\rangle = \\frac{1}{V} \\int_V  \\left(
   \\frac{\\mathbf{e}_g \\cdot \\left[\\mathbf{u}(\\mathbf{r}+\\mathbf{L}) -
   \\mathbf{u}(\\mathbf{r})\\right]}{L} \\right)^2 \\mathrm{d}\\mathbf{r}

References
----------

.. [1] B. E. Warren.
   X-Ray diffraction. Dover Publications, 1990. ISBN: 978-0-48-666317-3.

.. [2] F. R. N. Nabarro.
   Theory of crystal dislocations. Oxford Clarendon Press, 1967.

"""
