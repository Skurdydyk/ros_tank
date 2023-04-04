# This is an auto generated Dockerfile for ros:desktop
# generated from docker_images_ros2/create_ros_image.Dockerfile.em
FROM ros:galactic-ros-base-focal

# install ros2 packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-galactic-desktop=0.9.3-2* \
    && rm -rf /var/lib/apt/lists/*

# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-galactic-ros2-control \
    ros-galactic-hardware-interface \
    ros-galactic-gazebo-ros \
    ros-galactic-xacro

ENV XAUTHORITY="/tmp/.docker.xauth" \
    net=host
    
RUN mkdir -p ros2_ws/src &&  \
    cd ros2_ws/src && \
    git clone -b galactic https://github.com/Buzzology/diffdrive_arduino.git 

WORKDIR /ros2_ws/

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]
