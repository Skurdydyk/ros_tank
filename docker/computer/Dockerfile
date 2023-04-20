FROM osrf/ros:humble-desktop

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    vim \
    git \ 
    less \
    xterm \
    iputils-ping \
    python-is-python3 \
    ros-${ROS_DISTRO}-gazebo-* \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    ros-${ROS_DISTRO}-usb-cam

RUN mkdir -p ros2_ws/src && cd ros2_ws && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build

COPY ./ros2_ws/ ros2_ws/src/

# Build the ROS workspace using colcon build
RUN . /opt/ros/${ROS_DISTRO}/setup.sh && \
    cd ros2_ws && \
    colcon build

# Source the ROS workspace
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

WORKDIR /ros2_ws/

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]