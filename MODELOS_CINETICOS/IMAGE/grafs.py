import numpy as np
import matplotlib.pyplot as plt

xx = np.linspace(1e-5,5,200)
yy = xx/(1+xx)

plt.plot(xx,yy, label = 'Michaelis-Menten')
plt.xlabel('[S]')
plt.ylabel('V')
plt.xticks([])
plt.yticks([])
plt.axvline(x=1,color='r',linestyle='--', label = r'$k_f$')
plt.axhline(y=1,color='g',linestyle='-.', label = r'$V_{max}$')
plt.axhline(y=0.5,color='r',linestyle='--', label = r'$V_{max}$/2')
plt.legend()
plt.show()
