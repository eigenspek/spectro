import os 
import numpy as np
import Image as img
import matplotlib.pyplot as plt

""" SpectroD Module to convert an image to intensity Spectrum """

#### IMG2ARRAY : image to array  
def img2array(imgname, imglocation):
	""" return the array corresponding to non-integrated image, takes as arguments ('image_name','image_location') """
	os.chdir(imglocation)
	imageused = img.open(imgname).convert("L")
	imgtrsf = np.array(imageused)
	#compensation of rotation : 
	newimgtrsf = np.zeros((imgtrsf.shape[1],imgtrsf.shape[0]))
	i = 0
	j = 0	
	for i in range(imgtrsf.shape[0]) :
		for j in range(imgtrsf.shape[1]) : 
			newimgtrsf[j,i] = imgtrsf[i,j]
	return newimgtrsf

#### ARRAY2SPEC : array to intensity spectrum 
def array2spec(arrayused):
	""" gives the intensity spectrum as integrating pixels of the image over length. Uses as argument array2spec(image_array) where image_array is obtained from img2array. Return a 1 dimension array containing intensity over width. """
	intensity_array = np.zeros((arrayused.shape[0]))
	a = 0
	for a in range(arrayused.shape[0]):
		for b in range(arrayused.shape[1]):
			intensity_array[a] += arrayused[a,b]
	return intensity_array

#### SPECPLOT : plot intensity spectrum 
def specplot(ar,title = 'spectrum'):
	""" Plots the intensity spectrum of the image. takes in argument the array obtained from array2spec and a str for title """
	plt.plot(ar)
	plt.title(title)
	plt.xlabel('pixels')
	plt.ylabel('intensity')
	plt.show()

#### VERIFYARRAYS : verifies if all the arrays entered in *args are the same length
def verifyarrays(*args):
	""" This function returns a boolean, to verify if all arrays have the same length. Works with 1D arrays """
	length = len(args)
	i = 0 
	a = 0
	for i in range(length-1) :
		if len(args[i])==len(args[i+1]):
			print()
		else: 
			a = 1
	return a==0   # here is the boolean return

#### ADDARRAYS : add multiples 1D arrays together in one single array
def addarrays(*args):
	""" add multiples 1D arrays alltogether in one single array, used in the avrgarrays() function """
	lgt = len(args)
	if verifyarrays(args):
		a = np.zeros(len(args[0]))
		for i in range(lgt):
			a += args[i]
		return a

#### SUBARRAYS : Substracts all the arrays from the first array in the list
def subarrays(*args):
	""" Substracts arrays 2,3,4,... to the first array. """
	lgt = len(args)
	if verifyarrays(args):
		a = args[0]
		for i in range(lgt):
			if i != 0 :
				a -= args[i]
		return a
#### AVRGARRAYS : takes differents 1D arrays and create one with the average value in each previous ones
def avrgarrays(*args):
	""" Takes differents 1D arrays and create one with the average value in each previous ones """
	lgt = len(args)
	if verifyarrays(args):
		a = np.zeros(len(args[0]))
		for i in range(lgt):
			a += args[i]
		return (a / lgt)

#### AVRGIMGDIR : takes all images in one of the pre-defined directories and return an array with the average spectrum of all images 
def avrgimgdir(spc_folder,folder_name):
	""" Takes all the images in one of the pre-defined directories and return an array with the average intensity spectrum of all images. Takes the current directory name and the directory wanted as parameter. """

	os.chdir(spc_folder + '/images-source/' + folder_name)
	samplefile_list = os.listdir(os.getcwd())
	smpimgarrays = [ img2array(x,os.getcwd()) for x in samplefile_list ]
	alpha = img2array(samplefile_list[0],os.getcwd())
	l = alpha.shape[0]
	w = alpha.shape[1]
	smparrays = np.empty((len(smpimgarrays),l,w))
	for a in range(len(samplefile_list)):
		smparrays[a] = np.array(smpimgarrays[a])
	intsmparrays = np.empty((len(smpimgarrays),l))
	for b in range(len(smpimgarrays)):
		intsmparrays[b] = array2spec(smparrays[b])
	itavsmp = avrgarrays(*intsmparrays)


	return itavsmp
#### MAXARRAY : returns the maximum peak in a spectrum as [pixel,value] 
def maxarray(ar):

	""" return the maximum peak coordinates of a spectrum. the input is the array name and the output is an array containing [pixel,value] """
	max_int = ar[0]
	for i in range(len(ar)):
		if ar[i] > max_int : 
			max_int = ar[i]
			max_pixel = i
	mxar = np.array([max_pixel,max_int])
	return mxar

#### PTCLENERGY : returns the particle energy point of view in a raman-type spectrum, needs the array of the spectrum and a reference peak 
def ptclenergy(arr,refpeak):
	""" takes a peak and uses it as reference to give a particle point of view relative to this peak. input the array of the spectrum and the reference peak pixel """
	rfp = int(refpeak)
	energ = np.arange(rfp)
	for i in range(rfp):
		energ[i] = arr[(rfp - i)]
	return energ
