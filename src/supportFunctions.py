import scipy as sp
import numpy as np

#doc at https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html

def conv(in1, in2):
	'''
	input 
		in1: array_like, fist input
		in2: array_like, second input
	output
		numpy-array containing a subset of the discrete linear convolution of in1 with in2.
	'''
	mode='full'# The output is the full discrete linear convolution of the inputs. (Default) 
	convolved = np.asarray(sp.convolve(in1, in2, mode)) #numpy array it is better to math applications
	return convolved

def filter(in1, a, in2):
	'''
	input 
		in1: array_like, fist input
		a: constant that divide the filtered, note if a==1, the filter will be FIR
		in2: array_like, second input
	output
		numpy-array containing a subset of the discrete linear convolution of in1 with in2, The output is the same size as in1, starting from the beginning 
	'''
	if a == 0: raise Exception(" A value of '0' for 'a' is not allowed.") #cannot divive by zero
	filtered = np.asarray(conv(in1, in2)) #numpy array its better to math applications 
	filtered = filtered[0:len(in2)] #reshape
	if a == 1: #faster
		return filtered
	else:
		return filtered/float(a)