# Tank ros project

Tank launch project:
- usb cam package
- lidar package

![Selection_096](https://user-images.githubusercontent.com/23004657/209576988-321a2a82-18bd-4550-98bb-9a9118b5310c.png)


Command to check available cameras:
ls /dev | grep video*

Then change value param for tank launcher:
<param name="video_device" value="/dev/video4" />

Command to check available lidar:
ls -l /dev |grep ttyUSB

sudo chmod 666 /dev/ttyUSB0


ros2 launch ros_tank spawn.launch.py
ros2 run joint_state_publisher_gui joint_state_publisher_gui

roslaunch my_moviet demo.launch