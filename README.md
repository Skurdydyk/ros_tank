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

sudo chmod 666 /dev/ttyUSB0

Commands for starting the project:

ros2 launch ros_tank_logic ros_tank_sim.launch.xml
<!-- Spawn world in gazebo running sim -->
- ros2 launch ros_tank_gazebo start_world.launch.py
<!-- Publish URDF file in robot_description topic and launch rviz -->
- ros2 launch ros_tank_logic ros_tank_rviz.launch.py
<!-- Read robot_description and spawn in gazebo running sim -->
- ros2 launch ros_tank_gazebo spawn_robot.launch.py

ros2 launch ros_tank_logic ros_tank.launch.xml
ros2 launch ros_tank_control ros_tank_control_diff.launch.py

ros2 run teleop_twist_keyboard teleop_twist_keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=/diff_cont/cmd_vel_unstamped

ros2 run joint_state_publisher_gui joint_state_publisher_gui
