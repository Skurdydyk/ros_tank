FROM osrf/ros:humble-desktop

ENV DISPLAY=:1 \
    XAUTHORITY="/tmp/.docker.xauth" \
    net=host

RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-gazebo-* \
    ros-${ROS_DISTRO}-joint-state-publisher-gui \
    python-is-python3 \
    git \
    vim \
    nano \
    less \
    xterm 

RUN mkdir -p ros2_ws/src && cd ros2_ws && rosdep install --from-paths src --ignore-src -r -y 

WORKDIR /ros2_ws/

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]