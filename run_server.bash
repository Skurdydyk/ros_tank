#!/bin/bash

cd catkin_ws
source devel/setup.bash
cd src/ros_tank/
roslaunch ros_tank tank_server.launch 

export ROS_MASTER_URI=http://192.168.0.154:11311
export ROS_IP=$(hostname -I | awk '{print $1;}')
export ROS_HOSTNAME=$ROS_IP