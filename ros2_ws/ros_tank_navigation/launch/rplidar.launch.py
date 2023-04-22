from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    rplidar_node = Node(
        package='rplidar_ros',
        executable='rplidar_composition',
        output='screen',
        parameters=[{
            'serial_port': '/dev/ttyUSB0',
            'frame_id': 'link_laser_scan',
            'angle_compensate': True,
            'scan_mode': 'Standard'
        }]
    )
    
    return LaunchDescription([
        rplidar_node
    ])