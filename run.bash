xhost +local:root

SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR_PATH=$(dirname "$SCRIPT_PATH")
WS_DIR_PATH=$(realpath "$SCRIPT_DIR_PATH")

docker run -it --rm \
    --privileged \
    --device="/dev/ttyUSB0" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --volume="/tmp/.docker.xauth:/tmp/.docker.xauth" \
    --volume="$WS_DIR_PATH/ros_tank_logic:/ros2_ws/src/ros_tank_logic" \
    --volume="$WS_DIR_PATH/ros_tank_gazebo:/ros2_ws/src/ros_tank_gazebo" \
    --volume="$WS_DIR_PATH/ros_tank_control:/ros2_ws/src/ros_tank_control" \
    --volume="$WS_DIR_PATH/ros_tank_navigation:/ros2_ws/src/ros_tank_navigation" \
    --volume="$WS_DIR_PATH/ros_tank_description:/ros2_ws/src/ros_tank_description" \
    --volume="$WS_DIR_PATH/serial:/ros2_ws/src/serial" \
    --volume="$WS_DIR_PATH/diffdrive_arduino_humble:/ros2_ws/src/diffdrive_arduino" \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=0" \
    --env="XAUTHORITY=/tmp/.docker.xauth" \
    --name="ros_tank_container" \
    --net host \
    ros_tank  \
    bash

xhost -local:root
