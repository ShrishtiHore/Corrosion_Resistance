# Corrosion Resistance ANN

This project was a part of my tasks during my internship at Stir Research. The project consisted of various data exploratory analysis and data visualizations to be carried out on the given data by the company. 

### Code and Resources

**Language:** Python

**Modules and Packages:** numpy, matplotlib, pandas, scikit-learn, seaborn, keras, os, csv, time

**Dataset:** Corrosion Resistance dataset by the Stir Research 

This is a Data Analytics project with the following tasks:

1. Clean the dataset and Create Visualizations of each of the properties of welding metal against Corrosion pit potential/mv

2. Create an Artificial Neural Network model to predict Corrosion resistance.

3. Plot the Mean Squared error and Mean Absolute Percentage error during training.

4. Visualize a 3D Surface Plot and 2D Contour Plot for Corrosion resistance, Rotational Speed, Welding Speed and Axial Force.

5. Visualize and Tri Surface Plot for the N, S and F.

**Task 1: Clean the dataset and Create Visualizations of each of the properties of welding metal against Corrosion pit potential/mv**

Step 1: Import required libraries

Step 2: Import and read the Dataset

Step 3: Clean the dataset using Ms Excel

Step 4: Visualize a bar plot using seaborn of corrosion resistance vs corrosion pit potential/mv

Step 5: Use seaborn again to viuzalie bar plot by tool profile.

Step 6: Do the same for Rotartional Speed, Welding Speed, and Axial Force.

Step 7: Visualize a heatmap for all the properties of the tools and a bar plot for the no. of experiments conducted

**Results**

**Task 2: Create an Artificial Neural Network model to predict Corrosion resistance.**

Step 1: Import required libraries

Step 2: Import and read the Dataset

Step 3: Split datasets in input values(x) and output values(y), data pre-processing for regression

Step 4: Standardize dataset and reshape the dataset

Step 5: Split into train and test

Step 6: Nh=Ns/(α∗(Ni+No)) ie; 30/(2(3+1)) = 3.75 approx 4
* the first hidden layer has 4 nodes and uses relu
* the second hidden layer has 3 nodes and uses relu activation function
* the output layer had one node and uses sigmoid activation function 
* setting input layer with right no. of input features by setting it to 3 for 3 input features

Step 7: Model will be fit with stochastic gradient descent with a learning rate of 0.01 and momentum of 0.9. 

Step 8: Training will be performed for 100 epochs and test set will be evaluated at the end of each epoch 

Step 9: Evaluating the model/ training and testing for mean squared error

Step 10: Plot mean squared error during training.

**Results**

![mean](https://github.com/ShrishtiHore/Corrosion_Resistance/blob/master/mean.png)

![ann](https://github.com/ShrishtiHore/Corrosion_Resistance/blob/master/annn.PNG)

**Task 3: Plot the Mean Squared error and Mean Absolute Percentage error during training.**

Step 1-Step 10 of Task 2 repeated and then follow the same 10th step mean Absolute percentage error.

**Results**

![mean_abs](https://github.com/ShrishtiHore/Corrosion_Resistance/blob/master/mean_abs.PNG)

**Task 4: Visualize a 3D Surface Plot and 2D Contour Plot for Corrosion resistance, Rotational Speed, Welding Speed and Axial Force.**

Step 1: Import required libraries

Step 2: Import and read the Dataset

Step 3: Define the Co-ordinates by meshgrid

Step 4: Set the plot as 3D projection and define it as contour for corrosion resistance.

Step 5: Repeat from Step 3 and 4 for rotational speed, welding speed and Axial force contours.

**Results**

![2D_contour](https://github.com/ShrishtiHore/Corrosion_Resistance/blob/master/Rotational_Speed_2d_contour.png)

![3D Contour](https://github.com/ShrishtiHore/Corrosion_Resistance/blob/master/Rotational_Speed_3d_Surface_plot.png)

**Task 5: Visualize and Tri Surface Plot for the N, S and F.**

Step 1: Import required libraries

Step 2: Import and read the Dataset

Step 3: Transform it to a long format And transform the old column name in something numeric

Step 4: Define the plot as trisurface

Step 5: Set the labels, title and plot the tri surface and Add a color bar which maps values to colors.

**Results**

![tri](https://github.com/ShrishtiHore/Corrosion_Resistance/blob/master/Tri_Surface_plot.png)

