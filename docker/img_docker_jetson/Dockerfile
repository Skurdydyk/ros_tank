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

COPY ./ros2_ws/ros_tank_control ros2_ws/src/ros_tank_control
COPY ./ros2_ws/ros_tank_description ros2_ws/src/ros_tank_description
COPY ./ros2_ws/serial ros2_ws/src/serial

# Build the ROS workspace using colcon build
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && cd ros2_ws && colcon build

# Source the ROS workspace
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

WORKDIR /ros2_ws/

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]
