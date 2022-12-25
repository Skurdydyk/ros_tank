# This is an auto generated Dockerfile for ros:ros-base
# generated from docker_images/create_ros_image.Dockerfile.em
FROM ros:noetic-ros-core-focal

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && \
  rosdep update --rosdistro $ROS_DISTRO

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-base=1.5.0-1* \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY=:1 \
    XAUTHORITY="/tmp/.docker.xauth" \
    net=host
    

RUN apt-get update && \
    apt-get install -y libsdl-image1.2-dev && \
    apt-get install libsdl-dev && \
    apt-get install -y git && \
    apt-get install -y libyaml-cpp-dev && \
    apt install -y python3-pip && \ 
    apt install -y vim && \
    pip3 install pyserial

RUN apt-get install -y ros-noetic-cv-bridge

RUN mkdir catkin_ws &&  \
    cd catkin_ws && \
    mkdir src &&  \
    cd src && \
    git clone https://github.com/Skurdydyk/teleop_twist_keyboard.git && \
    git clone https://github.com/Skurdydyk/usb_cam.git && \
    git clone https://github.com/Skurdydyk/rplidar_ros.git && \
    git clone https://github.com/ros-perception/image_common.git

COPY ./ros_tank /catkin_ws/src/ros_tank/

RUN /bin/bash -c 'cd ../../; \
    source ros_entrypoint.sh; \
    cd catkin_ws; \
    catkin_make'
