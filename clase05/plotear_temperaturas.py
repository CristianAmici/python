import matplotlib.pyplot as plt
import numpy as np
def plotear_temperaturas():
    temperaturas=np.loadtxt('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=25)
    plt.show() 
plotear_temperaturas()