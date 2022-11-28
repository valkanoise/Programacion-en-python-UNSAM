import matplotlib.pyplot as plt
import numpy as np


def plotear_temperaturas():
    vector_temperaturas = np.load('../Data/temperatura.npy')
     
     
    plt.hist(vector_temperaturas,bins=25)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.