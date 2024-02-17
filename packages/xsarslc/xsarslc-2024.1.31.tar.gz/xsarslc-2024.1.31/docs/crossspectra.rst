.. _crossspectra:

=======================================================
Computation of look cross-spectra (WV and IW products)
=======================================================


Extraction of azimuthal looks
#############################

The extraction of azimuthal looks is computed as follow:

1. Taking the Inverse Fourier Transform of :math:`FT^{2D}\left[\widetilde{\underline{DN_c}}\right]` in the range direction.
2. Slicing the returned azimuthal Doppler bandwidth into :math:`n` portions.
3. Taking the Inverse Fourier Transform of each portion in the azimuthal direction.
4. Normalizing each look energy. (if necessary)
5. Detect the look

They are evaluated as follow:

.. math::
   FT^{1D}\left[\widetilde{\underline{DN_c}}\right](rg,f_{az}) = \dfrac{1}{2\pi}\int FT^{2D}\left[\widetilde{\underline{DN_c}}\right] e^{i2\pi f_{rg}rg} df_{rg}

The second and third step corresponding to the extraction of look :math:`i` writes:

.. math::
    \widetilde{\underline{DN_c}}^i(rg,az) = \dfrac{1}{2\pi}\int FT^{1D}\left[\widetilde{\underline{DN_c}}\right](rg,f_{az})W_i(f_{az}) e^{i2\pi f_{az}az} df_{az}

where :math:`W_i` is the weighting function corresponding to slice :math:`i` in the azimuthal spectrum.

Figure \ref{} shows :math:`\left|FT^{1D}\left[\widetilde{\underline{DN_c}}\right](rg,f_{az})\right|^2` averaged over the range direction and the weighting function of a look.

Detecting look :math:`i` and normalizing its energy finally writes:

.. math::
   look^i(rg,az)=\dfrac{\left|\widetilde{\underline{DN_c}}^i\right|^2}{\sum_{rg,az}{\left|\widetilde{\underline{DN_c}}^i\right|^2}}


In practice, the width of the slicing function :math:`W_i` is defined relatively to the total frequency range of the azimuthal Doppler spectrum.
The baseline processing relies on a division into 3 looks and each look contains 25\% of the total Doppler frequency range.
The remaining 25\% are located at the two borders of the frequency axis (12.5\% on each side).


Looks cross-spectra
###################

Cross-spectra between look :math:`i` and look :math:`i+n` writes:

.. math::
    XS^{n\tau}(f_{rg},f_{az})=FT^{2D}[look^i]\cdot FT^{2D}[look^{i+n}]^\star


where the :math:`\star` symbol stands for the complex conjugate and where the definition of the 2D Fourier Transform :math:`FT^{2D}` is

.. math::
   F(f_{rg},f_{az}) \triangleq FT^{2D}[f(rg,az)] = \iint f(rg,az) e^{-i2\pi(f_{az}az+f_{rg}rg)} d_{az}\ d_{rg}


The time separation '':math:`\tau`'' between two consecutive looks writes:

.. math::
   \tau = SaD\times look_{sep}

where :math:`SaD` and :math:`look_{sep}` are respectively the Synthetic aperture Duration [second] and the look separation.

They writes:

.. math::

   SaD = \dfrac{c\times s}{2f_{r}V_{sat} \Delta_{az}}\\
   look_{sep} = look_{width}\times(1-look_{overlap})


with :math:`c`, :math:`s`, :math:`f_r`, :math:`V_{sat}`, :math:`\Delta_{az}` being respectively the speed of light, the slant range distance, the radar frequency, the satellite ground velocity and the azimuth spacing.
In the baseline processing, :math:`look_{width}=0.2` for IW, :math:`look_{width}=0.25` for WV and :math:`look_{overlap}=0`.



