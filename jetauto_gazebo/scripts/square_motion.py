#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move(pub, linear_x=0.0, linear_y=0.0, angular_z=0.0, duration=1.0):
    msg = Twist()
    msg.linear.x = linear_x
    msg.linear.y = linear_y
    msg.angular.z = angular_z
    pub.publish(msg)
    rospy.sleep(duration)
    pub.publish(Twist())
    rospy.sleep(1)

if __name__ == '__main__':
    rospy.init_node('square_pattern_node')
    pub = rospy.Publisher('/jetauto_controller/cmd_vel', Twist, queue_size=10)
    rospy.sleep(2)

    for i in range(2):
        move(pub, linear_x=0.2, duration=5)
        move(pub, linear_y=0.2, duration=5)
        move(pub, angular_z=-1.57, duration=2)
        move(pub, linear_x=-0.2, duration=5)
        move(pub, linear_y=-0.2, duration=5)
        move(pub, angular_z=1.57, duration=2)

    rospy.loginfo("Finished moving in square.")
