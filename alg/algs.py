import numpy as np 

def lms(wk, beta, xk, ek):
	'''
    input 
        wk: filter of k 
        beta: beta of lms classic algorithm 
        xk: input signal of k 
        ek: error of k
    output
        numpy-array containing lms interaction
    '''
	return wk + beta * np.dot(xk,ek)