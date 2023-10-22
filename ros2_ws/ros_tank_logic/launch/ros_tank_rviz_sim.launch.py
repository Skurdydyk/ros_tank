from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    urdf_file = "robot_sim.xacro"
    rviz_file = "sim.rviz"
    rviz_package = "ros_tank_logic"

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare(rviz_package), "rviz", rviz_file]
    )
    robot_desc_path = PathJoinSubstitution(
        [FindPackageShare("ros_tank_hardware"), "urdf", urdf_file]
    )
    # Get URDF via xacro
    robot_description = {"robot_description": Command(["xacro ", robot_desc_path])}

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        name="rviz_node",
        parameters=[{"use_sim_time": True}],
        arguments=["-d", rviz_config_file],
    )

    return LaunchDescription([robot_state_publisher_node, rviz_node])
