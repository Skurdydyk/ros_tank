import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

import xacro

# this is the function launch  system will look for
def generate_launch_description():
    package_rviz = "ros_tank_logic"

    rrbot_description_path = os.path.join(get_package_share_directory('ros_tank_description'))

    xacro_file = os.path.join(rrbot_description_path, 'urdf', 'robot_sim.xacro')

    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    robot_description_config = doc.toxml()
    robot_description = {'robot_description': robot_description_config}

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[robot_description],
        output='screen',
    )

    # RVIZ Configuration
    rviz_config_dir = os.path.join(get_package_share_directory(package_rviz), "rviz", "sim.rviz")

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        name='rviz_node',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', rviz_config_dir]
    )

    # create and return launch description object
    return LaunchDescription(
        [             
            robot_state_publisher_node,
            rviz_node
        ]
    )