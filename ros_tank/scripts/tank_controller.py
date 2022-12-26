#!/usr/bin/env python

import rospy
import serial

from geometry_msgs.msg import Twist

utf = 'utf-8'

move = {
    "on": 0.5,
    "back": -0.5,
    "left": 1,
    "right": -1,
	"stop": 0
}
PORT = '/dev/ttyACM0'
TOPIC_CMD_VEL = '/cmd_vel'

def callback(data):
	with serial.Serial(PORT, 9600, timeout=10) as ser:
		if data.linear.x == move["on"]:
			rospy.loginfo('Move on')
			ser.write(bytes('w\n', utf))
		elif data.linear.x == move["back"]:
			rospy.loginfo('Move back')
			ser.write(bytes('s\n', utf))

		if data.angular.z == move["left"]:
			rospy.loginfo('Move left')
			ser.write(bytes('a\n', utf))
		elif data.angular.z == move["right"]:
			rospy.loginfo('Move right')
			ser.write(bytes('d\n', utf))

		elif data.linear.x == move["stop"] and data.angular.z == move["stop"]:
			rospy.loginfo('Stop')
			ser.write(bytes('x\n', utf))
    	
    

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.loginfo('Init_node listener')
	rospy.Subscriber(TOPIC_CMD_VEL, Twist, callback)
	rospy.loginfo('Create subscriber')
	
	rospy.spin()

if __name__ == '__main__':
	listener()
