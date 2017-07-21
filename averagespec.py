import os
import numpy as np
import matplotlib.pyplot as plt
import Image
import spectroD as spD

print(" Here you can get an average spectrum over different images ")
print(" please, create a subfolder in the images-source folder and put your images in")
print(" if done, please enter '0' ..." )
input()
newfolder = input("please enter the name of your folder in beetween '' : ")
spc_folder = os.getcwd()
smpl = spD.avrgimgdir(spc_folder,newfolder)
spD.specplot(smpl,'Average Spectrum' )
