#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial


class sub(Node):
    def __init__(self):
        super().__init__("node2")
        self.teleop_sub = self.create_subscription(Twist,"/cmd_vel",self.callback,10)
        # self.ser  = serial.Serial('/dev/ttyACM0',57600)
        # self.send_data = 's'
    def callback(self, msg: Twist):
        left_speed = msg.linear.x - (0.6 / 2) * msg.angular.z
        right_speed = msg.linear.x + (0.6 / 2) * msg.angular.z
        self.get_logger().info("left_motor = " + str(left_speed) + " right_motor = " + str(right_speed))
        # self.send_data = "f {} {}\r".format(left_speed,right_speed)
        # self.ser.write(self.send_data.encode("utf-8"))


def main(args=None):
    rclpy.init(args=args)
    node = sub()
    rclpy.spin(node)
    rclpy.shutdown()