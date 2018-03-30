import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import sys


s_choice = [0.5,1,5,10,20]
l_choice = [50,60,70,80,90]


for gh in range(5):
    s = s_choice[gh]
    l = 70
    titl = "plot for Gini's Coefficient vs probability for source 26 and S = " + str(s)+ " and L = " + str(l)
    # per_name = 'percent_k' + str(s) + '_' + str(l)+'.csv'
    # time_name = 'time_k' + str(s) + '_' + str(l)+'.csv'
    trans_name = 'trans_k_ginni' + str(s) + '_' + str(l)+'.csv'
    ds=pd.read_csv(trans_name)
    np_arr=ds.values
    np_arr = np_arr[np.lexsort(np.transpose(np_arr)[::-1])]
    # np_arr = np.sort(np_arr,axis=0)
    # np_arr=np_arr[0:67,:]

    plt.figure()
    # plt.errorbar(np_arr[:,0],np_arr[:,5],yerr=np_arr[:,6],ecolor='red')
    plt.plot(np_arr[:,0],np_arr[:,4])
    plt.title(titl)
    plt.xlabel("probability of transmission to supernode(p)")
    plt.ylabel("Coefficient Value")
    plt.savefig("Plot/"+titl +'.png',bbox_inches='tight')


for gh in range(5):
    s = 0.5
    l = l_choice[gh]
    titl = "plot for Gini's Coefficient vs probability for source 26 and S = " + str(s)+ " and L = " + str(l)
    # per_name = 'percent_k' + str(s) + '_' + str(l)+'.csv'
    # trans_name = 'time_k' + str(s) + '_' + str(l)+'.csv'
    trans_name = 'trans_k_ginni' + str(s) + '_' + str(l)+'.csv'
    ds=pd.read_csv(trans_name)
    np_arr=ds.values
    np_arr = np_arr[np.lexsort(np.transpose(np_arr)[::-1])]
    # np_arr = np.sort(np_arr,axis=0)
    # np_arr=np_arr[0:67,:]

    plt.figure()
    # plt.errorbar(np_arr[:,0],np_arr[:,5],yerr=np_arr[:,6],ecolor='red')
    plt.plot(np_arr[:,0],np_arr[:,4])
    plt.title(titl)
    plt.xlabel("probability of transmission to supernode(p)")
    plt.ylabel("Coefficient Value")
    plt.savefig("Plot/"+titl +'.png',bbox_inches='tight')
