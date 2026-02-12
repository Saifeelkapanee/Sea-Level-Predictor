# %%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats as stats

# %%
df =pd.read_csv("/mnt/Study/FreeCodeCampTasks/Sea-Level-Predictor/epa-sea-level.csv")

# %%
fig , axis=plt.subplots()
axis.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])
axis.set_title("Rise in Sea Level")
axis.set_xlabel("Year")
axis.set_ylabel("CSIRO Adjusted Sea Level")
fig.savefig("sea_level_plot.png")



# %%
x = df["Year"]
y = df["CSIRO Adjusted Sea Level"]
slope, intercept,*other= stats.linregress(x, y)
years_extended = np.arange(x.min(), 2051)  
sea_level_pre = intercept + slope * years_extended

#scatter plot of the original data and the best fit line
fig, axis = plt.subplots()
axis.scatter(x, y)  
axis.plot(years_extended, sea_level_pre, color="black", label="Best Fit Line")

axis.set_title("Rise in Sea Level")
axis.set_xlabel("Year")
axis.set_ylabel("Sea Level (inches)")
fig.savefig("sea_level_plot_with_line_1.png")

# %%
filtered = df[df["Year"] >= 2000]
x_filtered = filtered["Year"]
y_filtered = filtered["CSIRO Adjusted Sea Level"]

slope_filtered, intercept_filtered,*other= stats.linregress(x_filtered, y_filtered)
years_filtered_extended = np.arange(2000, 2051)
sea_level_pre_filtered = intercept_filtered + slope_filtered * years_filtered_extended
fig, axis = plt.subplots()
axis.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="black", label="Data")

years_extended = np.arange(df["Year"].min(), 2051)
sea_level_pre = intercept + slope * years_extended
axis.plot(years_extended, sea_level_pre)
axis.plot(years_filtered_extended, sea_level_pre_filtered)


axis.set_title("Rise in Sea Level")
axis.set_xlabel("Year")
axis.set_ylabel("Sea Level (inches)")
fig.savefig("sea_level_plot_with_line_2.png")




