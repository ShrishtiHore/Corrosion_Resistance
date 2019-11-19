# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:45:23 2019

@author: Shrishti D Hore
"""

#for axial force
'''
#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#importing the dataset
DataAll1D = np.loadtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Axial_Force.csv", skiprows = 1, delimiter=",")

# create 2d x,y grid (both X and Y will be 2d)
X, Y = np.meshgrid(DataAll1D[:,0], DataAll1D[:,1])

# repeat Z to make it a 2d grid
Z = np.tile(DataAll1D[:,2], (len(DataAll1D[:,2]), 1))

#setting the figure plot and subplot as 3d projection
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#setting the title 
ax.set_title("Axial Force Surface Plot")

#setting the labels
ax.set_xlabel('rotational speed')     
ax.yaxis.set_label_text('Axial Force')
ax.zaxis.set_label_text('Corrosion_pit_per_mv ')

#defining the plot as 3d surface
ax.plot_surface(X, Y, Z, cmap='ocean')


#rotating the plot
#ax.view_init(30, 60)

#displaying the plot
plt.show()
'''
#for rotational speed
'''
#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#importing the dataset
DataAll1D = np.loadtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\rotational_speed.csv", skiprows = 1, delimiter=",")

# create 2d x,y grid (both X and Y will be 2d)
X, Y = np.meshgrid(DataAll1D[:,0], DataAll1D[:,1])

# repeat Z to make it a 2d grid
Z = np.tile(DataAll1D[:,2], (len(DataAll1D[:,2]), 1))

#setting the figure plot and subplot as 3d projection
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#setting the title 
ax.set_title("Rotational Speed Surface Plot")

#setting the labels
ax.set_xlabel('Axial Force')     
ax.yaxis.set_label_text('Rotational Speed')
ax.zaxis.set_label_text('Corrosion_pit_per_mv ')

#defining the plot as 3d surface
ax.plot_surface(X, Y, Z, cmap='viridis')


#rotating the plot
#ax.view_init(30, 60)

#displaying the plot
plt.show()
'''
#for welding speed
'''
#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#importing the dataset
DataAll1D = np.loadtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Welding_speed.csv", skiprows = 1, delimiter=",")

# create 2d x,y grid (both X and Y will be 2d)
X, Y = np.meshgrid(DataAll1D[:,0], DataAll1D[:,1])

# repeat Z to make it a 2d grid
Z = np.tile(DataAll1D[:,2], (len(DataAll1D[:,2]), 1))

#setting the figure plot and subplot as 3d projection
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#setting the title 
ax.set_title("Welding Speed Surface Plot")

#setting the labels
ax.set_xlabel('Rotational Speed')     
ax.yaxis.set_label_text('Welding Speed')
ax.zaxis.set_label_text('Corrosion_pit_per_mv ')

#defining the plot as 3d surface
ax.plot_surface(X, Y, Z, cmap='viridis')


#rotating the plot
#ax.view_init(30, 60)

#displaying the plot
plt.show()
'''
#for all factors
'''
#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#importing the dataset
DataAll1D = np.loadtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\corrosion_final_data.csv", skiprows = 1, delimiter=",")

# create 2d x,y grid (both X and Y will be 2d)
X, Y = np.meshgrid(DataAll1D[:,0], DataAll1D[:,1])

# repeat Z to make it a 2d grid
Z = np.tile(DataAll1D[:,2], (len(DataAll1D[:,2]), 1))

#setting the figure plot and subplot as 3d projection
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#setting the title 
ax.set_title("All Factors Surface Plot")

#setting the labels
ax.set_xlabel('Rotational Speed')     
ax.yaxis.set_label_text('Welding Speed')
ax.zaxis.set_label_text('Axial Force ')

#defining the plot as 3d surface
ax.plot_surface(X, Y, Z, cmap='viridis')


#rotating the plot
#ax.view_init(30, 60)

#displaying the plot
plt.show()
'''