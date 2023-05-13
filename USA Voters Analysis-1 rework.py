#!/usr/bin/env python
# coding: utf-8

# # Loading Modules & Data

# In[1]:


# Importing Modules
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Function to ready the data
def read_data(filename):
    """
    Read CSV data from the given file and return the data as a pandas DataFrame.
    
    Parameters:
        filename (str): Path to the CSV file containing the data to be read.

    Returns:
        pd.DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    # Read the CSV file using pandas and store the data in a DataFrame
    data = pd.read_csv(filename)

    # Return the DataFrame containing the data
    return data


# In[3]:


df = read_data("nonvoters_data.csv")
df.head()


# # Visualization 1

# In[4]:


def create_plot(df, plot_type, features, titles, figsize, subplot_params, ylabel=None):
    """
    Create plots for given features in the DataFrame with specified plot types, titles, and figure sizes.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the data to be plotted.
        plot_type (list of str): The list of plot types to be used for each feature (e.g., "pie", "bar").
        features (list of str): The list of features in the DataFrame to be plotted.
        titles (list of str): The list of titles for each plot.
        figsize (tuple of int): The size of the entire figure (width, height) in inches.
        subplot_params (list of list of int): The list of parameters for each subplot (nrows, ncols, index).
        ylabel (str, optional): The y-axis label for each plot. Default is None.

    Returns:
        None
    """
    
    plt.figure(figsize=figsize)

    # Loop through the features, plot types, titles, and subplot parameters
    for i in range(len(features)):
        plt.subplot(*subplot_params[i])
        df[features[i]].value_counts().plot(kind=plot_type[i])
        plt.title(titles[i])
        plt.ylabel(ylabel if ylabel else "")

    # Display the figure with all subplots
    plt.show()


# In[5]:
