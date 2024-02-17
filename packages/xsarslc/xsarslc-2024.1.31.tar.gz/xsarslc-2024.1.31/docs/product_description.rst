.. _productdescription:

****************************************
Level-1B SAR IFREMER Product Description
****************************************

This page stands as a Product Description document for Sentinel-1 L1B IFREMER product.

It describes the format, the files and the content of Level-1B SAR product.

Product philosophy
##################


The Level-1B Sentinel-1 IFREMER product is designed to be a SAR expert product. The rationales behind the dimensions and coordinates that are showing the tiling of the SAR image in slice / sub-swath / burst / tiles are:

    The willing to stay close to image geometry to be able to easily swap from image domain to geo-referenced spectral domain

    The willing to stay close to ESA Sentinel-1 SLC product format.

The limited number of variables (only geometry, radar and radar-derived variables) is also a strategy to limit the volume of the products and keep simple the first L1 -> L1B processing which is also the most greedy processing in terms of processing-time and memory-usage.

L1B Level-1B Sentinel-1 IFREMER product has been designed to ease the work on the inversion from cross-spectrum coming from intra-burst and inter-burst (overlapping) part of the SLC products.

The current version of the product is still prototype, and future evolution are expected depending on feedbacks from partners. The configurations of the tiles, periodograms, looks is tuneable and furthers tests will help to choose the proper set of parameters for wind and wave applications.

Product structure
#################

Each product is stored in a .SAFE directory. The SAFE convention is inherited from Sentinel-1 mission. Except that the SLC (single look complex) acronym has been replaced by XSP (for cross-spectrum which is the most important variable in this dataset).

.. image:: ./figures/L1_naming_conventions.png
   :width: 650px
   :height: 500px
   :scale: 110 %
   :alt: safe-naming
   :align: center



Each .SAFE directory contains 3 or 6 netCDF files, one per polarization (could be single polarization HH/VV or dual polarization HH/HV - VV/VH) plus one per sub-swath, following the storage of official ESA SLC products. All the polarizations are processed from Level-1 to Level-1B even though VV is the classical candidate polarization for wave inversion.


The netCDF files naming convention is adapted from ESA Sentinel-1:


.. image:: ./figures/Sentinel-1-SAR-User-Guide-Product-Formatting-Figure-2.jpg
   :width: 800px
   :height: 400px
   :scale: 90 %
   :alt: file-naming
   :align: center


Example of L1B filename:

s1a-iw1-slc-hv-20220309t083923-20220309t083948-042242-0508e1-004_L1B_xspec_IFR_1.4k.nc

Extra part gives the processing level, IFR stands for IFREMER and "1.4k" is the ID of the processing.

Typical size for a IW SLC processed at 17.7 km² tile width is about 75 Mo per L1B .nc file .

Product variables
#################


Exhaustive content
------------------

Each netCDF files is split into 2 groups:

     - **intraburst**: region (i.e. SAR time span) of SLC bursts in which Ocean/Land surface have been seen only one time.

     - **interburst**: region (i.e. SAR time span) of SLC bursts for which the Ocean/Land surface have been observed twice thanks to antenna steering in azimuth.

Each of the group contains the same set of variables with minor exceptions*.

The variables of **intraburst** group:

.. raw:: html

 <details>
 <summary><a>exhaustive list of the variables available in Level-1B SAR IFREMER</a></summary>

.. code-block:: python

 float incidence(burst, tile_line, tile_sample) ;

          incidence:_FillValue = NaNf ;

          incidence:long_name = "incidence at tile middle" ;

          incidence:units = "degree" ;

          incidence:coordinates = "pol line longitude latitude sample" ;

      string pol ;

      short burst(burst) ;

      float normalized_variance(burst, tile_line, tile_sample) ;

          normalized_variance:_FillValue = NaNf ;

          normalized_variance:long_name = "normalized variance" ;

          normalized_variance:units = "" ;

          normalized_variance:coordinates = "pol line longitude latitude sample" ;

      float sigma0(burst, tile_line, tile_sample) ;

          sigma0:_FillValue = NaNf ;

          sigma0:long_name = "calibrated sigma0" ;

          sigma0:units = "linear" ;

          sigma0:coordinates = "pol line longitude latitude sample" ;

      float ground_heading(burst, tile_line, tile_sample) ;

          ground_heading:_FillValue = NaNf ;

          ground_heading:long_name = "ground heading" ;

          ground_heading:units = "degree" ;

          ground_heading:convention = "from North clockwise" ;

          ground_heading:coordinates = "pol line longitude latitude sample" ;

      float doppler_centroid(burst, tile_line, tile_sample) ;

          doppler_centroid:_FillValue = NaNf ;

          doppler_centroid:long_name = "Doppler centroid" ;

          doppler_centroid:units = "rad/m" ;

          doppler_centroid:coordinates = "pol line longitude latitude sample" ;

      float k_rg(burst, tile_sample, freq_sample) ;

          k_rg:_FillValue = NaNf ;

          k_rg:long_name = "wavenumber in range direction" ;

          k_rg:units = "rad/m" ;

      float k_az(freq_line) ;

          k_az:_FillValue = NaNf ;

          k_az:long_name = "wavenumber in azimuth direction" ;

          k_az:units = "rad/m" ;

      float var_xspectra_0tau(burst, tile_line, tile_sample, freq_line, freq_sample, \0tau) ;

          var_xspectra_0tau:_FillValue = NaNf ;

          var_xspectra_0tau:coordinates = "pol k_az k_rg line longitude latitude sample" ;

      float var_xspectra_1tau(burst, tile_line, tile_sample, freq_line, freq_sample, \1tau) ;

          var_xspectra_1tau:_FillValue = NaNf ;

          var_xspectra_1tau:coordinates = "pol k_az k_rg line longitude latitude sample" ;

      float var_xspectra_2tau(burst, tile_line, tile_sample, freq_line, freq_sample, \2tau) ;

          var_xspectra_2tau:_FillValue = NaNf ;

          var_xspectra_2tau:coordinates = "pol k_az k_rg line longitude latitude sample" ;

      float tau(burst, tile_line, tile_sample) ;

          tau:_FillValue = NaNf ;

          tau:long_name = "delay between two successive looks" ;

          tau:units = "s" ;

          tau:coordinates = "pol line longitude latitude sample" ;

      float azimuth_cutoff(burst, tile_line, tile_sample) ;

          azimuth_cutoff:units = "m" ;

          azimuth_cutoff:coordinates = "pol line longitude latitude sample" ;

          azimuth_cutoff:_FillValue = NaNf ;

          azimuth_cutoff:long_name = "Azimuthal cut-off (2tau)" ;

      short line(burst, tile_line) ;

      short sample(burst, tile_sample) ;

      float corner_longitude(burst, tile_line, tile_sample, c_sample, c_line) ;

          corner_longitude:_FillValue = NaNf ;

          corner_longitude:history = "longitude:\n  annotation/s1a.xml:\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/line\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/pixel\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/longitude\n" ;

          corner_longitude:definition = "Geodetic longitude of grid point [degrees]." ;

          corner_longitude:coordinates = "pol line longitude latitude sample" ;

      float corner_latitude(burst, tile_line, tile_sample, c_sample, c_line) ;

          corner_latitude:_FillValue = NaNf ;

          corner_latitude:history = "latitude:\n  annotation/s1a.xml:\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/line\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/pixel\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/latitude\n" ;

          corner_latitude:definition = "Geodetic latitude of grid point [degrees]." ;

          corner_latitude:coordinates = "pol line longitude latitude sample" ;

      short corner_line(burst, tile_line, c_line) ;

          corner_line:long_name = "line number in original digital number matrix" ;

          corner_line:coordinates = "line pol" ;

      short corner_sample(burst, tile_sample, c_sample) ;

          corner_sample:long_name = "sample number in original digital number matrix" ;

          corner_sample:coordinates = "pol sample" ;

      float longitude(burst, tile_line, tile_sample) ;

          longitude:_FillValue = NaNf ;

          longitude:history = "longitude:\n  annotation/s1a.xml:\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/line\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/pixel\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/longitude\n" ;

          longitude:definition = "Geodetic longitude of grid point [degrees]." ;

      float latitude(burst, tile_line, tile_sample) ;

          latitude:_FillValue = NaNf ;

          latitude:definition = "Geodetic latitude of grid point [degrees]." ;

          latitude:history = "latitude:\n  annotation/s1a.xml:\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/line\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/pixel\n  - /product/geolocationGrid/geolocationGridPointList/geolocationGridPoint/latitude\n" ;

      byte land_flag(burst, tile_line, tile_sample) ;

          land_flag:long_name = "land flag" ;

          land_flag:convention = "True if land is present" ;

          land_flag:dtype = "bool" ;

          land_flag:coordinates = "pol line longitude latitude sample" ;

      float burst_corner_longitude(burst, c_sample, c_line) ;

          burst_corner_longitude:_FillValue = NaNf ;

          burst_corner_longitude:long_name = "corner longitude of burst valid portion" ;

          burst_corner_longitude:coordinates = "pol" ;

      float burst_corner_latitude(burst, c_sample, c_line) ;

          burst_corner_latitude:_FillValue = NaNf ;

          burst_corner_latitude:long_name = "corner latitude of burst valid portion" ;

          burst_corner_latitude:coordinates = "pol" ;

      float xspectra_0tau_Re(burst, tile_line, tile_sample, freq_line, freq_sample, \0tau) ;

          xspectra_0tau_Re:long_name = "sub-looks cross-spectra 0 tau apart" ;

          xspectra_0tau_Re:_FillValue = NaNf ;

          xspectra_0tau_Re:look_window = "None" ;

          xspectra_0tau_Re:look_overlap = 0. ;

          xspectra_0tau_Re:look_width = 0.2 ;

          xspectra_0tau_Re:coordinates = "pol k_az k_rg line longitude latitude sample" ;

          xspectra_0tau_Re:nlooks = 3LL ;

      float xspectra_0tau_Im(burst, tile_line, tile_sample, freq_line, freq_sample, \0tau) ;

          xspectra_0tau_Im:long_name = "sub-looks cross-spectra 0 tau apart" ;

          xspectra_0tau_Im:_FillValue = NaNf ;

          xspectra_0tau_Im:look_window = "None" ;

          xspectra_0tau_Im:look_overlap = 0. ;

          xspectra_0tau_Im:look_width = 0.2 ;

          xspectra_0tau_Im:coordinates = "pol k_az k_rg line longitude latitude sample" ;

          xspectra_0tau_Im:nlooks = 3LL ;

      float xspectra_1tau_Re(burst, tile_line, tile_sample, freq_line, freq_sample, \1tau) ;

          xspectra_1tau_Re:long_name = "sub-looks cross-spectra 1 tau apart" ;

          xspectra_1tau_Re:_FillValue = NaNf ;

          xspectra_1tau_Re:look_window = "None" ;

          xspectra_1tau_Re:look_overlap = 0. ;

          xspectra_1tau_Re:look_width = 0.2 ;

          xspectra_1tau_Re:coordinates = "pol k_az k_rg line longitude latitude sample" ;

          xspectra_1tau_Re:nlooks = 3LL ;

      float xspectra_1tau_Im(burst, tile_line, tile_sample, freq_line, freq_sample, \1tau) ;

          xspectra_1tau_Im:long_name = "sub-looks cross-spectra 1 tau apart" ;

          xspectra_1tau_Im:_FillValue = NaNf ;

          xspectra_1tau_Im:look_window = "None" ;

          xspectra_1tau_Im:look_overlap = 0. ;

          xspectra_1tau_Im:look_width = 0.2 ;

          xspectra_1tau_Im:coordinates = "pol k_az k_rg line longitude latitude sample" ;

          xspectra_1tau_Im:nlooks = 3LL ;

      float xspectra_2tau_Re(burst, tile_line, tile_sample, freq_line, freq_sample, \2tau) ;

          xspectra_2tau_Re:long_name = "sub-looks cross-spectra 2 tau apart" ;

          xspectra_2tau_Re:_FillValue = NaNf ;

          xspectra_2tau_Re:look_window = "None" ;

          xspectra_2tau_Re:look_overlap = 0. ;

          xspectra_2tau_Re:look_width = 0.2 ;

          xspectra_2tau_Re:coordinates = "pol k_az k_rg line longitude latitude sample" ;

          xspectra_2tau_Re:nlooks = 3LL ;

      float xspectra_2tau_Im(burst, tile_line, tile_sample, freq_line, freq_sample, \2tau) ;

          xspectra_2tau_Im:long_name = "sub-looks cross-spectra 2 tau apart" ;

          xspectra_2tau_Im:_FillValue = NaNf ;

          xspectra_2tau_Im:look_window = "None" ;

          xspectra_2tau_Im:look_overlap = 0. ;

          xspectra_2tau_Im:look_width = 0.2 ;

          xspectra_2tau_Im:coordinates = "pol k_az k_rg line longitude latitude sample" ;

          xspectra_2tau_Im:nlooks = 3LL ;

.. raw:: html
 </details>

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: extra explanations

   examples/L1B_Sentinel1_variables_explanation

Explanation on specific variables
---------------------------------

This section gives illustrated details on some of the variables:

    * :doc:`examples/L1B_Sentinel1_variables_explanation`


Product attributes
##################

.. code-block::


 // group attributes:
 :name = "SENTINEL1_DS:/home/datawork-cersat-public/project/mpc-sentinel1/data/esa/sentinel-1a/L1/IW/S1A_IW_SLC__1S/2018/065/S1A_IW_SLC__1SDV_20180306T230337_20180306T230405_020901_023DBA_73A0.SAFE:IW1" ;

                :short_name = "SENTINEL1_DS:S1A_IW_SLC__1SDV_20180306T230337_20180306T230405_020901_023DBA_73A0.SAFE:IW1" ;

                :product = "SLC" ;

                :safe = "S1A_IW_SLC__1SDV_20180306T230337_20180306T230405_020901_023DBA_73A0.SAFE" ;

                :swath = "IW" ;

                :multidataset = "False" ;

                :ipf = 2.84 ;

                :platform = "SENTINEL-1A" ;

                :pols = "VV VH" ;

                :start_date = "2018-03-06 23:03:38.051625" ;

                :stop_date = "2018-03-06 23:04:03.182857" ;

                :footprint = "POLYGON ((-76.08430839864033 26.63756326996933, -75.18793064940225 26.79052036139598, -75.50267764839376 28.28730160398311, -76.41199086776611 28.13488378485153, -76.08430839864033 26.63756326996933))" ;

                :coverage = "169km * 90km (line * sample )" ;

                :orbit_pass = "Ascending" ;

                :platform_heading = -12.5313253576975 ;

                :comment = "denoised digital number, read at full resolution" ;

                :history = "digital_number: measurement/s1a-iw1-slc-v*-20180306t230338-20180306t230403-020901-023dba-00*.tiff\n" ;

                :radar_frequency = 5405000454.33435 ;

                :azimuth_time_interval = 0.0020555563 ;

                :tile_width_sample = 17700LL ;

                :tile_width_line = 17700LL ;

                :tile_overlap_sample = 0LL ;

                :tile_overlap_line = 0LL ;

                :periodo_width_sample = 3540LL ;

                :periodo_width_line = 3540LL ;

                :periodo_overlap_sample = 1770LL ;

                :periodo_overlap_line = 1770LL ;



Product access
##############

Currently the L1B SAR Sentinel-1 product is disseminated from this URL:

https://cerweb.ifremer.fr/datarmor/sarwave/diffusion/sar/iw/slc/l1b/experimental_product_collection/


Acknowledgment
##############

The Sentinel-1 Level-1B SAR IFREMER Product has been co-funded by ESA through the SARWAVE project (https://www.sarwave.org/).
The processor development benefits from support and contribution from/to Sentinel-1 Mission Performance Cluster (https://sar-mpc.eu/about/activities-and-team/).
