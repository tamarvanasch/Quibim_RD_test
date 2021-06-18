# Quibim_RD_test
Dicomhandling module designed for filtering and rotation of dicom images. 

The main purpose of this module is to obtain the residue of a voxelwise subtraction operation applied to two input images, unfiltered and filtered. The module reads the DICOM files present in a specified folder. The number of images in the folder should be exactly 2 and the images should have different Image Position Patient (ipp) coordinates. The residues will be saved in a separate folder. 
