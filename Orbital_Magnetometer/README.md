# Orbital_Magnetometer

## Project Background

The original intent for this project was to use the PhyPhox phone experiment to output raw data measurements from the phone's magnetometer. After some experimenting with this data gathering method, I realized that without putting a significant amount of time into creating a setup that constrains the phone's motion in a consisten way, and allows for some method of checking whether my analysis was even reasonable. Thus, I decided to employ an orbital simulator I was somewhat familiar with from research experience in order to provide good data sets for analysis. The simulator is heavily ITAR restricted, however I am able to provide raw data sets of magnetometer readings, as they are generated by pulling data from the IGRF and adding a layer of experimentally determined sensor noise over it. 

## Contents 

+ `Data_Sets` contains `.csv` files with data from simulations with various runtimes and orbit eccentricities
+ `images` contains data plots pulled directly from the simulator, just for sanity checking plots created in the jupyter notebooks
+ `src` contains the three `.py` files containing algorithms used for data analysis
+ `Data Analysis.ipynb` is a shell for carrying out and displaying data analysis for the provided data sets using the methods contained in src
+ `Unit Testing Notebook.ipynb` is a shell for carrying out trivial, easily verifiable tests of all written algorithms
+ `Wiki` details methodology and decisions made for this project
