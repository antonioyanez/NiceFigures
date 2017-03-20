import sys; sys.path.insert(0,'/usr/local/lib/python2.7/dist-packages')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

gs = gridspec.GridSpec(1,1,bottom=.08,left=.11,top=.99,right=.99)
fig = plt.figure(figsize=(6.25,6.3))
ax = fig.add_subplot(gs[0,0])

x = np.linspace(-10,10,1001)

ax.plot(x,np.sin(2*np.pi*x/2)/x)
ax.set_ylabel('V (mV)')
ax.set_xlabel('t (ms)')


fig.savefig('figure.pdf')
fig.show()
