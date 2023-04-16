FROM ros:humble

RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-hardware-interface \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    ros-${ROS_DISTRO}-xacro \
    ros-${ROS_DISTRO}-ros2-controllers \
    python-is-python3 \
    git \
    vim \
    less \
    xterm \
    iputils-ping

RUN sudo apt install build-essential -y \
    libboost-system-dev \
    libboost-thread-dev \
    libboost-program-options-dev \
    libboost-test-dev

RUN mkdir -p ros2_ws/src && cd ros2_ws && rosdep install --from-paths src --ignore-src -r -y && colcon build

WORKDIR /ros2_ws/

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]
