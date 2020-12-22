# Analysis of Orbital Magnetometer Data

Due to familiarity with satllite sensor systems gained through research experience, I decided to analyze data provided by an orbital simulator, allowing for control of data that would greatly ease verifiation of any analysis done. As most of my experience with satellite sensors so far had been assembly and testing of hardware, I was eager for a chance to attempt the type of work that on actual projects had been left to the team who built this simulator in the first place. As such, I had my work cut out for me, trawling through papers and reference texts attempting to figure out what properties of the orbit I could determine from the data available to me. As the assignment was to analyze just the data from a magnetometer, I quickly scrapped the idea of attitude determination of the spacecraft. Kalman filters which can return accurate state vectors require at least two separate input vectors, taking the form of inputs from multiple sensors. In my research I had come accross methods which would allow for attitude determination using just the magnetic field readings. However, these were based on a robust interpolation system with models of the Earth's magnetic field. As such I decided to focus my efforts on information I could determine from pure analysis of the raw data.

# System Simplification

In order to produce a system that was relatively easy to analyze, I set the orbit conditions to be something rarely seen in practice, while still being complex enough to be a realistic system. The simulation accounted for all environmental factors  except differential drag and solar pressure. These effects can generally be ignored, especially since I set the satellite to be spin-stabilized. The orbit I selected was one along the Earth's equator (celestial equator in Fig. 1) As seen in 

<p align="center">
 <img width="300" alt="orbitdg" src="https://github.com/ubsuny/data-analysis-final20/tree/main/Orbital_Magnetometer/images/orbitdiagram.png">  
<p align="center">Figure 1. Orbit diagram.
