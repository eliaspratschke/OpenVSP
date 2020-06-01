import numpy as np
import matplotlib as plt

#this imports the system matrix when used in combination with GetMatrix

influence = np.genfromtxt('influence.txt', delimiter=',')
A = np.transpose(influence)

b = np.genfromtxt('RHS.txt', delimiter=',')

GMRES_Sol = np.genfromtxt('Solution.txt', delimiter=',')

sol = np.linalg.solve(A,b)

c = sol - GMRES_Sol

error = np.linalg.norm(c)

cond = np.linalg.cond(A)

diff = influence -A

plt.pyplot.matshow(diff)

print(diff)
#print(cond)

#plt.pyplot.matshow(A)

plt.pyplot.show()

#print(error)