import os
import numpy as np
import matplotlib.pyplot as plt
import Image
import spectroD as spD


print("Welcome to the python program where we will deduce an absorption spectrum ")
print("Please, place all the images in the right folder as indicated in the READ_ME file")
print(" if done, please enter '0' ..." )
input()

spc_folder = os.getcwd()
bkgnd = spD.avrgimgdir(spc_folder,'_background')
### uncomment if background average spectrum needed : 
#spD.specplot(bkgnd, 'background average spectrum')
lgt = spD.avrgimgdir(spc_folder,'_lightsource')
### uncomment if light-source average spectrum needed : 
#spD.specplot(lgt, 'light source average spectrum')
smpl = spD.avrgimgdir(spc_folder,'_sample')
### uncomment if light with sample average spectrum needed : 
#spD.specplot(smpl,' light spectrum with sample average sample' )

os.chdir(spc_folder)
absorption_spc = spD.subarrays(lgt,bkgnd,smpl)
spD.specplot(absorption_spc,' Absorption Spectrum ')

