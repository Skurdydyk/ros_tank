#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    if data.linear.x == 0.8:
    	rospy.loginfo('Move on')
    elif data.linear.x == -0.5:
    	rospy.loginfo('Move back')
    	
    if data.angular.z == 1:
    	rospy.loginfo('Move left')
    elif data.angular.z == -1:
    	rospy.loginfo('Move right')
    	
    

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/key_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
