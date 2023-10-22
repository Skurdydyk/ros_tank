# Tank ros project

Tank launch project packages:
- ros_tank_logic
- ros_tank_gazebo
- ros_tank_navigation
- ros_tank_description

![Selection_096](https://user-images.githubusercontent.com/23004657/209576988-321a2a82-18bd-4550-98bb-9a9118b5310c.png)


Command to check available cameras:
ls /dev | grep video*

Then change value param for tank launcher:
<param name="video_device" value="/dev/video4" />

Command to check available lidar:
ls -l /dev |grep ttyUSB

sudo chmod 666 /dev/ttyUSB0 or /dev/ttyACM0

Commands for starting the project:

1. download file - arduino/ros_tank.ino to arduino


2. terminal jetson nano
./run_jetson.bash
cd ros_tank 
ros2 launch ros_tank_control ros_tank_control_diff.launch.py

3. terminal PC
./run.bash
ros2 launch ros_tank_logic ros_tank_rviz.launch.py

4. terminal PC
./exec.bash 
ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=/diff_cont/cmd_vel_unstamped


For simulation:

ros2 launch ros_tank_logic ros_tank_sim.launch.xml
<!-- Spawn world in gazebo running sim -->
- ros2 launch ros_tank_gazebo start_world.launch.py
<!-- Publish URDF file in robot_description topic and launch rviz -->
- ros2 launch ros_tank_logic ros_tank_rviz.launch.py
<!-- Read robot_description and spawn in gazebo running sim -->
- ros2 launch ros_tank_gazebo spawn_robot.launch.py


run joint state publisher node:
ros2 run joint_state_publisher_gui joint_state_publisher_gui

run lidar node:
ros2 launch rplidar_ros view_rplidar.launch.py 
ros2 launch rplidar_ros rplidar.launch.py 

ros2 launch ros_tank_navigation rplidar.launch.py
ros2 launch ros_tank_navigation camera.launch.py

ros2 launch ros_tank_control ros_tank.xml

checking camera:
sudo apt-get install v4l-utils
v4l2-ctl --list-devices

run camera node:
ros2 run usb_cam usb_cam_node_exe --ros-args --params-file /ros2_ws/src/ros_tank_description/config/camera-params.yaml


ros2 topic pub --once /forward_position_controller/commands std_msgs/msg/Float64MultiArray "
layout:
 dim: []
 data_offset: 0
data:
 - 1
 - 1"
