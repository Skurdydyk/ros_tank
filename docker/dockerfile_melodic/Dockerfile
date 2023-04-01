# Start with a base image of Ubuntu 18.04
FROM ubuntu:18.04

# Set the shell to bash
SHELL ["/bin/bash", "-c"]

# Set the environment variables for ROS Melodic
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV ROS_DISTRO melodic

# Add the ROS Melodic package repository to the sources list
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl gnupg2 && \
    curl -sSL http://packages.ros.org/ros.key -o /tmp/ros.key && \
    apt-key add /tmp/ros.key && \
    echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-latest.list

# Install ROS Melodic packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ros-melodic-desktop-full \
        python-rosdep \
        python-rosinstall \
        python-rosinstall-generator \
        python-wstool \
        build-essential \
        && \
    rm -rf /var/lib/apt/lists/*

# Initialize rosdep
RUN rosdep init && \
    rosdep update

# Set up the ROS environment variables
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc

# Set the working directory
WORKDIR /root

# Set the default command to launch a bash shell
CMD ["/bin/bash"]