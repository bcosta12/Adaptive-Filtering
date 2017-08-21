import scipy as sp
import numpy as np

#doc at https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html

def conv(in1, in2):
	'''
	input 
		in1: array_like, fist input
		in2: array_like, second input
	output
		array containing a subset of the discrete linear convolution of in1 with in2.
	'''
	mode='full'# The output is the full discrete linear convolution of the inputs. (Default) 
	convolved = np.asarray(sp.convolve(in1, in2, mode)) #numpy array it is better to math applications
	return convolved

def filter(in1, in2):
	'''
	input 
		in1: array_like, fist input
		in2: array_like, second input
	output
		array containing a subset of the discrete linear convolution of in1 with in2, The output is the same size as in1, starting from the beginning 
	'''
	filtered = np.asarray(conv(in1, in2)) #numpy array its better to math applications 
	filtered = filtered[0:len(in1)] #reshape
	return filtered