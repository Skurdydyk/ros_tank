Tank launch project:
- usb cam package
- lidar package

Command to check available cameras - ls /dev | grep video*\
Then change value param for tank launcher:
<param name="video_device" value="/dev/video4" />

Command to check available lidar - ls -l /dev |grep ttyUSB
sudo chmod 666 /dev/ttyUSB0