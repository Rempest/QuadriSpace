import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
class GeometryNode(Node):
       def __init__(geo):
           super().__init__('vector')
           geo.publisher = geo.create_publisher(Vector3, 'vector_topic', 10)
           geo.subscription = geo.create_subscription(Vector3, 'vector_topic', geo.listener_callback, 10)
           geo.timer = geo.create_timer(1, geo.timer_callback)
       def timer_callback(geo):
           msg = Vector3()
           msg.x = -1.5
           msg.y = 2.5
           msg.z = 7.0
           geo.publisher.publish(msg)
           geo.get_logger().info(f'send: {msg.x}, {msg.y}, {msg.z}')
       def listener_callback(geo, msg: Vector3):
           geo.get_logger().info(f'gotten: {msg.x}, {msg.y}, {msg.z}')
def main(args = None):
            rclpy.init(args = args)
            geo = GeometryNode()
            rclpy.spin(geo)
            geo.destroy_node()
            rclpy.shutdown()
if __name__ == '__main__':
    main()

