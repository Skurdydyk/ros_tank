FROM osrf/ros:humble-desktop

RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-gazebo-* \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
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