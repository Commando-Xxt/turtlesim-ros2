import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.srv import SetPen, TeleportAbsolute
import math
import time

class Square(Node):
    def __init__(self):
        super().__init__('draw_square')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # make red pen and teleport to center facing east
        self.cli_pen = self.create_client(SetPen, '/turtle1/set_pen')
        self.cli_tp = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.cli_reset = self.create_client(Empty, '/reset')
        while not self.cli_pen.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting for turtlesim...')
        self.cli_reset.call_async(Empty.Request())
        self.cli_pen.call_async(SetPen.Request(r=255, g=0, b=0, width=4, off=0))
        self.cli_tp.call_async(TeleportAbsolute.Request(x=5.5, y=5.5, theta=0.0))
        self.timer = self.create_timer(0.01, self.tick)
        self.step = 0
        self.edge_time = 1.8  # tune if needed
        self.turn_time = 1.6
        self.t0 = time.time()

    def tick(self):
        msg = Twist()
        t = time.time() - self.t0
        if self.step >= 4:
            self.pub.publish(Twist())  # stop
            rclpy.shutdown()
            return
        if 0.0 <= t < self.edge_time:
            msg.linear.x = 1.5
            msg.angular.z = 0.0
        elif self.edge_time <= t < self.edge_time + self.turn_time:
            msg.linear.x = 0.0
            msg.angular.z = math.pi/2.0 / self.turn_time
        else:
            self.step += 1
            self.t0 = time.time()
        self.pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(Square())

if __name__ == '__main__':
    main()
