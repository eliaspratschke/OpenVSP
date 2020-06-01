import numpy as np
import matplotlib.pyplot as plt

#generate arrays from our text files
iterations = 56
numlines = 60
nodes = 17
lines = np.zeros((iterations, nodes, numlines, 3))
left = np.zeros((iterations, nodes, int(0.5 * numlines), 3))
right = np.zeros((iterations, nodes, int(0.5 * numlines), 3))

streamlinesx = np.genfromtxt('Streamlinex.txt', delimiter=',')
streamlinesy = np.genfromtxt('Streamliney.txt', delimiter=',')
streamlinesz = np.genfromtxt('Streamlinez.txt', delimiter=',')


#put streamline coordinates in easier to use array line[iteration][nodelevel][streamline][coordinate direction]
for i in range(iterations):
    for j in range(nodes):
        for k in range(numlines):

            lines[i, j, k, 0] = streamlinesx[k + i * numlines, j]
            lines[i, j, k, 1] = streamlinesy[k + i * numlines, j]
            lines[i, j, k, 2] = streamlinesz[k + i * numlines, j]

#instead of sorting array, split it into two parts, wich are already sorted
for i in range(iterations):
    for j in range(nodes):
        for k in range(0, int(0.5 * numlines)):
            left[i, j, k, 0] = lines[i, j, k, 0]
            left[i, j, k, 1] = lines[i, j, k, 1]
            left[i, j, k, 2] = lines[i, j, k, 2]

        for k in range(0, int(0.5 * numlines)):
             right[i, j, k, 0] = lines[i, j, k + int(0.5 * numlines), 0]
             right[i, j, k, 1] = lines[i, j, k + int(0.5 * numlines), 1]
             right[i, j, k, 2] = lines[i, j, k + int(0.5 * numlines), 2]

#loop over array and print it
for i in range(iterations):
    fig = plt.figure(figsize=plt.figaspect(0.5)*1.8)
    ax = fig.gca(projection='3d')
    ax.view_init(30, 240)

    #uncomment loop below to get a mesh instead of contours

    #for j in range(int(numlines * 0.5)):
     #   if j > (int(numlines * 0.5) - 7):
      #      ax.plot(streamlinesx[j + (i) * numlines], streamlinesy[j + (i) * numlines], streamlinesz[j + (i) * numlines], lw=0.4, c='k')
       # else:
        #    ax.plot(streamlinesx[j + (i) * numlines], streamlinesy[j + (i) * numlines],streamlinesz[j + (i) * numlines], lw=0.4,c='k')


    for j in range(nodes):
        for k in range(numlines):

            ax.plot(left[i, j, :, 0], left[i, j, :, 1], left[i, j, :, 2], lw=0.7)
            ax.plot(right[i, j, :, 0], right[i, j, :, 1], right[i, j, :, 2], lw=0.5)
            ax.set_xlim([4, 24])
            ax.set_ylim([-20, 20])
            ax.set_zlim([0, 5])
            ax.set_ylabel("Y Axis")
            ax.set_zlabel("Z Axis")
            ax.set_xlabel("X Axis")

    plt.savefig('/Users/eliaspratschke/Desktop/bachelorarbeit/python/figures/iteration%i.png' % (i + 1), dpi=400)
    plt.show()
    
