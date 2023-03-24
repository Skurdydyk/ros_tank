import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

# this is the function launch  system will look for
def generate_launch_description():

    ####### DATA INPUT ##########
    urdf_file = 'robot_sim.xacro'
    package_description = "ros_tank_description"
    package_rviz = "ros_tank_logic"

    ####### DATA INPUT END ##########
    print("Fetching URDF ==>")
    robot_desc_path = os.path.join(get_package_share_directory(package_description), "urdf", urdf_file)

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        emulate_tty=True,
        parameters=[{'use_sim_time': True, 'robot_description': Command(['xacro ', robot_desc_path])}],
        output="screen"
    )

    # RVIZ Configuration
    rviz_config_dir = os.path.join(get_package_share_directory(package_rviz), "rviz", "robot.rviz")

    rviz_node = Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            name='rviz_node',
            parameters=[{'use_sim_time': True}],
            arguments=['-d', rviz_config_dir])

    joint_state_publisher_gui = ExecuteProcess(
        cmd=['ros2', 'run', 'joint_state_publisher_gui', 'joint_state_publisher_gui'],
        output='screen'
    )

    teleop_twist_keyboard = ExecuteProcess(
        cmd=['ros2', 'run', 'teleop_twist_keyboard', 'teleop_twist_keyboard'],
        output='screen'
    )
    
    # create and return launch description object
    return LaunchDescription(
        [               
            teleop_twist_keyboard,
            joint_state_publisher_gui,
            robot_state_publisher_node,
            rviz_node
        ]
    )