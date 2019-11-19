#importing the libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
 
# Get the data 
data = pd.read_csv("C:\\Users\\Shrishti D Hore\\OneDrive\\Documents\\Stir_Research\\corrosion_final_data.csv")
 
# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# And transform the old column name in something numeric
df['X']=pd.Categorical(df['X'])
df['X']=df['X'].cat.codes
 
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')

'''
#defining the plot as trisurface
ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
'''
#setting the labels
ax.set_xlabel('axial_force')     
ax.yaxis.set_label_text('welding_speed')
ax.zaxis.set_label_text('rotational_speed ')

#setting the title
ax.set_title("Tri_surface_plot")

#rotating the plot
ax.view_init(30, 60)

'''
#rotating for different p.o.v
ax.view_init(60, 30)

'''

'''
#displaying the plot
plt.show()
'''

# to Add a color bar which maps values to colors.
surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar( surf, shrink=0.8, aspect=10)
plt.show()
 
