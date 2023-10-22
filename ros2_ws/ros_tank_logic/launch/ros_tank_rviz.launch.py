from launch import LaunchDescription
from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    urdf_file = "robot.xacro"
    rviz_file = "robot.rviz"
    package_rviz = "ros_tank_logic"
    package_description = "ros_tank_description"

    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare(package_rviz), "rviz", rviz_file]
    )
    robot_desc_path = PathJoinSubstitution(
        [FindPackageShare(package_description), "urdf", urdf_file]
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher_node",
        emulate_tty=True,
        parameters=[
            {
                "use_sim_time": True,
                "robot_description": Command(["xacro ", robot_desc_path]),
            }
        ],
        output="screen",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        name="rviz_node",
        parameters=[{"use_sim_time": False}],
        arguments=["-d", rviz_config_path],
    )

    return LaunchDescription([robot_state_publisher_node, rviz_node])
