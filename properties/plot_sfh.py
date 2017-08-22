# This script plots the star formation history for the GM                                           
# suite for h243 given OUTPUTS from sfhistory.py  
import matplotlib.pyplot as plt
import numpy as np
import pynbody


data =['P0_sfhistory_bins.txt','GM1_sfhistory_bins.txt','GM4_sfhistory_bins.txt','GM5_sfhistory_bins.txt','GM6_sfhistory_bins.txt','GM7_sfhistory_bins.txt']
labels = ['P0','GM1','GM4','GM5','GM6','GM7']
colors = ['DodgerBlue','SteelBlue','FireBrick','IndianRed','Salmon','Orange']

for i in range(1):#len(data)):
    dt = np.transpose(np.loadtxt(data[i]))
    SFR = dt[0]
    time = dt[1]

    plt.plot(time,SFR,color=colors[i],drawstyle=steps)
    plt.show()