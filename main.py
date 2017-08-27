import numpy as np
import scipy as sp
import src.supportFunctions as sf
import src.models as ms
import math as math
import alg.algs as al
import sys as sys
import matplotlib.pyplot as plt

sys.path.append('/src')
sys.path.append('/alg')

#initial parameters 
w0 = ms.models(2)
sigmanu2 = 10 ** (-6)
numberOfRepeats = 10
N = len(w0)
betaVector = [5*(10**(-4))]
numberOfSamples = 20000

MSE = np.zeros(( numberOfSamples - N, len(betaVector) ))
MSD = np.zeros(( numberOfSamples - N, len(betaVector) ))


for repeat in range(numberOfRepeats):

    for betaIndex in range(len(betaVector)):
        
        beta = betaVector[betaIndex]
        
        x = (np.random.standard_normal(numberOfSamples))
        d = sf.filter( w0 , 1 , x )
        d = d + math.sqrt( sigmanu2 ) * np.random.standard_normal(numberOfSamples)
        wk = np.zeros((N,1))
        
        
        for k in range(N, numberOfSamples):

            xk = x[k-N:k]
            #xk = np.array(list(reversed(xk)))
            xk = np.reshape(xk, (len(xk), 1))

            yk = np.dot(wk.T,xk)
            ek = d[k] - yk

            MSE[ k - N, betaIndex] = MSE[ k - N, betaIndex] + ek ** 2 /numberOfRepeats
            MSD[ k - N, betaIndex ] = MSD[ k - N, betaIndex ] + ( np.linalg.norm(wk-w0)) ** 2 / numberOfRepeats 
            
            wk = wk + beta * xk * ek
            
print(wk[0:5])
print(w0[0:5])
xAxis = range(N, 19000-N+1)
yAxis = []
for i in range(N, 19000-N+1):
    yAxis.append(10.0 * np.log10(MSE[i][0]))
plt.plot( xAxis, yAxis) 
plt.show()
