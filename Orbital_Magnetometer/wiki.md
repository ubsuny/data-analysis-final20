# Analysis of Orbital Magnetometer Data

Due to familiarity with satllite sensor systems gained through research experience, I decided to analyze data provided by an orbital simulator, allowing for control of data that would greatly ease verifiation of any analysis done. As most of my experience with satellite sensors so far had been assembly and testing of hardware, I was eager for a chance to attempt the type of work that on actual projects had been left to the team who built this simulator in the first place. As such, I had my work cut out for me, trawling through papers and reference texts attempting to figure out what properties of the orbit I could determine from the data available to me. As the assignment was to analyze just the data from a magnetometer, I quickly scrapped the idea of attitude determination of the spacecraft. Kalman filters which can return accurate state vectors require at least two separate input vectors, taking the form of inputs from multiple sensors. In my research I had come accross methods which would allow for attitude determination using just the magnetic field readings. However, these were based on a robust interpolation system with models of the Earth's magnetic field. As such I decided to focus my efforts on information I could determine from pure analysis of the raw data.

# System Simplification

In order to produce a system that was relatively easy to analyze, I set the orbit conditions to be something rarely seen in practice, while still being complex enough to be a realistic system. The simulation accounted for all environmental factors  except differential drag and solar pressure. These effects can generally be ignored, especially since I set the satellite to be spin-stabilized. The orbit I selected was one along the Earth's equator (celestial equator in Fig. 1). This will remove any north-south data variation. Spin-stabilizing the spacecraft was done through taking a face of the satellite and fixing it to a vector that stays pointed along the same axis across the entire orbit and stays parallel to the equitorial plane, along with zeroing angular rotation along all three axes (variable parameters in the simulation). This trivially leads to an expectation of a maximum value of the x-axis measurements on one side of the planet, a minimum on the other, and periodic variations in the y and z data as the satellite orbits. By reducing the complexity of the system to be analyzed, we can ensure that the data will (hopefully) already be in a sinusoid. One of the only parameters that wasn't fixed was the eccentricity of the orbit, which governs how elliptical it is. 
 
<p align="center">
 <img width="500" alt="orbitdg" src="https://github.com/ubsuny/data-analysis-final20/blob/main/Orbital_Magnetometer/images/orbitdiagram.png?">  
<p align="center">Figure 1. Orbit diagram.


# Raw Data Plots

The following diagrams were generated directly from the orbital simulator. The contain the same data as the ones generates from the same data in analysis, however I find these to display the noisiness of the measurements a tiny bit better. Fig. 2 shows the raw data plotted for a zero eccentricity orbit propagated tbrough 900 minutes, or about 10 orbits of the average 90 minute L.E.O. orbit. The actual orbital period may be lesser or greater than this value, and the number of orbits completed in the simulation time will vary accordingly.  A better data resolution can be gained from simply running the simulation for longer, such as the 100 orbits in Fig. 3.
<p align="center">
 <img width="500" alt="orbit10" src="https://github.com/ubsuny/data-analysis-final20/blob/main/Orbital_Magnetometer/images/e=0_10O_axis.png?">  
<p align="center">Figure 2. 10 Orbit raw readings.
 
 
 <p align="center">
 <img width="500" alt="orbit10" src="https://github.com/ubsuny/data-analysis-final20/blob/main/Orbital_Magnetometer/images/e=0_100O_axis.png?">  
<p align="center">Figure 3. 100 Orbit raw readings.
 
There is very clear sinusoidal behavior in the data sets. However, to clean it up even further we can work with the scalar magnitude of the field, given by <img src="https://render.githubusercontent.com/render/math?math=Bmag= \sqrt((x)^2+(y)^2+(z)^2)">. This should make periodic behavior even more easily distinguishable. Indeed, the magnitude plot for the 10 orbit zero eccentricity shows an already almost perfect sinusoid in Fig. 4. It also displays artifacts of the shape of the magnetic field (something that will come in handy later on).

  <p align="center">
 <img width="500" alt="orbit10" src="https://github.com/ubsuny/data-analysis-final20/blob/main/Orbital_Magnetometer/images/e=0_10O_magnitude.png?">  
<p align="center">Figure 1. 10 Orbit magnitude data.
 
 
 # Algorithms
 
I pause the discussion of the physics to discuss the three algorithms I employed in order to perform the necessary data analysis. The code resides in the `src` folder. The first algorithm I employed was a sine function fit. It uses a fast-fourier transform on the data to get an initial guess for the function, and then adjusts the fit using `scipy.optimize.curve_fit`. It returns a python dictionary containing different attributes of the fitted function. The second algorithm is a data smoother. It is a simple implementation of a triangular moving average in order to produced the smoothed data. It generally functions better than the provided filters in the `scipy.signal` module. However, data type errors occasionally prevented full use. The final agorithm is one that generally requires well-smoothed data. This is the peak finder algorithm. Taking advantage of the fact that it will be dealing with nice and smooth data sets, the functionality is relatively simple. A massive if statement parses the input; first it identifies all local maxima, and then refines based on the necessary peak width that is given as an input. While slightly computatoionally expensive, it allows user selection of a statistically peak width. 

# Data Analysis
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
