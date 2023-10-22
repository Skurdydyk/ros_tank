cmake_minimum_required(VERSION 3.16)
project(ros_tank_hardware LANGUAGES CXX)

if(CMAKE_CXX_COMPILER_ID MATCHES "(GNU|Clang)")
  add_compile_options(-Wall -Wextra)
endif()

# find dependencies
set(THIS_PACKAGE_INCLUDE_DEPENDS
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
)

# find dependencies
find_package(ament_cmake REQUIRED)
foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
  find_package(${Dependency} REQUIRED)
endforeach()


## COMPILE
add_library(
  ros_tank_hardware
  SHARED
  hardware/ros_tank.cpp
)
target_compile_features(ros_tank_hardware PUBLIC cxx_std_17)
target_include_directories(ros_tank_hardware PUBLIC
$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/hardware/include>
$<INSTALL_INTERFACE:include/ros_tank_hardware>
)
ament_target_dependencies(
  ros_tank_hardware PUBLIC
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

# Causes the visibility macros to use dllexport rather than dllimport,
# which is appropriate when building the dll but not consuming it.
target_compile_definitions(${PROJECT_NAME} PRIVATE "ROS_TANK_HARDWARE_BUILDING_DLL")

# Export hardware plugins
pluginlib_export_plugin_description_file(hardware_interface ros_tank_hardware.xml)

# INSTALL
install(
  DIRECTORY hardware/include/
  DESTINATION include/ros_tank_hardware
)
install(
  DIRECTORY description/ros2_control description/urdf description
  DESTINATION share/ros_tank_hardware
)
install(
  DIRECTORY bringup/launch bringup/config
  DESTINATION share/ros_tank_hardware
)
install(TARGETS ros_tank_hardware
  EXPORT export_ros_tank_hardware
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
endif()

## EXPORTS
ament_export_targets(export_ros_tank_hardware HAS_LIBRARY_TARGET)
ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})
ament_package()
