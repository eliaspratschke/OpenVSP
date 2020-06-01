import numpy as np
import matplotlib.pyplot as plt

#plots the solver residual and l/d value


residuals = np.genfromtxt('GMRES.txt', delimiter=',' ,max_rows=50)
perf = np.genfromtxt('LoverD.txt', delimiter=',',max_rows=50)

iterations = len(residuals)

j = np.arange(iterations)



plt.plot(j, perf, linewidth=0.5)
plt.xlabel('wake iterations')
plt.ylabel('L/D')
plt.title('')
plt.scatter(j, perf)
plt.savefig('/Users/eliaspratschke/Desktop/bachelorarbeit/python/figures/convergence.png', transparent=True, dpi=900)
plt.show()

plt.plot(j,residuals, linewidth=0.5)

plt.yscale('log')
plt.xlabel('Solver iterations')
plt.ylabel('log10(residual)')
plt.title('')

plt.savefig('/Users/eliaspratschke/Desktop/bachelorarbeit/python/figures/GMRES.png', transparent=True, dpi=900)
plt.show()