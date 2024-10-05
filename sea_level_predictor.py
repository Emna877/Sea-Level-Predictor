import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'], label='Sea level')

    # Create first line of best fit
    # Perform linear regression on the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Predict sea level for years 1880-2050
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred = intercept + slope * years_extended
    # Plot the first regression line
    plt.plot(years_extended, sea_level_pred, 'r', label='Fitted Line 1880-2050')

    # Create second line of best fit
    # Filter data from 2000 onwards
    recent_df = df[df['Year'] >= 2000]
    # Perform linear regression for data from 2000 onwards
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    # Predict sea level for years 2000-2050
    recent_years_extended = pd.Series(range(2000, 2051))
    sea_level_recent_pred = intercept_recent + slope_recent * recent_years_extended
    # Plot the second regression line
    plt.plot(recent_years_extended, sea_level_recent_pred, 'g', label='Fitted Line 2000-2050')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()