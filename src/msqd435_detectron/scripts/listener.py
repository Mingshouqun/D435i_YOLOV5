#!/usr/bin/env python
#coding=utf-8


import rospy
from msqd435_detectron.msg import Num

def callback(data):
    rospy.loginfo("X轴:%f,y轴:%f,距离:%f",msg.x,msg.y,msg.z)
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', Num, callback,queue_size=10)
    rospy.spin()
