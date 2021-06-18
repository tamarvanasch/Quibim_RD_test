# Quibim_RD_test
The main purpose of this module is to obtain the residue of a voxelwise subtraction operation applied to two input images, unfiltered and filtered. The module reads the DICOM files present in a specified folder. The number of images in the folder should be exactly 2 and the images should have different Image Position Patient (ipp) coordinates. The residues will be saved in a separate folder. Additionally the module can be used to filter and rotate dicom images. 

# Files
- dicomhandling.py : is the main module that can be loaded into a python script or used in the command prompt to execute its main function.
- example_main.py : is an example script that loads the dicomhandling module and tests its functions
- dicom_images : is the folder that contains two dicom images, the folder directory can be used as input for the main function of dicomhandling

# Dependencies
The required packages are:
- pydicom
- numpy
- os
- glob
- sys
- OpenCV

