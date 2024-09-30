#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class taking_command:
    def __init__(self) -> None:
        rospy.init_node("command_node", anonymous=True)
        self.pub = rospy.Publisher("/nadeef_command", String, queue_size=1)
    def send(self, command):
        self.pub.publish(command)
        rospy.loginfo("Command: " + command)
    def run(self):
        rospy.loginfo("Command node is running")
        while not rospy.is_shutdown():
            command = input("Enter command: ")
            self.send(command)
            rospy.sleep(1)

if __name__=='__main__':
    node = taking_command()
    node.run()