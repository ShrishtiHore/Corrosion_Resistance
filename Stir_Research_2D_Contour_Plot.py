# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:30:05 2019

@author: Shrishti D Hore
"""
#FOR ROTATIONAL SPEED
'''
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df_xyz = pd.read_csv("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\rotational_speed.csv", delimiter=",")
x = df_xyz.iloc[:,0].values
y = df_xyz.iloc[:,1].values
z = df_xyz.iloc[:,2].values

def plot_contour(x,y,z,resolution = 50,contour_method='linear'):
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution),   min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X,Y,Z

X,Y,Z = plot_contour(x,y,z,resolution = 50,contour_method='linear')

with plt.style.context("dark_background"):
    fig, ax = plt.subplots(figsize=(13,8))
    ax.scatter(x,y, color="red", linewidth=1, edgecolor="ivory", s=50)
    ax.set_title("Rotational Speed Contour")
    ax.set_xlabel("Axial Force")
    ax.set_ylabel("Rotational Speed")
    ax.contourf(X,Y,Z)
    #ax.contour(X,Y,Z)
    
'''
'''
#FOR WELDING SPEED

import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df_xyz = pd.read_csv("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Welding_speed.csv", delimiter=",")
x = df_xyz.iloc[:,0].values
y = df_xyz.iloc[:,1].values
z = df_xyz.iloc[:,2].values

def plot_contour(x,y,z,resolution = 50,contour_method='linear'):
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution),   min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X,Y,Z

X,Y,Z = plot_contour(x,y,z,resolution = 50,contour_method='linear')

with plt.style.context("dark_background"):
    fig, ax = plt.subplots(figsize=(13,8))
    ax.scatter(x,y, color="red", linewidth=1, edgecolor="ivory", s=50)
    ax.set_title("Welding Speed Contour")
    ax.set_xlabel("Rotational Speed")
    ax.set_ylabel("Welding Speed")
    ax.contourf(X,Y,Z)
    #ax.contour(X,Y,Z)
'''
#FOR AXIAL FORCE
'''
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df_xyz = pd.read_csv("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Axial_Force.csv", delimiter=",")
x = df_xyz.iloc[:,0].values
y = df_xyz.iloc[:,1].values
z = df_xyz.iloc[:,2].values

def plot_contour(x,y,z,resolution = 50,contour_method='linear'):
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution),   min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X,Y,Z

X,Y,Z = plot_contour(x,y,z,resolution = 50,contour_method='linear')

with plt.style.context("dark_background"):
    fig, ax = plt.subplots(figsize=(13,8))
    ax.scatter(x,y, color="red", linewidth=1, edgecolor="ivory", s=50)
    ax.set_title("Axial Force Contour")
    ax.set_xlabel("Welding Speed")
    ax.set_ylabel("Axial Force")
    ax.contourf(X,Y,Z)
    #ax.contour(X,Y,Z)
'''
#FOR ALL DATA
'''
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df_xyz = pd.read_csv("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\corrosion_final_data.csv", delimiter=",")
x = df_xyz.iloc[:,0].values
y = df_xyz.iloc[:,1].values
z = df_xyz.iloc[:,2].values

def plot_contour(x,y,z,resolution = 50,contour_method='linear'):
    resolution = str(resolution)+'j'
    X,Y = np.mgrid[min(x):max(x):complex(resolution),   min(y):max(y):complex(resolution)]
    points = [[a,b] for a,b in zip(x,y)]
    Z = griddata(points, z, (X, Y), method=contour_method)
    return X,Y,Z

X,Y,Z = plot_contour(x,y,z,resolution = 50,contour_method='linear')

with plt.style.context("dark_background"):
    fig, ax = plt.subplots(figsize=(13,8))
    ax.scatter(x,y, color="red", linewidth=1, edgecolor="ivory", s=50)
    ax.set_title("All Data Contour")
    ax.set_xlabel("Rotational Speed")
    ax.set_ylabel("Axial Force")
    ax.contourf(X,Y,Z)
    #ax.contour(X,Y,Z)
'''








    