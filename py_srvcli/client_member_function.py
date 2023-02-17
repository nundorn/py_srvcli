import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.pub = self.create_publisher(String, 'my_topic', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # Send HTTP GET request to external API
        response = requests.get('https://webhook.site/5ece8a22-46ae-4566-8d73-4ef71d230285')

        # Log response data to terminal
        self.get_logger().info('Received response: %s' % response.text)

        # Publish response to ROS topic
        msg = String()
        msg.data = response.text
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    minimal_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
