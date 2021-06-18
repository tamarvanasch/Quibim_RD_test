# -*- coding: utf-8 -*-
"""
Date: Jun 17, 2021
@author: Tamar van Asch

Description: The main purpose of this module is to obtain the residue of a 
voxelwise subtraction operation applied to two input images, unfiltered and 
filtered. The module reads the DICOM files present in a specified folder. The
number of images in the folder should be exactly 2 and the images should have
different Image Position Patient (ipp) coordinates. The residues will be saved
in a separate folder. 

"""

import pydicom
import numpy as np
import os
import glob
import sys
import cv2

from scipy.ndimage.filters import gaussian_filter

class DcmFilter:
    """DcmFilter is able to read and store a DICOM file's pixel data as a NumPy array.
    A Gaussian 2D filter can be applied to smooth the image with a default sigma 
    of 3. The image position patient tag in DICOM file can be read and stored. """
    
    def __init__(self, path, sigma=3):
         
         # Read DICOM file
         dcm_file = pydicom.read_file(path)
         
         # Assign properties
         self.original = dcm_file.pixel_array
         self.filtered = gaussian_filter(self.original, sigma)
         self.ipp = [np.float(i) for i in list(dcm_file.ImagePositionPatient)]
     
        
class DcmRotate:
    """DcmRotate is able to read and store a DICOM file's pixel data as a NumPy array.
    The image can be rotated with multiples of 90 degrees, default of 180. The 
    image position patient tag in DICOM file can be read and stored."""  
    
    def __init__(self, path, angle=90):
                 
         # Read DICOM file
         dcm_file = pydicom.read_file(path)
         
         # Assign properties
         self.original = dcm_file.pixel_array
         self.rotated = np.rot90(self.original, int(angle/90))
         self.ipp = [np.float(i) for i in list(dcm_file.ImagePositionPatient)]


def check_ipp(dcm_1, dcm_2):
    """Check if the image position of the patient is the same for two given objects."""
   
    same_ipp = dcm_1.ipp == dcm_2.ipp
    return same_ipp

class IncorrectNumberOfImages(Exception):
    
    def __init__(self, message = 'Incorrect number of images. Aborting.'):
        
        # Set message
        self.message = message
        
        # Override constructor of Exception class
        super().__init__(self.message)
        
class SameImagePositionPatient(Exception):
    
    def __init__(self, message = 'The DICOM files appear to be the same. Aborting.'):
        
        # Set message
        self.message = message
        
        # Override constructor of Exception class
        super().__init__(self.message)
    
def main(input_folder):
    """ The main function of the module saves two residual images that are
    created by the subtraction of two different DICOM images. """
    
    # Read files in input folder
    dcm_files = glob.glob(os.path.join(input_folder,'*.dcm'))
    
    # Check if nr. of images is exactly 2
    if len(dcm_files) != 2:
        raise IncorrectNumberOfImages
    
    # Read DICOM files
    dcm_list = list()
    for file in dcm_files:
        dcm_filter = DcmFilter(file)
        dcm_list.append(dcm_filter)
    
    # Check if the ipps are different
    if check_ipp(dcm_list[0], dcm_list[1]):
        raise SameImagePositionPatient
        
    # Obtain residu images
    unfiltered_res = np.subtract(dcm_list[0].original,dcm_list[1].original)
    filtered_res = np.subtract(dcm_list[0].filtered,dcm_list[1].filtered)
    
    # Make residues folder if it does not exist
    res_dir = os.path.join(input_folder,'residues')
    if not os.path.exists(res_dir):
        os.mkdir(res_dir)
        
    # Save images in residual folder
    cv2.imwrite(os.path.join(res_dir,'unfiltered_residu.jpeg'), np.float64(unfiltered_res))
    cv2.imwrite(os.path.join(res_dir,'filtered_residu.jpeg'), np.float64(filtered_res))
    
if __name__ =="__main__":
    main(sys.argv[1])
