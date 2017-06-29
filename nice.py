import sys; sys.path.insert(0,'/usr/local/lib/python2.7/dist-packages')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec


class MyFigure(object):
    def __init__(self,figsize=None,left=.12,bottom=.07):
        self.right = .99    # parameter, more difficult to move
        self.top = 1-.95    # parameter, more difficult to move
        self.left = left
        self.bottom = bottom
        self.fig = plt.figure(figsize=figsize,dpi=100)

    def grisspec(self,nrows=1,ncols=1):
        self.wspace = self.left / (self.right/ncols - self.left)
        self.hspace = self.bottom /(self.top/nrows - self.bottom )
        self.hspace = (self.bottom+self.top) /(1./nrows - self.bottom-self.top )
        self.nrows = nrows
        self.ncols = ncols
        self.gs = gridspec.GridSpec(nrows,ncols,
            hspace=self.hspace,wspace=self.wspace,
            bottom=self.bottom,left=self.left,
            top=1-self.top,right=self.right)
    
        return self.gs

    def make_axes(self):
        self.axes = [ self.fig.add_subplot(self.gs[i,j]) for i in range(nrows)
                     for j in range(ncols)]

    def add_labels(self):
        texts = [ ax.text(-.7*self.wspace,1+.2*self.hspace,chr(65+i),
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

    
aa = plt.style.use('/home/antonio/NiceFigures/antonio.mplstyle')
if __name__ == '__main__':
    #figs = [ PlayFig(j,i,show=False)  for j in range(1,6) for i in range(1,6) ]
    #gs = figs[0].gs
    #save = [ fig.fig.savefig('axes_{0:02d}.png'.format(i)) for i, fig in enumerate(figs) ]

    ff = PlayFig(4,5)
    ff.fig.savefig('figure.pdf')


