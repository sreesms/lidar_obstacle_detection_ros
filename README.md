# lidar_obstacle_detection_ros
2D Lidar ROS package for obstacle detection

This package is for the detection of obstacles nearby the lidars

In this package I have used the rplidar. You can also use another lidar which publishes the /scan topic.

For clone this file use :
$ mkdir -p catkin_ws/src
$ cd catkin_ws/src
#### $ git clone https://github.com/sreesms/lidar_obstacle_detection_ros.git
$ cd .. && catkin_make

##### For using the object detection in rplidar, use the following launch files 
#### $ roslaunch obstacle_detection object_detection_rplidar.launch

##### if you are using another lidar, make sure /scan topic is publishing then run
#### $ roslaunch obstacle_detection object_detection.launch
