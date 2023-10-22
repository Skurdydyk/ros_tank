from launch import LaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.substitutions import Command, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    urdf_file = "ros_tank.urdf.xacro"
    rviz_file = "hardware.rviz"
    package_hardware = "ros_tank_hardware"

    # Get URDF via xacro
    robot_desc_path = PathJoinSubstitution(
        [FindPackageShare("ros_tank_hardware"), "urdf", urdf_file]
    )

    robot_description = {"robot_description": Command(["xacro ", robot_desc_path])}

    robot_controllers = PathJoinSubstitution(
        [FindPackageShare(package_hardware), "config", "ros_tank_controllers.yaml"]
    )

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare(package_hardware), "rviz", rviz_file]
    )

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, robot_controllers],
        output="both",
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "forward_position_controller",
            "--controller-manager",
            "/controller_manager",
        ],
    )

    # Delay rviz start after `joint_state_broadcaster`
    delay_rviz_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[rviz_node],
        )
    )

    # Delay start of robot_controller after `joint_state_broadcaster`
    delay_robot_controller_spawner_after_joint_state_broadcaster_spawner = (
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=joint_state_broadcaster_spawner,
                on_exit=[robot_controller_spawner],
            )
        )
    )

    return LaunchDescription(
        [
            control_node,
            robot_state_publisher_node,
            joint_state_broadcaster_spawner,
            delay_rviz_after_joint_state_broadcaster_spawner,
            delay_robot_controller_spawner_after_joint_state_broadcaster_spawner,
        ]
    )
