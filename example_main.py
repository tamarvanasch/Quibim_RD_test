# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 13:40:26 2021

@author: Tamar van Asch

Description: execution file
"""
# Import modules
import os
import dicomhandling as dh

# Set folder dir and image path
directory = r'C:\Users\s140390\Documents\Internship\Quibim_RD_test'
image = os.path.join(directory, 'dicom_images\IM-0001-0086-0001.dcm')

# %% Test Dicom Filter
sigma = 5
dcm_filter = dh.DcmFilter(image, sigma)

# %% Test Dicom Rotate
angle = 5
dcm_rotate = dh.DcmRotate(image, sigma)

# %% Test main function
dh.main(os.path.join(directory,'dicom_images'))
