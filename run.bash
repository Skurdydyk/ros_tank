xhost +local:root

SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR_PATH=$(dirname "$SCRIPT_PATH")
WS_DIR_PATH=$(realpath "$SCRIPT_DIR_PATH")

docker run -it --rm \
    --privileged \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --volume="/tmp/.docker.xauth:/tmp/.docker.xauth" \
    --volume="$WS_DIR_PATH/ros_tank_description:/ros2_ws/src/ros_tank_description" \
    --volume="$WS_DIR_PATH/ros_tank_gazebo:/ros2_ws/src/ros_tank_gazebo" \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=0" \
    --env="XAUTHORITY=/tmp/.docker.xauth" \
    --name="ros_tank_project_galactic_container" \
    --net host \
    ros_tank_project_galactic  \
    bash

xhost -local:root
