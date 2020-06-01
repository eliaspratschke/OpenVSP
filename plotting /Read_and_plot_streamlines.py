import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#this plots the streamlines for each iteration. Not best way to visualse wake

streamlinesx = np.genfromtxt('Streamlinex.txt', delimiter=',')
streamlinesy = np.genfromtxt('Streamliney.txt', delimiter=',')
streamlinesz = np.genfromtxt('Streamlinez.txt', delimiter=',')

j = 1
NumLines = 60
totaliter = 50
ResRed = 1
Relax = 0.85
Nodes = 16
#time = 110
AoA = 10

LoverD = np.genfromtxt('LoverD.txt', delimiter=',')
iter = np.linspace(1, totaliter, totaliter)

cmap = sns.color_palette("GnBu_d",7)

#c= cmap[int((len(cmap) - 1) * np.abs(streamlinesy[i][0] / 20)**2)]

#cmap=sns.dark_palette("Blues", NumLines)


for j in range(0,totaliter):
    fig = plt.figure(figsize=plt.figaspect(0.5)*1.8)
    ax = fig.gca(projection='3d')

    for i in range(int(NumLines * 0.5), NumLines):
        if i > (NumLines - 7):
            ax.plot(streamlinesx[i + (j) * NumLines], streamlinesy[i + (j) * NumLines], streamlinesz[i + (j) * NumLines], lw=0.5)
        else:
            ax.plot(streamlinesx[i + (j) * NumLines], streamlinesy[i + (j) * NumLines],streamlinesz[i + (j) * NumLines], lw=0.5,c='k')
    ax.set_xlabel("X Axis")
    #ax.set_xlim([0,20])
    #ax.set_ylim([-11,0])
    #ax.set_zlim([0, 2.6])
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title('Iteration {}' .format((j+1)))
    ax.view_init(30, 110)
    plt.savefig('/Users/eliaspratschke/Desktop/bachelorarbeit/python/figures/iteration%i.png' % (j + 1), dpi=400)
    #plt.show()






#for i in range(len(LoverD)):
#    LoverD[i] = np.log10(np.abs(LoverD[i]))

#plt.plot(iter, LoverD)
#plt.scatter(iter, LoverD)
#plt.grid()
#plt.title('AoA={} relax={}, ResRed={}, WakeNodes={}' .format(AoA, Relax, ResRed, Nodes))
#plt.yscale('log')
#plt.savefig('/Users/eliaspratschke/Desktop/bachelorarbeit/python/figures/convergence.png', dpi=400)
#plt.show()