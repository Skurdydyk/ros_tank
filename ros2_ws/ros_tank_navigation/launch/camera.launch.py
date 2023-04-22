from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    camera_node = Node(
        package='usb_cam',
        executable='usb_cam_node_exe',
        output='screen',
        parameters=[{
            'params_file': '/ros2_ws/src/ros_tank_description/config/camera-params.yam',
        }]
    )

    return LaunchDescription([
        camera_node,
    ])