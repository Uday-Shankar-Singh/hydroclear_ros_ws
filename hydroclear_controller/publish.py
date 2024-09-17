#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class publish_node(Node):
    def __init__(self):
        super().__init__("node1")
        self.counter = 0
        self.create_timer(0.5,self.timer_callback)
        #self.get_logger().info("Activated Parthiv")
    def timer_callback(self):
        self.get_logger().info("Activated Partiv"  + str(self.counter))
        self.counter +=1


def main(args=None):
    rclpy.init(args=args)
    node = publish_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()    