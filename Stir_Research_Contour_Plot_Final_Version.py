# -*- coding: utf-8 -*-
"""
Created on Sat Oct 2 22:09:32 2019

@author: Shrishti D Hore
"""
'''
#ACTUAL 3D WORKING MODEL 
# CONSISTS OF ALL THE DATA 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
from mpl_toolkits.mplot3d import Axes3D
import os

f = open("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\corrosion_final_data.csv")
data = np.genfromtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\corrosion_final_data.csv", delimiter =',')

for line in f:
    print(line)

x,y  = np.meshgrid(data[:,0], data[:,1])
z = np.tile(data[:,2], (len(data[:,2]), 1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.contour(x, y,z, cmap = plt.get_cmap('rainbow'))
plt.colorbar()

plt.title("Corrosion Resistance Contour")

plt.show()
'''

'''
# CONSISTS OF ROTATIONAL SPEED ANALYSIS CONTOUR
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
from mpl_toolkits.mplot3d import Axes3D
import os

f = open("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\rotational_speed.csv")
data = np.genfromtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\rotational_speed.csv", skip_header = 1, delimiter =',')

for line in f:
    print(line)

x,y  = np.meshgrid(data[:,0], data[:,1])
z = np.tile(data[:,2], (len(data[:,2]), 1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.contour(x, y,z, cmap = plt.get_cmap('rainbow'))
plt.colorbar()

plt.title("Rotational Speed Contour")

plt.show()
'''

'''
# CONSISTS OF WELDING SPEED ANALYSIS CONTOUR
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
from mpl_toolkits.mplot3d import Axes3D
import os

f = open("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Welding_speed.csv")
data = np.genfromtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Welding_speed.csv", skip_header = 1, delimiter =',')

for line in f:
    print(line)

x,y  = np.meshgrid(data[:,0], data[:,1])
z = np.tile(data[:,2], (len(data[:,2]), 1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.contour(x, y,z, cmap = plt.get_cmap('rainbow'))
plt.colorbar()

plt.title("Welding Speed Contour")

plt.show()
'''

'''
# CONSISTS OF AXIAL FORCE ANALYSIS CONTOUR
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
from mpl_toolkits.mplot3d import Axes3D
import os

f = open("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Axial_Force.csv")
data = np.genfromtxt("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\Axial_Force.csv", skip_header = 1, delimiter =',')

for line in f:
    print(line)

x,y  = np.meshgrid(data[:,0], data[:,1])
z = np.tile(data[:,2], (len(data[:,2]), 1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.contour(x, y,z, cmap = plt.get_cmap('rainbow'))
plt.colorbar()

plt.title("Axial Force Contour")

plt.show()
'''