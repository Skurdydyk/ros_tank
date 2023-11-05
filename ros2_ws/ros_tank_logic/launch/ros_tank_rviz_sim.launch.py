from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    urdf_file = "robot_sim.xacro"
    rviz_file = "sim.rviz"
    rviz_package = "ros_tank_logic"
    description_package = "ros_tank_description"

    sim_time = LaunchConfiguration("sim_time")

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare(rviz_package), "rviz", rviz_file]
    )

    robot_desc_path = PathJoinSubstitution(
        [FindPackageShare(description_package), "urdf", urdf_file]
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {
                "use_sim_time": sim_time,
                "robot_description": Command(["xacro ", robot_desc_path]),
            }
        ],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        name="rviz_node",
        parameters=[{"use_sim_time": sim_time}],
        arguments=["-d", rviz_config_file],
    )

    return LaunchDescription([robot_state_publisher_node, rviz_node])
