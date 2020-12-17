### Welcome to the Gyroscope wiki!
### Guangpeng (Carl) Xu

***
## Introduction  

A gyroscope is a commonly-used device for measursing variations of orientation and angular velocity. [1] It's based on conservation of angular momentum: the rotation axis of a rotating object does not change its direction unless an external force is applies. It was first invented by [J.Foucault](https://en.wikipedia.org/wiki/L%C3%A9on_Foucault), a French physicist who was engaging in a research on Earth's Rotation in 1850. He combined two Greek words "gyro" and "skopein" to name the novel device.

A gyroscope usually consists of a wheel mounted into several gimbals to rotate about a single axis. A set of three orthogonally-mounted gimbals allow the wheel to have an orientation remaining independent of the orientation in space. The rotor on the wheel is constrained to spin about an axis, which is always perpendicular to the axis of the inner gimbal. And while the rotor possesses angular momentum which is conserved, the spinning object tends to resist any change in its axis of rotation, since a change in orientation will result in a change in angular momentum.

Based on a gyroscope, the angular velocity can be calculated by measuring the [Coriolis force](https://en.wikipedia.org/wiki/Coriolis_force). [2] A two-mass system moving continuously in opposite direction is utilized to experience Coriolis force under angular rotation. Accoriding to the right-hand rule, masses will have opposite directions of Coriolis forces and the final value is taken by finding the difference of measured acceleration of the Coriolis force (an [accelerometer](https://en.wikipedia.org/wiki/Accelerometer) might need to be involved). Ideally, the accelerations are in the opposite directions as well so subtracting them will get a summation and neglect any other undesired forces acting on the system.

## Methods  

In this project, a useful mobile application entitled [phyphox](https://phyphox.org/) is utilized to acquire data. This app provides different kinds of physics experiments and several of them are gyroscope-involved: "inclination", "Centrifugal acceleration", "roll", etc. The one will be studied for this project is simply called "gyroscope", which just gives the raw data from the phone’s gyroscope as a rotation rate in rad/s. [3] With the phyphox experiment running, the real-time data is shown and temporal evolution is recoreded simultaneously. Also, after the measurement, you can choose the file format and data type for output.  



Figure 1. A phyphox interface for the gyroscope experiment. (photoshopped to replace Chinese with English)

Fig.1 shows us how an interface looks like, where three subplots represent three components along x, y and z direction of the angular velocity, respectively. There're several other interfaces to show the total angular velocity, real-time data and all components in one plot, etc. In this experiment, axes are fixed to be based on for measuring angular velocities along different directions and they're with respect to the cellphone screen, as shown in the following figure.


![](https://phyphox.org/wp-content/uploads/2016/04/coordinate_system.jpg)  
Figure 2. Coordinate system of Phyphox. [4]  

From fig.2, we can see that the z axis is pointing out of the screen perpendicularly. The x axis points to the right looking at the screen in portrait (vertical) orientation. The y axis points upwards along the long side of the phone. [4] And the original point is set at the geometrical center of the screen.


## Set up  

For measurement, it's possible to simply wave a cellphone in the air with the Phyphox running. However, to get non-trivial (periodic) data makes it a difficult task as a cellphone usually has a cuboid shape and needs to be rotated steadily. I did spend an amount of time and work on this and tried several methods:  
- barely use my hands to rotate the mobile :   
It'll generate huge errors and is hard to maintain the motion state due to its shape.
- fix the phone onto a office chair then rotate the chair :  
It works but not very well because of the resistance; also it cannot have a higher speed, depending on how fast you can rotate the office chair.
- ~~tie my phone to a rope and swing it~~ :  
The phone will have weird spin during rotating the rope which ruins the data.
- ~~tape my phone to the tire then drive the car at a low speed~~ :  
This actually works but **it's also dangerous**. My phone was close to be smashed so it's not recommended.
- [✔] tape my phone to an ab wheel roller:
It went smoothly, is relatively easy to operate and guarantees a steady rotation.  

Figure 3. Experimental set up based on a cellphone and an ab wheel roller.

As shown in Fig.3, the half of axle is removed from the roller to allow the phone taped on the side of it. Then I tape the phone tightly at the center of the roller, put the other half axle through the roller then I can control the angular velocity by adjusting the speed of the roller (the roller can also make a turn). Recalling from Fig.2, now z axis is pointing out from the mobile screen while x and y axes are in the side plane of the roller.

## Experiment I

The first experiment is to simulate that the phone has a constant angular acceleration along the z direction while there's no motion along the x and y direction. Therefore, the z component of angular velocity is linear with respect to time and other two components are ideally zero. 

Figure 4. Trajectory of the roller in Experiment I.

In Fig.4, the roller accelerates and rolls along a straight line which drives the phone to rotate with it. This is implemented by my hand holding the roller axle and applying a constant force, assuming the resistance force is constant, the phone will be spinning with a constant angular acceleration. The following figure simply derives the physics. 

Figure 5. Derivation to prove the phone has a constant angular acceleration.

Then we're able to write following relations as expected results:  
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega_x=0)
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega_y=0)
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega_z=\alpha*t)
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega_{total}=\alpha*t)  


## Experiment II

To better testify the algorithm, I set up a second experiment as shown in Fig.6, with the roller now rotating around the tip of its axle while rolling as a normal roller. A flat ground floor with a red marked dot is needed to minimize systematic errors and monitor the position of the rotation axle to be fixed.  

Figure 6. Trajectory of the roller in Experiment II. The red dot is the projection of the roation axle on the floor.  

The spinning of the phone generates angular velocity components along z direction; meanwhile the precession rises x and y components. Since now both precession and rotation are involved, based on rigid body rotation theorem, we derived relations between components of angular velocity and actual angular velocities, as in Fig.7.

Figure 7. Derivation x and y components of angular velocity.

Thus, we have all components of angular velocity as:  
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega_x=\omega_p*sin(\omega_s*(t+\phi)))
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega_y=\omega_p*cos(\omega_s*(t+\phi)))
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega_z=\omega_s)
-  ![](https://latex.codecogs.com/gif.latex?\\-\omega=\sqrt{\omega_s^2+\omega_p^2})

where ![](https://latex.codecogs.com/gif.latex?\\-\omega_p) is the precession angular velocity while ![](https://latex.codecogs.com/gif.latex?\\-\omega_s) is the spin angular velocity; ![](https://latex.codecogs.com/gif.latex?\\-\phi) is the phase depending on the initial position.

## Results

For Experiment I, using the [least square regression analysis](https://en.wikipedia.org/wiki/Least_squares), we get a linear fit for the z component which is not satisfying and has a large chi square value. In the contrast, a quadratic fitting function corresponds the raw data plot and this indicates the experiment object might actually have an unsteady angular accelerating motion. And it could be caused by the increasing force I applied to balance the increasing friction as speeding up.

For Experiment II, we first use the algorithm to fit three components and the total angular velocity since trigonometric functions could be expanded as polynomials. Instead of analyzing the whole data, we truncate a part of it to minimize jittering and other factors affecting fitting analysis. The x and y components fitting works pretty well while the z component and total angular velocity have large chi square values, results from large jittering amplitude due to experimental operation issue. It means either the ground is not flat or the precession trajectory is not accurately circle. Based on fitting results, rotation and precession anguar velocities can be determined: ![](https://latex.codecogs.com/gif.latex?\\-\omega_p=2.5418rad/s) and ![](https://latex.codecogs.com/gif.latex?\\-\omega_s=4.1824rad/s).

Additionally, we directly use the [leastsq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html) function in scipy library to fit x and y data. With an appropriate initial guess, we calculate the rotation and precession anguar velocities from fitting parameters: ![](https://latex.codecogs.com/gif.latex?\\-\omega_p=2.5033rad/s) and ![](https://latex.codecogs.com/gif.latex?\\-\omega_s=4.0767rad/s). As we can see results from both algorithms are close to each other which illustrates our algorithm successfully fits the original data.

## Outlook
For future work (if interested), we could measure more data from different models and integrate data with respect to time to get angular variation. In my opinion, the hardest part of this experiment is the implementation; due to the shape and the cost of a cellphone, the feasibility is limited. And from the programming point of view, it's definitely worth a try to filter out the noise in raw data which will be very useful for fitting. 


## Reference
[1] https://en.wikipedia.org/wiki/Gyroscope#History  
[2] https://www.youtube.com/watch?v=ti4HEgd4Fgo  
[3] https://phyphox.org/experiment/gyroscope/  
[4] https://phyphox.org/sensors/