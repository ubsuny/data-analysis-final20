# Final Project

A repository for the final project of PHY 410/505 Computational Physics I.  

All details, data, figures and codes for the gyroscope experiment are included here. The experiment is based on a cellphone application `phyphox`, which could measure angular velocity data via the gyroscope sensor inside the cellphone. 

# Contents

+ `data` folder: All data files are included in this folder in formats of `.csv` and `.xls`. Same file names with different suffixes mean they're the same data. I took several measurement and use `z_cir` and `z_acc` for data analysis.
+ `codes` folder: This folder has all pthon files required for this project. The `read_data` file is for read raw data from csv files and `fitting` file includes the fitting algorithms and a function to calculate χ square values. The `unittest` file is for testing all above functions automatically once it's run. All files have docstrings and comments to describe details and utilities.
+ `figures` folder: Including all photographs for wiki. 
+ `gyroscope` jupyter notebook: It serves as a shell to analyze data via algorithms in the `codes` folder, compare fitting data with original data and discuss fitting results.
+ `wiki` file: It elaborates the motivation of this project, introduction to the gyroscope, some utilities of `phyphox`, physics and details of the experiment.
