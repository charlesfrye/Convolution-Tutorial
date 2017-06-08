import matplotlib.pyplot as plt
import numpy as np

# A Whole Bunch of Convenience Functions for Cleaning Up Plots
def removeAxes(ax):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

def removeFrames(ax,sides=['top','right']):
    for side in sides:
        ax.spines[side].set_visible(False)

def removeTicks(ax,axes):
    if 'x' in axes:
        ax.tick_params(axis='x',
                        which='both',
                        top='off',
                        labeltop='off',
                        bottom='off',
                        labelbottom='off')
    if 'y' in axes:
        ax.tick_params(axis='y',
                        which='both',
                        left='off',
                        labelleft='off',
                        right='off',
                        labelright='off')

def addAxis(ax,axis='horizontal'):
    if axis == 'horizontal':
        xmin,xmax = ax.get_xlim()
        ax.hlines(0,xmin,xmax)
    elif axis == 'vertical':
        ymin,ymax = ax.get_ylim()
        ax.vlines(0,ymin,ymax)

def cleanPlot(ax):
    removeFrames(plt.gca(),['top','right','bottom']);
    removeTicks(plt.gca(),['x','y']);

def setLims(ax,xBounds,yBounds):
    ax.set_xlim(xBounds); ax.set_ylim(yBounds);

def plotSignal(signal,signalName):
    plt.figure(figsize=(12,2));
    plt.plot(signal,'-o',color='k');
    cleanPlot(plt.gca()); 
    plt.xlim(-len(signal)/10,len(signal)+len(signal)/10);
    addAxis(plt.gca(),'horizontal');
    plt.title(signalName);

def plotSignalAsDelta(signal,signalName,color='r'):
    plt.figure(figsize=(16,4)); plt.subplot(2,1,1)
    plt.plot(signal,'-o',color='k');
    cleanPlot(plt.gca()); 
    plt.xlim(-len(signal)/10,len(signal)+len(signal)/10);
    addAxis(plt.gca(),'horizontal');
    plt.title(signalName);
    plt.subplot(2,1,2)
    deltaPlot(signal,color=color);
    cleanPlot(plt.gca()); 
    plt.xlim(-len(signal)/10,len(signal)+len(signal)/10);
    addAxis(plt.gca(),'horizontal');
    plt.title('also ' +signalName);
        
def deltaPlot(inp,color='r'):
    plt.scatter(np.arange(0,len(inp)),inp,
                linewidth=0,marker='o',s=36,color=color,
                zorder=10); 
    plt.vlines(np.arange(0,len(inp)),0,inp,)

def plotKronecker():
    pad=[0,0]; padLen = len(pad)
    deltaPlot(pad+[1]+pad,color='b')
    cleanPlot(plt.gca());
    plt.xlim(-padLen/10,2*padLen+1+padLen/10)
    addAxis(plt.gca(),'horizontal');
    plt.title('the delta function')
    
def kernelsPlot(kernels,kernelNames):
    numKernels = len(kernels)
    plt.figure(figsize=(16,4));
    
    for idx,(kernel,name) in enumerate(zip(kernels,kernelNames)):
        plt.subplot(1,numKernels,idx+1)
        deltaPlot(kernel)
        cleanPlot(plt.gca()); 
        plt.xlim(-len(kernel)/10,len(kernel)+len(kernel)/10);
        addAxis(plt.gca(),'horizontal');
        plt.title(name);
        
def convolutionPlot(signals,signalName,kernels,kernelNames):
    for idx,(signal,kernel,kernelName) in enumerate(zip(signals[1:],kernels,kernelNames)):
        plt.figure(figsize=(16,4));
        
        plt.subplot(1,3,1)
        #Plot the original signal for reference
        deltaPlot(signals[0],color='blue');
        plt.title(signalName); plt.ylim(-1,1.5); 
        plt.xlim(-len(signals[0])/10,len(signals[0])+len(signals[0])/10); 
        cleanPlot(plt.gca()); addAxis(plt.gca(),'horizontal')
    
        plt.subplot(1,3,2)
        #Plot the kernel for reference
        deltaPlot(kernel)
        plt.title(kernelName); plt.ylim(-1,1.5); 
        plt.xlim(-len(kernel)/10,len(kernel)+len(kernel)/10); 
        cleanPlot(plt.gca()); addAxis(plt.gca(),'horizontal')
    
        plt.subplot(1,3,3)
        #Plot convolved signal
        outName = signalName+'*'+kernelName
        deltaPlot(signal,color='purple'); plt.ylim(-1,1.5); 
        plt.xlim(-len(signal)/10,len(signal)+len(signal)/10);  
        cleanPlot(plt.gca()); addAxis(plt.gca(),'horizontal')
        plt.title(outName);

def randomWalk(tMax=1,sigma=1,eps=0.1):
    signal=[0]; scaleFactor = np.sqrt(eps)
    for t in np.arange(0,tMax,eps):
        signal.append(signal[-1]+np.random.normal(0,sigma*scaleFactor))
    return np.asarray(signal[1:])
