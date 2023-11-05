FROM ros:humble

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    git \
    vim \
    less \
    xterm \
    nano \
    iputils-ping \
    python-is-python3 \
    ros-${ROS_DISTRO}-xacro \
    ros-${ROS_DISTRO}-usb-cam \
    ros-${ROS_DISTRO}-ros2-control \
    ros-${ROS_DISTRO}-ros2-controllers \
    ros-${ROS_DISTRO}-hardware-interface \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    ros-${ROS_DISTRO}-rplidar-ros \
    ros-${ROS_DISTRO}-navigation2

RUN sudo apt install build-essential -y \
    libboost-test-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libboost-program-options-dev

RUN mkdir -p ros2_ws/src && \
    cd ros2_ws && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build

COPY ./ros2_ws/serial ros2_ws/src/serial
COPY ./ros2_ws/ros_tank_control ros2_ws/src/ros_tank_control
COPY ./ros2_ws/diffdrive_arduino ros2_ws/src/diffdrive_arduino
COPY ./ros2_ws/ros_tank_navigation ros2_ws/src/ros_tank_navigation
COPY ./ros2_ws/ros_tank_description ros2_ws/src/ros_tank_description

# Build the ROS workspace using colcon build
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    cd ros2_ws && \
    colcon build

# Source the ROS workspace
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

WORKDIR /ros2_ws/

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]
