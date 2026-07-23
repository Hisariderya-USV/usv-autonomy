import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64


class ThrusterTest(Node):

    def __init__(self):
        super().__init__("thruster_test")

        self.left_pub = self.create_publisher(
            Float64,
            "/wamv/thrusters/left/thrust",
            10)

        self.right_pub = self.create_publisher(
            Float64,
            "/wamv/thrusters/right/thrust",
            10)

        self.timer = self.create_timer(0.1, self.publish_thrusters)

    def publish_thrusters(self):

        msg = Float64()

        msg.data = 30.0

        self.left_pub.publish(msg)
        self.right_pub.publish(msg)


def main():

    rclpy.init()

    node = ThrusterTest()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
