#!/usr/bin/env python

import rospy
import serial

from geometry_msgs.msg import Twist

utf = 'utf-8'

move = {
    "on": 0.8,
    "back": -0.5,
    "left": 1,
    "right": -1
}


def callback(data):
	with serial.Serial('/dev/ttyACM0', 9600, timeout=10) as ser:
		if data.linear.x == move["on"]:
			ser.wite(bytes('w\n', utf))
			rospy.loginfo('Move on')
		elif data.linear.x == move["back"]:
			rospy.loginfo('Move back')
			ser.write(bytes('s\n', utf))

		if data.angular.z == move["left"]:
			rospy.loginfo('Move left')
			ser.write(bytes('a\n', utf))
		elif data.angular.z == move["right"]:
			rospy.loginfo('Move right')
			ser.write(bytes('d\n', utf))
    	
    

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/key_vel", Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()