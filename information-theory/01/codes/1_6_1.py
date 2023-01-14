import numpy as np
import matplotlib.pyplot as plt

N = 1000
X = np.linspace(0.1,10,N)
plt.plot(X, np.log2(X))
plt.grid()
plt.tight_layout()
plt.savefig('../figs/1_6_1.png')
plt.show()