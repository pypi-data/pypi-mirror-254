# ![NumLPA](docs/source/logo.svg)

What does it mean?

> The name "NumLPA" comes from the contraction of "Numerical Line Profile Analysis".

What is the use of it?

> NumLPA is a Python package developed for research in materials science.

Is it hard to use?

> Just type one of the available commands in a terminal and look at the generated files.

## Background

The physical properties of a solid material are strongly impacted by the nature and quantity of structural defects it contains.
It is therefore important to have reliable tools to characterize deviations from a perfect crystal.
Line Profile Analysis (LPA) is one of the methods used for the study of microstructures from the analysis of X-ray diffraction patterns.

## Features

NumLPA Has been developed to meet the need to analyze the accuracy of LPA models.
The main features of the package are presented bellow:

* `draw`: Generate samples of dislocations by random drawing from different probability distribution models.
* `diffract`: Simulate X-ray diffraction on crystals containing the previously generated dislocations and compute the Fourier transform of the diffracted intensity.
* `merge`: Average the Fourier transform coefficients or the strain energy evaluations from multiple samples drawn from a same distribution.
* `fit`: Fit LPA models on the simulated diffraction profiles to obtain their predictions and compare them to the real parameters of the distribution.
* `evaluate`: Compute the strain energy density and the outer cut-off radius for a sample of dislocations.
* `analyze`: Perform a spatial statistical analysis and calculate the strain energy contained in a sample of dislocations.
* `export`: Export figures illustrating the previously generated data according to different representations.

## Installation

You can find how to install the package in the [installation section](https://x-rays.gitlab.io/numlpa/practice/installation/index.html) of the documentation.

## Usage

You can find how to use the package in the [examples section](https://x-rays.gitlab.io/numlpa/practice/examples/index.html) of the documentation.

## Credits

* Dunstan Becht
* Asdin Aoufi
* András Borbély

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
