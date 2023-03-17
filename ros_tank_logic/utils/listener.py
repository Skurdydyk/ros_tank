#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate = 9600

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    vertical = float(data.angular.z)
    horizontal = float(data.linear.x)

    if vertical == 1.0:
        rospy.loginfo("Left")
	ser.wtrite(b"a")
    elif vertical == -1.0:
        rospy.loginfo("Right")
	ser.wtrite(b"d")
    elif horizontal == 0.5:
        rospy.loginfo("Forward")
	ser.wtrite(b"w")
    elif horizontal == -0.5:
        rospy.loginfo("Back")
	ser.wtrite(b"s")
    elif horizontal == 0.0 and data.angular.z == 0.0:
        rospy.loginfo("Stop")
	ser.wtrite(b"x")

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == "__main__":
    listener()
