import numpy as np 

def lms(wk, beta, xk, ek):
	  '''
    input 
        wk: 
        beta: beta of lms classic algorithm 
        xk:
        ek: error of k
    output
        numpy-array containing lms interaction
    '''

	wk = np.asarray(wk)
	xk = np.asarray(xk)
	ek = np.asarray(ek)
	return wk + beta * xk * ek