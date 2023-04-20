xhost +local:root

SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR_PATH=$(dirname "$SCRIPT_PATH")
WS_DIR_PATH=$(realpath "$SCRIPT_DIR_PATH")

docker run -it --rm \
    --privileged \
    --device="/dev/ttyUSB0" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --volume="/tmp/.docker.xauth:/tmp/.docker.xauth" \
    --volume="$WS_DIR_PATH/ros2_ws/:/ros2_ws/src/" \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=0" \
    --env="XAUTHORITY=/tmp/.docker.xauth" \
    --name="ros_tank_container" \
    --net=host \
    ros_tank  \
    bash

xhost -local:root
