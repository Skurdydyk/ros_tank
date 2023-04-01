xhost +local:root

SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR_PATH=$(dirname "$SCRIPT_PATH")
WS_DIR_PATH=$(realpath "$SCRIPT_DIR_PATH")

docker run -it --rm \
    --privileged \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --volume="/tmp/.docker.xauth:/tmp/.docker.xauth" \
    --volume="$WS_DIR_PATH/../diffdrive_arduino:/ros2_ws/src/diffdrive_arduino" \
    --volume="$WS_DIR_PATH/../serial:/ros2_ws/src/serial" \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=0" \
    --env="XAUTHORITY=/tmp/.docker.xauth" \
    --name="ros_tank_melodic_container" \
    --net host \
    ros_tank_melodic \
    bash

xhost -local:root
