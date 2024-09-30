#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class move_bot:
    def __init__(self) -> None:
        rospy.init_node("move_node", anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber("/nadeef_command", String, self.callback)
    def callback(self, command):
        rospy.loginfo("Command received: " + command.data)

        array = command.data.split()
        direction = array[0]
        if len(array) == 2:
            value = array[1]
        
        velocity = Twist()

        if direction.lower()=='forward':
            velocity.linear.x = float(value)
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='backward':
            velocity.linear.x = float(0-float(value))
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='left':
            velocity.angular.z = float(value)
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='right':
            velocity.angular.z = float(0-float(value))
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
        elif direction.lower()=='stop':
            velocity.linear.x = 0.0
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
            velocity.angular.z = 0.0
        else:
            rospy.loginfo("Wrong command")
        try:
            self.pub.publish(velocity)
        except:
            rospy.loginfo("AN ERROR OCCURED")
if __name__=='__main__':
    node = move_bot()
    rospy.spin()