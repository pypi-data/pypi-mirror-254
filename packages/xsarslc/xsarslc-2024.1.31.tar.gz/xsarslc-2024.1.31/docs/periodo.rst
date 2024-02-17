.. _periodo:

===========================
Divide tiles into sub-tiles
===========================

The spectrum of the modulation signal over a full tile is noisy du to speckle contamination.
It also contains very low frequency signal which is not usefull to derive wave spectrum.
To reduce noise level and derive better wave modulation content, we use a Welsh-like methodology.
Each tile is divived into (overlapping) sub-tiles with parametrized size (typically 1.8 km x 1.8 km).
Doppler cendroids and look cross-periodogram derived in each sub-tile are then averaged to increase signal-to-noise ratio.