# This is an auto generated Dockerfile for ros:desktop
# generated from docker_images_ros2/create_ros_image.Dockerfile.em
FROM ros:humble

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-hardware-interface \
    ros-${ROS_DISTRO}-gazebo-ros \
    ros-${ROS_DISTRO}-xacro \
    python-is-python3 \
    git \
    vim \
    less \
    xterm \
    iputils-ping
    
RUN mkdir -p ros2_ws/src && cd ros2_ws && rosdep install --from-paths src --ignore-src -r -y && colcon build

WORKDIR /ros2_ws/

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]
