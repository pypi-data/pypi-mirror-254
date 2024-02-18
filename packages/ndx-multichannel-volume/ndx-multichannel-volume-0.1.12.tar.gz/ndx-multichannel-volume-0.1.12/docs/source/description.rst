Overview
========

.. note::
    This extension is to add support for volumetric multichannel images. This 
    extends existing NWB functions for optophysiology imaging to allow for 
    3 dimensions and a flexible number of channels. There is additional support
    for adding metadata that is necessary for imaging in C. Elegans. 

    New classes added in this extension are:

    CElegansSubject - extension of the base subject class with additional attributes
    for metadata specific to C. Elegans.

    MultiChannelVolumeSeries - extension of the base TimeSeries class to support 
    multiple channels and 3 dimensions.

    MultiChannelVolume - class for storing mutlichannel volumetric images with 
    a flexible number of channels. 

    ImagingVolume - alternate version of the native ImagingPlane class for supporting
    metadata associated with volumetric multichannel images. Contains a list of optical
    channel references as well as an ordered list of how those channels index to the 
    channels in the image.

    OpticalChannelPlus - extension of the OpticalChannel class to support additional
    information including emission_range, excitation_range, and excitation_lambda.

    OpticalChannelReferences - contains ordered list of optical channel to represent the 
    order of the optical channels in the reference volume.

    VolumeSegmentation - contains segmentation masks for image volumes. There are options 
    to use either a standard voxel_mask with XYZ information as well as a Cell ID label,
    or color_voxel_mask which has RGBW information as well as XYZ.
