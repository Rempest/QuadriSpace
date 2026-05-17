import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3, Quaternion
 
 
class geometry_dimension(Node):
    def __init__(self):
        super().__init__('geometry_node')
        self.vector_publisher = self.create_publisher(Vector3, 'vector_topic', 10)
        self.vector_subscription = self.create_subscription(
            Vector3, 'vector_topic', self.vector_callback, 10
        )

        self.quat_publisher = self.create_publisher(Quaternion, 'quaternion_topic', 10)
        self.quat_subscription = self.create_subscription(
            Quaternion, 'quaternion_topic', self.quaternion_callback, 10
        )
 
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.angle = 0.0 
 
    def timer_callback(self):
        vec = Vector3()
        vec.x = -1.5
        vec.y = 2.5
        vec.z = 7.0
        self.vector_publisher.publish(vec)
        self.get_logger().info(
            f'[Vector3 sent]  x={vec.x}, y={vec.y}, z={vec.z}'
        )
 
        # -- publish quaternion representing rotation around Z-axis --
        # q = (sin(θ/2)*axis_x, sin(θ/2)*axis_y, sin(θ/2)*axis_z, cos(θ/2))
        # Rotation around Z: axis = (0, 0, 1)
        half = self.angle / 2.0
        quat = Quaternion()
        quat.x = 0.0
        quat.y = 0.0
        quat.z = math.sin(half)
        quat.w = math.cos(half)
        quat = self._normalize_quaternion(quat)
        self.quat_publisher.publish(quat)
        self.get_logger().info(
            f'[Quaternion sent] x={quat.x:.4f}, y={quat.y:.4f}, '
            f'z={quat.z:.4f}, w={quat.w:.4f}  (angle={math.degrees(self.angle):.1f}°)'
        )
 
        self.angle += 0.1  
    def vector_callback(self, msg: Vector3):
        self.get_logger().info(
            f'[Vector3 recv]  x={msg.x}, y={msg.y}, z={msg.z}'
        )
 
    def quaternion_callback(self, msg: Quaternion):
        angle = 2.0 * math.acos(max(-1.0, min(1.0, msg.w)))
        self.get_logger().info(
            f'[Quaternion recv] x={msg.x:.4f}, y={msg.y:.4f}, '
            f'z={msg.z:.4f}, w={msg.w:.4f}  (angle={math.degrees(angle):.1f}°)'
        )
 
    @staticmethod
    def _normalize_quaternion(q: Quaternion) -> Quaternion:
        norm = math.sqrt(q.x**2 + q.y**2 + q.z**2 + q.w**2)
        if norm < 1e-10:
               q.w = 1.0
               return q
          q.x /= norm
          q.y /= norm
          q.z /= norm
          q.w /= norm
           return q
    def main(args = None)
       rclpy.init(args=args)
       node = geometry_dimension()
       try:
              rclpy.spin(node)
       except KeyboardInterrupt:
              pass
       finally:
              node.destroy_node()
              rclpy.shutdwon()
   if __name__ == '__main__':
          main()
           
