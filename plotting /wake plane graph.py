import numpy as np
import matplotlib.pyplot as plt
#ony plots last line of wake nodes
#generate arrays from our text files

streamlinesx = np.genfromtxt('Streamlinex.txt', delimiter=',')
streamlinesy = np.genfromtxt('Streamliney.txt', delimiter=',')
streamlinesz = np.genfromtxt('Streamlinez.txt', delimiter=',')

perf = np.genfromtxt('LoverD.txt', delimiter=',')
residual = np.genfromtxt('GMRES.txt', delimiter=',')

#at wich "plane" do we want to evaluate (in x direction)

plane = 16
iterations = 56
numlines = 60
nodes = 16

lines = np.zeros((iterations, numlines, 3))

#copy plane of interest into lines array

def extractplane(plane):

    for i in range(iterations):
        for j in range(numlines):

            lines[i][j][0] = streamlinesx[j + i * numlines][plane]
            lines[i][j][1] = streamlinesy[j + i * numlines][plane]
            lines[i][j][2] = streamlinesz[j + i * numlines][plane]

#because we cant easily sort instead split up into two sorted arrays. if we sorted we would not get
#the correct physical location of the lines, since they often cross over at higher distances from the wing
#we would have to sort entire array at first wake node
#less work to split.

linesleft = np.zeros((iterations, 30, 3))
linesright = np.zeros((iterations, 30, 3))

def splitlist(numlines, iterations):

    for i in range(iterations):
        for j in range(0, int(0.5 * numlines)):
            linesleft[i][j][0] = lines[i][j][0]
            linesleft[i][j][1] = lines[i][j][1]
            linesleft[i][j][2] = lines[i][j][2]

        for j in range(0, int(0.5 * numlines)):
            linesright[i][j][0] = lines[i][j + int(0.5 * numlines)][0]
            linesright[i][j][1] = lines[i][j + int(0.5 * numlines)][1]
            linesright[i][j][2] = lines[i][j + int(0.5 * numlines)][2]

#sort array for printing

#for i in range(iterations):
 #   B = lines[i, :, :]
  #  idx = B[:, 1].argsort()

   # lines[i, :, :] = B[idx, :]


extractplane(16)
splitlist(numlines, iterations)

#set up to plot a wake with correct proportions in a node plane

for i in range(iterations):
    fig = plt.figure(figsize=plt.figaspect(1.0)*2.5)
    ax = fig.gca()
    #ax.axis('off')
    plt.plot(linesleft[i, :, 1], linesleft[i, :, 2], lw=0.7, c='k')
    plt.plot(linesright[i, :, 1], linesright[i,:,2], lw=0.7, c='k')
    ax.set_xlim([-21, 21])
    ax.set_ylim([0, 7])
    #ax.set_title('Iteration {}'.format((i+1)))
    ax.text(.5, .9, 'Iteration {}' .format((i+1)),
            horizontalalignment='center',
            transform=ax.transAxes)
    #ax = plt.axes()
    #ax.plot([0, 1], [0, 10])
    ax.set_ylabel("Z Axis")
    #ax.set_zlabel("Z Axis")
    ax.set_xlabel("Y Axis")
    ax.set_aspect('equal', 'box')
    plt.savefig('/Users/eliaspratschke/Desktop/bachelorarbeit/python/figures/iteration%i.png' % (i + 1),dpi=400, transparent=True)
    #plt.show()



