.. _bright-target:

******************************
Bright-Target mask computation
******************************

Bright target on SAR images are manifestations of extreme return due to target with significantly higher back-scattered signal (boats, wind turbines, ...) compared to background.
Bright target strongly affect most of significant radar quantities computation such as cross-section, normalized variance or image cross-spectrum evaluation.
To derive significant estimation of these radar parameters (from a sea-state estimation perspective), these bright targets must be, as much as possible, removed from
the original data before applying conventional algorithms. To this purpose, we will rely on the Cell-Averaging CFAR (Constant False Alarm Rate) algorithm to identify
the bright target location. The CFAR method spots (Cell-averaging) bright targets having significantly different signal statistical characteristics compared to the surounding (clutter) cells. A guard distance (guard cells) from the target location ensures to keep bright target spatial contamination from the reference clutter (training cells).

The CA-CFAR algorithm is applied on the absolute value of Digital Numbers :math:`|\widetilde{DN}|`.

The bright target mask is computed as follow:

1. define a target typical size [m] and corresponding number of pixels
2. define a guard size [m] (:math:`g_{rg}, g_{az}`) and corresponding number of pixels
3. define a clutter size [m] (:math:`c_{rg}, c_{az}`) and corresponding number of pixels
4. Convolve original data by a uniform kernel having target typical sizes. Resulting data writes :math:`\langle t \rangle`

4. Define a cluster kernel based on the aforementioned guard and clutter sizes.

The convolving kernel writes:

.. math::
   \begin{equation}
   K(rg,az)=\left\{{
   \begin{array}{l}
   1\quad \text{if}\ \left(\dfrac{rg}{g_{rg}}\right)^2 + \left(\dfrac{az}{g_{az}}\right)^2>\dfrac{1}{2^2}\quad \text{and}\quad \left(\dfrac{rg}{c_{rg}}\right)^2 + \left(\dfrac{az}{c_{az}}\right)^2<\dfrac{1}{2^2}\\
   0\quad \text{else}
   \end{array}
   }\right.
   \end{equation}

where :math:`g_{rg}, g_{az}, c_{rg}, c_{az}` respectively stands for guard sizes and clutter sizes in range and azimuth direction.

5. Convolving the original (respectively abs-squared) data with this kernel provide reference clutter mean :math:`\langle c \rangle` and variance :math:`\langle(c-\langle c \rangle)^2\rangle` per pixel.
6. Difference of target mean and reference mean normalized by square root of reference standard deviation gives a relative normalized ratio :math:`r_T` that is to compare with a fixed treshold :math:`BT_{treshold}`.

.. math::
   \begin{equation}
   r_T = \dfrac{\langle c \rangle-\langle t \rangle}{\sqrt{\langle(c-\langle c \rangle)^2\rangle}}
   \end{equation}

7. Bright target mask is defined as follow

.. math::
   \begin{equation}
   BT_{mask}=\left\{{
   \begin{array}{l}
   \text{True if}\ r>BT_{treshold}\\
   \text{False if}\ r<BT_{treshold}
   \end{array}
   }\right.
   \end{equation}

8. Original data is masked with the resulting :math:`BT_{mask}` and steps 5 to 7 is then recursively applied. The recursive operation progressively remove targets that could have been missed in previous iteration du to spatial contamination of another close target.

9. An optional additional procedure called neighbor filtering can be applied after step 7. Synthetic Aperture Radar azimuthal compression makes bright targets signature to span over a larger distante than the actual size of the bright target. As a consequence,
it is common to have spread brigh points around a stronger bright target.
To remove such points, bright target mask derived in step 7 is dilated (binary dilation) and relative ratio :math:`r_T` of points in the dilation radius are tested against a neighboor treshold :math:`BT'_{treshold}` smaller than :math:`BT_{treshold}`. Bright target mask is dilated for dilated pixels where :math:`r_T>BT'_{treshold}`.

Typical values for parameters listed in this procedure are: :math:`(t_{rg}, t_{az})=(5 m,5 m), (g_{rg}, g_{az})=(350 m,350 m), (c_{rg}, c_{az})=(1 km,1 km), BT_{treshold}=10, BT'_{treshold}=5`.

Illustration of the algorithm

Before:

.. image:: ./figures/before_bt.png
  :alt: Bright Target signature
  :scale: 100 %
  :align: center

After:

.. image:: ./figures/after_bt.png
  :alt: Bright Target after correction
  :scale: 100 %
  :align: center