.. _modulation:

=========================
Complex modulation signal
=========================

The SAR image cross-spectra is meant to quantify the spatial frequency content of the cross-section modulations.
The modulations are the relative variation of the radar cross-section relatively to the mean radar cross section of the image.
As we are interested with the frequency content due to wave modulation, we define the mean radar cross-section as the average of the radar cross-section over a prescribed image extension (typically 1 km x 1 km).

It writes:

.. math::
   I_{low} = |\overline{DN}|^2\star G

where :math:`\star` operators stands for the convolution and with :math:`G` a normalized Gaussian-filter with a customizable 1 km x 1 km standard deviations.

The complex Digital Number modulations thus writes:

.. math::
  :label: DNmod

    \widetilde{DN} = \dfrac{\overline{DN}}{\sqrt{I_{low}}}


**********************************************
Computation of the sigma0 normalized variance
**********************************************

The normalized variance is the variance of the Digital number defined over a prescribed spatial extension.
In the baseline L1B SLC processor, the variance is computed at a tile level.

It writes:

.. math::
   nv\triangleq\dfrac{\left\langle\left(m-\left\langle m\right\rangle\right)^2\right\rangle}{\left\langle m\right\rangle^2}

where :math:`m=\left|\widetilde{DN}\right|^2` and :math:`\widetilde{DN}` is defined in equation :eq:`DNmod`