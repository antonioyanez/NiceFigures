import sys; sys.path.insert(0,'/usr/local/lib/python2.7/dist-packages')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec


class MyFigure(object):
    def __init__(self,figsize=(6.25,6.3),left=.12,bottom=.08):
        self.right = .99    # parameter, more difficult to move
        self.top = .95    # parameter, more difficult to move
        self.left = left
        self.bottom = bottom
        self.fig = plt.figure(figsize=figsize,dpi=100)

    def make_axes(self,nrows=1,ncols=1):
        # horizontal alignment
        left = self.left
        right = self.right
        wspace = left / (right/ncols - left)
        self.wspace = wspace
        # vertical alignment
        self.hspace = self.bottom /(self.top/nrows - self.bottom )
        self.gs = gridspec.GridSpec(nrows,ncols,
            hspace=self.hspace,wspace=wspace,
            bottom=self.bottom,left=left,
            top=self.top,right=right)
        self.axes = [ self.fig.add_subplot(self.gs[i,j]) for i in range(nrows) 
                                        for j in range(ncols)]
    
        return self.gs

    def add_labels(self):
        texts = [ ax.text(-.7*self.wspace,1+.3*self.hspace,chr(65+i),
                        va='center',ha='center',
                        fontweight='bold',
                        transform=ax.transAxes) 
                    for i, ax in enumerate(self.axes) ]



class PlayFig(MyFigure):
    def __init__(self,nrows=1,ncols=1,show=True):
        super(PlayFig,self).__init__()
        self.make_axes(nrows=nrows,ncols=ncols)
        self.add_labels()
        self.paint_something()
        if show:
            self.fig.show()

    def paint_something(self):
        x = np.linspace(-10,10,1001)
        for ax in self.axes:
            ax.plot(x,np.sin(2*np.pi*x/2)/x)
            ax.set_ylabel('V (mV)')
            ax.set_xlabel('t (ms)')

    

figs = [ PlayFig(i,j,show=False)  for j in range(1,6) for i in range(1,6) ]
gs = figs[0].gs
save = [ fig.fig.savefig('axes_{0:02d}.png'.format(i)) for i, fig in enumerate(figs) ]




