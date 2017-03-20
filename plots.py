import sys; sys.path.insert(0,'/usr/local/lib/python2.7/dist-packages')
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.linspace(-10,10,1001)

ax.plot(x,np.sin(2*np.pi*x/2)/x)


fig.savefig('figure.pdf')
fig.show()
