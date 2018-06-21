import os as os
import sys as sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

import Generic as ge
import Read as rd
import TrajectoryAnalysis as ta
import Write as wr

def msd_plot(Time, MSD, XMSD, YMSD, ZMSD):
    '''
    MSDPlot - Plot MSD 
    
    Parameters 
    ----------
    first  : 1D array
             Timesteps
    second : 1D array
             MSD values
    third  : 1D array
             XMSD values
    fourth : 1D array
             YMSD values
    filth  : 1D array
             ZMSD values
             
    Return
    ------
    matplotlib plot - png
    
    '''
    
    YMax = np.amax(MSD)
    XMax = np.amax(Time)
    plt.ylim(ymin=0, ymax=YMax)
    plt.xlim(xmin=0, xmax=XMax)
    plt.scatter(Time, MSD, color="crimson", label="MSD", s=5)
    plt.scatter(Time, XMSD, color="blue", label="XMSD",  s=5)
    plt.scatter(Time, YMSD, color="black", label="YMSD",  s=5)
    plt.scatter(Time, ZMSD, color="darkgreen", label="ZMSD",s=5)
        
    plt.xlabel("Timestep (ps)", fontsize=15)
    plt.ylabel("MSD", fontsize=15)
    plt.savefig("MSD.png", dpi=600)

def msd_output(MSD, XMSD, YMSD, ZMSD, Time):
    '''
    MSDOutput - Writes out the values of MSD calc to a file
    
    Parameters 
    ----------
    first  : 1D array
             Timesteps
    second : 1D array
             MSD values
    third  : 1D array
             XMSD values
    fourth : 1D array
             YMSD values
    filth  : 1D array
             ZMSD values
    
    Return
    ------
    text file
    
    '''
    A = np.array([])
    A = np.append(A, MSD)
    A = np.append(A, XMSD)
    A = np.append(A, YMSD)
    A = np.append(A, ZMSD)
    A = np.split(A, 4)
    np.savetxt("MSD.txt", A, delimiter=',')
            
    
def diffusion_output(DiffusionCo, XDiffusionCo, YDiffusionCo, ZDiffusionCo):
    '''
    DiffusionOutput - Write out diffusion coefficients to a file
    
    Parameters
    ----------
    first  : float
             Diffusion coefficient
    second : float
             Diffusion coefficient in x
    third  : float
             Diffusion coefficient in y
    fourth : float
             Diffusion coefficient in z
    
    Return
    ------
    Text file
    
    '''
    DiffusionCo = str(DiffusionCo)
    XDiffusionCo = str(XDiffusionCo)
    YDiffusionCo = str(YDiffusionCo)
    ZDiffusionCo = str(ZDiffusionCo)
    Output = open("Diffusion.txt", "w")
    Output.write("3D Diffusion Coefficient: " + DiffusionCo + " m^2/s (10^-9)\n")
    Output.write("2D X Diffusion Coefficient: " + XDiffusionCo + " m^2/s (10^-9)\n")
    Output.write("2D Y Diffusion Coefficient: " + YDiffusionCo + " m^2/s (10^-9)\n")
    Output.write("2D Z Diffusion Coefficient: " + ZDiffusionCo + " m^2/s (10^-9)\n")
    Output.close()    

def pmsd_plot(Average, Diffusion):
    '''
    PMSDPlot - Plot for PMSD function
    
    Parameters 
    ----------
    first  : numpy array
             Average positions
    second : numpy array
             Diffusion data
             
    Return
    ------
    matplotlib plot
    
    '''
    YMax = np.amax(Diffusion)
    XMax = np.amax(Average)
    XMin = np.amin(Average)
    plt.ylim(ymin=0, ymax=YMax)
    plt.xlim(xmin=XMin, xmax=XMax)
    plt.scatter(Average, Diffusion, color="crimson", label="MSD", s=5)
    plt.xlabel("Distance from Interface", fontsize=15)
    plt.ylabel("Diffusion Coefficient", fontsize=15)
    plt.savefig("PMSD.png", dpi=600)
    
def pmsd_average_plot(Bins, Diffusion, Coef):
    '''
    PMSDAvPlot - Plot for PMSD in bins
    
    Parameters
    ----------
    first  : numpy array
             Bins
    second : numpy array
             Diffusion data in each bin
    third  : float
             Overall diffusion value
             
    Return
    ------
    matplotlib plot
    
    '''
    plt.axhline(y=Coef, ls='dashed', color='grey')
    plt.scatter(Bins, Diffusion, color="crimson", label="MSD", s=5)
    plt.xlabel("Distance from Interface", fontsize=15)
    plt.ylabel("Diffusion Coefficient", fontsize=15)
    plt.savefig("PMSDAv.png", dpi=600)
    
    
def line_plot(X, Y, XLab, YLab):
    '''
    LinePlot - Simple line plot
    
    Parameters
    ----------
    first  : numpy object
             X axis values
    second : numpy object
             Y axis values
    third  : str
             X label
    fourth : str
             Y label
             
    Return
    ------
    matplotlib plot
    
    '''
    plt.plot(X, Y, color="crimson")
    plt.xlabel(XLab, fontsize=13)
    plt.ylabel(YLab, fontsize=13)
    plt.savefig("LinePlot.png", dpi=600)
    

def contour_plot(X, Y, Z):
    '''
    CountourPlot - Contour plotting tool
    
    Parameters 
    ----------
    first  : numpy 
             X axis
    second : numpy 
             Y axis
    third  : 2D numpy array
             grid
             
    Return
    ------
    matplotlib plot
    
    '''
   
    plt.contourf(X, Y, Z, cmap="hot", norm = colors.LogNorm(vmin=Z.min(), vmax=Z.max()))
    plt.xlabel("X Coordinate", fontsize=15)
    plt.ylabel("Y Coordinate", fontsize=15)
    plt.colorbar()
    plt.savefig("Heatmap.png", dpi=600)
    
