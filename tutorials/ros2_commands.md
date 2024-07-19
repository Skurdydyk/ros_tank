

ros2 pkg create --build-type ament_python <package_name>

ros2 pkg create --build-t ype ament_python --node-name my_node my_package

cd ~/ros2_ws

colcon build

colcon build --packages-select my_package

source install/local_setup.bash

ros2 run my_package my_node
