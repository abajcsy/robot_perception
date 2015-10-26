robot_perception
=============

Code is written in Python and is using [ROS Indigo].

Dependencies
-------
In order to run all the functionality of this project, clone the following projects into your ros workspace: 
* [ar_track_alvar]
* [experiment_calib]

If you're using catkin_make, navigate to the /src directory in your ros workspace and type 'git clone' followed by the http://... website to each of the following github repositories. Then, navigate up one folder level to your ros workspace and type 'catkin_make'.

Example:
```bash
cd ~/ros_workspace/src
git clone https://github.com/abajcsy/coop_pcl
cd ..
catkin_make
```

Extra Info
-------
Developed during Fall 2015 as part of CMSC396H - Honors Research Seminar at the University of Maryland College Park. 


[ar_track_alvar]: http://wiki.ros.org/ar_track_alvar
[experiment_calib]: https://github.com/abuchan/experiment_calib 
[ROS Indigo]: http://wiki.ros.org/indigo
