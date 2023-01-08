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

RUN mkdir -p ros2_ws/src && \
    cd ros2_ws/src 
    # && \
    # git clone https://github.com/ros-controls/ros2_control_demos.git -b galactic && \
    # vcs import --input ros2_control_demos/ros2_control_demos.galactic.repos
    
COPY ./ros_tank ros2_ws/src/ros_tank/

RUN cd ros2_ws && rosdep install --from-paths src --ignore-src -r -y 

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]