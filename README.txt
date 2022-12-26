Tank launch project:
- usb cam package
- lidar package

Command to check available cameras:
ls /dev | grep video*

Then change value param for tank launcher:
<param name="video_device" value="/dev/video4" />

Command to check available lidar:
ls -l /dev |grep ttyUSB

sudo chmod 666 /dev/ttyUSB0


![alt text](https://github.com/Skurdydyk/ros_tank/blob/4e855116cd1fe3d0dce81566ee47a814646cd3e8/Selection_094.png)
