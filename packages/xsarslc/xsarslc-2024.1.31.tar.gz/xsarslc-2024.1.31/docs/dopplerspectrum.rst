.. _dopplerspectrum:

=========================================
Computation of azimuthal Doppler centroid
=========================================

Lets call :math:`rg` and :math:`az` as respectively the range and azimuth spatial vectors associated with the selected image.
:math:`rg = \text{sample}\times d_{rg}` and :math:`az = \text{line}\times d_{az}` where :math:`d_{rg}` and :math:`d_{az}` are respectively the sample and line spacing in meters.
The azimuthal Doppler spectrum writes:

.. math::
  :label: dop

    D(rg,f_{az}) = \left|\int \widetilde{DN}(rg,az) e^{-i2\pi f_{az}az} d_{az}\right|^2


The azimuthal Doppler centroid is the mean azimuth frequency of the azimuthal Doppler spectrum. In order to get a good estimation of the Doppler centroid, the average of the Doppler spectrum is computed on the range direction:

.. math::
    \overline{D}(f_{az}) = \left\langle D(rg,f_{az})\right\rangle_{rg}


+-------------------------------------------------------------------------------------------+
|                                                                                           |
| .. math::                                                                                 |
|     :label: some_descriptive_label                                                        |
|                                                                                           |
|     \textbf{Azimuthal Doppler spectrum}                                                   |
|                                                                                           |
|                                                                                           |
+===========================================================================================+
| .. image:: ./figures/S1_azimuth_IR_IW_VV.png                                              |
|  :alt: Azimuthal Doppler spectrum                                                         |
|  :scale: 50 %                                                                             |
|  :name: S1_azimuth_IR_IW_VV_1                                                             |
|  :target: _`dopplerspectrum`                                                              |
|  :align: center                                                                           |
|                                                                                           |
| figure :eq:`some_descriptive_label`:Example of Doppler spectrum.                          |
+-------------------------------------------------------------------------------------------+



The azimuthal Doppler centroid is, by definition, the mean (first order moment) of the Doppler spectrum, namely:

.. math::
  :label: centroid

    DC \triangleq \dfrac{\int f_{az} \overline{D}(f_{az}) df_{az}}{\int\overline{D}(f_{az}) df_{az}}

However, since the azimuthal Doppler spectrum is not symmetric due to windowing processing applied during the generation
of the L1 SLC the estimation of the DC using equation :eq:`centroid` is biased.
In practise, the DC is computed by fitting a Gaussian curve on the Doppler spectrum to find the position of the maximum.

.. note::
   This should be updated in the future.

=======================================================
Computation of centered and normalized Doppler spectrum
=======================================================


The that the Doppler spectrum is not centered around zero nor symmetric relatively to its maximum.
Several explanations can be given to explain this two characteristics.
The not centered value of the azimuthal centroid can be due, among others, to some geophysical aspects such as the observed scene mean motion but also on some instrument uncorrected geometry and uncompensated antenna properties.

The disymmetric shape can also be due to some uncompensated instrument effect but also on applied signal processing such as windowing or interpolation.

In order to correctly further process the Doppler spectrum, it is mandatory to compensate as much as possible these effects with a two step processing:

1. centering the Doppler spectrum
2. Normalize the Doppler spectrum by the Impulse Response of the instrument


Centering the Doppler spectrum
++++++++++++++++++++++++++++++

Centering the Doppler spectrum and computing the 2D Fourier Transform of the complex modulation signal writes:

.. math::
    :label: centereddop

    FT^{2D}\left[\widetilde{DN}_c\right] = \int \widetilde{DN}(rg,az)e^{-i2\pi\ DC\ az} e^{-i2\pi (f_{az}az+f_{rg}rg} d_{az}d_{rg}


===============================================================================
Normalization of the Doppler spectrum by the Impulse Response of the instrument
===============================================================================


These Impulse Responses have been computed over homogeneous and motion-less surfaces, averaged and stored.
The dataset used to compute theses response is available here and the numerical code to produce them refers to :py:mod:`xsarslc.processing.impulseResponse.compute_IR` .

The normalization of the doppler spectrum is performed by :py:mod:`xsarslc.processing.intraburst.compute_looks` method.


+-------------------------------------------------------------------------------------------+
|                                                                                           |
| .. math::                                                                                 |
|     :label: S1_range_IR_IW_VV                                                             |
|                                                                                           |
|     \textbf{Range Doppler spectrum IW VV}                                                 |
|                                                                                           |
|                                                                                           |
+===========================================================================================+
| .. image:: ./figures/S1_range_IR_IW_VV.png                                                |
|  :scale: 50 %                                                                             |
|  :name: S1_range_IR_IW_VV                                                                 |
|  :align: center                                                                           |
|                                                                                           |
| figure :eq:`S1_range_IR_IW_VV` :Example of Doppler spectrum along range.                  |
+-------------------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------------------+
|                                                                                           |
| .. math::                                                                                 |
|     :label: S1_azimuth_IR_WV_VV                                                           |
|                                                                                           |
|     \textbf{Azimuth Doppler spectrum WV VV}                                               |
|                                                                                           |
|                                                                                           |
+===========================================================================================+
| .. image:: ./figures/S1_azimuth_IR_WV_VV.png                                              |
|  :scale: 90 %                                                                             |
|  :name: S1_azimuth_IR_WV_VV                                                               |
|  :align: center                                                                           |
|                                                                                           |
| figure :eq:`S1_azimuth_IR_WV_VV` :Example of Doppler spectrum along azimuth.              |
+-------------------------------------------------------------------------------------------+


+-------------------------------------------------------------------------------------------+
|                                                                                           |
| .. math::                                                                                 |
|     :label: S1_range_IR_WV_VV                                                             |
|                                                                                           |
|     \textbf{Range Doppler spectrum WV VV}                                                 |
|                                                                                           |
|                                                                                           |
+===========================================================================================+
| .. image:: ./figures/S1_range_IR_WV_VV.png                                                |
|  :scale: 90 %                                                                             |
|  :name: S1_range_IR_WV_VV                                                                 |
|  :align: center                                                                           |
|                                                                                           |
| figure :eq:`S1_range_IR_WV_VV` :Example of Doppler spectrum along range.                  |
+-------------------------------------------------------------------------------------------+


The normalization with the instrument Impulse Response is realized in the Fourier domain and writes:

.. math::
   FT^{2D}\left[\widetilde{\underline{DN_c}}\right](f_{rg},f_{az}) = \dfrac{FT^{2D}[\widetilde{DN}_c]}{\sqrt{IR_{rg}(f_{rg})}\sqrt{IR_{az}(f_{az})}}

with :math:`IR_{rg}` and :math:`IR_{az}` being the Impulse Response in range and azimuth direction for the considered acquisition mode.

.. note::
   in `xsarslc` library the methods to estimate the Impulse Response are :py:func:`xsarslc.processing.impulseResponse.compute_IWS_subswath_Impulse_Response` and :py:func:`xsarslc.processing.impulseResponse.compute_WV_Impulse_Response`
