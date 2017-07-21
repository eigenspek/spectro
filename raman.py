import os
import numpy as np 
import Image
import matplotlib.pyplot as plt
import spectroD as spD

print(" please, create a subfolder in the images-source folder and put your images in")
print(" if done, please enter '0' ..." )
input()

newfolder = input("please enter the name of your folder in beetween '' : ")

spc_folder = os.getcwd()

smpl = spD.avrgimgdir(spc_folder,newfolder)
spD.specplot(smpl , 'Raman Spectrum')

a = spD.maxarray(smpl)
print( 'maximum peak found at : ', a)

b = spD.ptclenergy(smpl,a[0])
spD.specplot(b,'in_situ particles energy')


