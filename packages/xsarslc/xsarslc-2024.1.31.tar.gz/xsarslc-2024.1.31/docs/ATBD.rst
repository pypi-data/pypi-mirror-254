.. _atbd:

***************************************************************
Algorithm Level-1 SLC to Level-1B XSP cross spectrum Sentinel-1
***************************************************************

This page stands as the A.T.B.D. (Algorithm Technical Baseline Document) for Sentinel-1 Level-1B product generated at IFREMER .

This ATBD describes the processing steps to transform Sentinel-1 SLC (Single Look Complex) product into a Level-1B XSP.

.. toctree::
   :maxdepth: 1
   :caption: Overview of the processing steps

   overview

Links to detailed processing step descriptions:

.. toctree::
   :maxdepth: 1
   :caption: Deramping of SLC signal: step 0.1

   deramping

.. toctree::
   :maxdepth: 1
   :caption: Computation of calibrated denoised sigma0: step 1 and 2

   sigma0

.. toctree::
   :maxdepth: 1
   :caption: Land detection: step 3

   landmask

.. toctree::
   :maxdepth: 1
   :caption: Bright target mitigation: step 4

   brighttarget

.. toctree::
   :maxdepth: 1
   :caption: Compute modulation (and Normalized Variance): step 6

   modulation

.. toctree::
   :maxdepth: 1
   :caption: Sub-tiling: step 7

   periodo

.. toctree::
   :maxdepth: 1
   :caption: Compute modulation: step 8 and 9

   dopplerspectrum

.. toctree::
   :maxdepth: 1
   :caption: Sub tile granularity operations: steps 10-11-12-13-14

   crossspectra

.. toctree::
   :maxdepth: 1
   :caption: Computation of the azimuthal cut-off

   cutoff


.. _`bright targets`: ATBD.rst#bright target
.. _`Impulse Response`: ATBD.rst#Impulse Response


Last documentation build: |today|