# Ardupilot_worlds

## T1:

        roslaunch imp_wrlds step.launch or roslaunch imp_wrlds sloppy.launch
## T2:

        ../Tools/autotest/sim_vehicle.py -f gazebo-iris
## T3:
        roslaunch apm.launch

# Running multiplot:
> Used plugin: RQT Multiplot
Download: 

    sudo apt install ros-melodic-rqt-multiplot
## In 4th terminal:
 
    rosrun rqt_multiplot rqt_multiplot

> In the multiplot window, open the terrain_drone.xml or slope.xml file that I added in the package.

> Then simply click on the run button on the top right corner of the plotting area.

> Then the terrain will be plotted and as the drone is commanded to move, it’s pose will also be plotted.

………………………………

Python file: scripts/terrain.py & scripts/slope.py (already added in the world launch file, not required to run separately)
