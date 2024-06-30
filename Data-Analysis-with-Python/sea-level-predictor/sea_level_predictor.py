import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")
    years_extended = pd.Series(range(1880, 2051))

    # Create first line of best fit
    res = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    plt.plot(years_extended, res.intercept + res.slope * years_extended, 'r', label="First Line of Best Fit")

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    res_2000 = linregress(x=df_2000["Year"], y=df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = pd.Series(range(2000, 2051))
    plt.plot(years_2000, res_2000.intercept + res_2000.slope * years_2000, 'g', label="Second Line of Best Fit")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()