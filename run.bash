#!/bin/bash

xhost + 
 
docker run -it --net=host --rm \
    --privileged \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=0" \
    --env="XAUTHORITY=/tmp/.docker.xauth" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix" \
    --volume="/tmp/.docker.xauth:/tmp/.docker.xauth" \
    --name="ros_tank_project_galactic_container" \
    ros_tank_project_galactic \
    bash