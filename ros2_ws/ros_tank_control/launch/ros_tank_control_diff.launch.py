from launch import LaunchDescription
from launch.actions import TimerAction, RegisterEventHandler
from launch.substitutions import Command, PathJoinSubstitution
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    urdf_file = "robot.xacro"
    description_package = "ros_tank_description"
    control_package = "ros_tank_control"

    # Get URDF via xacro
    robot_desc_path = PathJoinSubstitution(
        [FindPackageShare(description_package), "urdf", urdf_file]
    )

    robot_description = {"robot_description": Command(["xacro ", robot_desc_path])}

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
        output="screen",
    )

    robot_diff_controller = PathJoinSubstitution(
        [FindPackageShare(control_package), "config", "diff_drive_controller.yaml"]
    )

    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, robot_diff_controller],
    )

    delayed_controller_manager = TimerAction(period=3.0, actions=[controller_manager])

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_controller"],
    )

    delayed_diff_drive_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[diff_drive_spawner],
        )
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    delayed_joint_broad_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[joint_broad_spawner],
        )
    )

    return LaunchDescription(
        [
            robot_state_publisher_node,
            delayed_controller_manager,
            delayed_diff_drive_spawner,
            delayed_joint_broad_spawner,
        ]
    )
