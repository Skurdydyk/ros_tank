#include "diffdrive_arduino/diffdrive_arduino.hpp"

#include <chrono>
#include <cmath>
#include <limits>
#include <memory>
#include <vector>

#include "hardware_interface/types/hardware_interface_type_values.hpp"
#include "hardware_interface/types/hardware_interface_return_values.hpp"
#include "rclcpp/rclcpp.hpp"

namespace diffdrive_arduino
{

DiffDriveArduino::DiffDriveArduino()
: logger_(rclcpp::get_logger("DiffDriveArduino"))
{
}

CallbackReturn DiffDriveArduino::on_init(const hardware_interface::HardwareInfo & info)
{
  if (hardware_interface::SystemInterface::on_init(info) != CallbackReturn::SUCCESS) {
    return CallbackReturn::ERROR;
  }

  hw_start_sec_ = stod(info_.hardware_parameters["example_param_hw_start_duration_sec"]);
  hw_stop_sec_ = stod(info_.hardware_parameters["example_param_hw_stop_duration_sec"]);
  hw_slowdown_ = stod(info_.hardware_parameters["example_param_hw_slowdown"]);

  hw_device_ = info_.hardware_parameters["device"];
  hw_baud_rate_ = stod(info_.hardware_parameters["baud_rate"]);
  hw_timeout_ = stod(info_.hardware_parameters["timeout"]);

  // Set up the Arduino
  arduino_.setup(hw_device_, hw_baud_rate_, hw_timeout_);

  if (info_.joints.size() != 2) {
    RCLCPP_ERROR(logger_, "Incorrect number of joints. 2 expected.");
    return hardware_interface::CallbackReturn::ERROR;
  }

  static constexpr int NUMBER_OF_COMMAND_INTERFACES = 1;

  for (uint i = 0; i < info_.joints.size(); i++) {
    const auto & command_interfaces = info_.joints[i].command_interfaces;

    if (command_interfaces.size() != NUMBER_OF_COMMAND_INTERFACES) {
      RCLCPP_FATAL(
        logger_,
        "Joint '%s' has %zu command interfaces found. 1 expected.",
        info_.joints[i].name.c_str(),
        info_.joints[i].command_interfaces.size());
      return hardware_interface::CallbackReturn::ERROR;
    }

    for (const auto & interface : command_interfaces) {
      if (interface.name != hardware_interface::HW_IF_VELOCITY) {
        RCLCPP_FATAL(
          logger_,
          "Joint '%s' has %s command interface. Expected %s.",
          info_.joints[i].name.c_str(),
          interface.name.c_str(),
          hardware_interface::HW_IF_VELOCITY);
        return hardware_interface::CallbackReturn::ERROR;
      }
    }
  }

  hw_states_.resize(info_.joints.size(), std::numeric_limits<double>::quiet_NaN());
  hw_commands_.resize(info_.joints.size(), std::numeric_limits<double>::quiet_NaN());

  return CallbackReturn::SUCCESS;
}

CallbackReturn DiffDriveArduino::on_configure(const rclcpp_lifecycle::State &previous_state)
{
  // prevent unused variable warning
  auto prev_state = previous_state;
  RCLCPP_INFO(logger_, "Configuring ...please wait...");

  for (int i = 0; i < hw_start_sec_; i++) {
    rclcpp::sleep_for(std::chrono::seconds(1));
    RCLCPP_INFO(logger_, "%.1f seconds left...", hw_start_sec_ - i);
  }

  // reset values always when configuring hardware
  for (uint i = 0; i < hw_states_.size(); i++) {
    hw_states_[i] = 0;
    hw_commands_[i] = 0;
  }

  RCLCPP_INFO(logger_, "Successfully configured!");

  return CallbackReturn::SUCCESS;
}

std::vector<hardware_interface::StateInterface>DiffDriveArduino::export_state_interfaces()
{
  std::vector<hardware_interface::StateInterface> state_interfaces;
  for (uint i = 0; i < info_.joints.size(); i++) {
    for (std::size_t j = 0; j < info_.joints[i].state_interfaces.size(); j++) {
        state_interfaces.emplace_back(
            hardware_interface::StateInterface(
                info_.joints[i].name,
                info_.joints[i].state_interfaces[j].name,
                &hw_states_[j]
            )
        );
    }
  }

  return state_interfaces;
}

std::vector<hardware_interface::CommandInterface>DiffDriveArduino::export_command_interfaces()
{
  std::vector<hardware_interface::CommandInterface> command_interfaces;
  for (uint i = 0; i < info_.joints.size(); i++) {
    for (std::size_t j = 0; j < info_.joints[i].command_interfaces.size(); j++) {
        command_interfaces.emplace_back(
            hardware_interface::CommandInterface(
                info_.joints[i].name,
                info_.joints[i].command_interfaces[j].name,
                &hw_commands_[i]
            )
        );
    }
  }

  return command_interfaces;
}

CallbackReturn DiffDriveArduino::on_activate(const rclcpp_lifecycle::State & /*previous_state*/)
{
  RCLCPP_INFO(logger_, "Activating ...please wait...");

  arduino_.sendEmptyMsg();

  for (int i = 0; i < hw_start_sec_; i++) {
    rclcpp::sleep_for(std::chrono::seconds(1));
    RCLCPP_INFO(logger_, "%.1f seconds left...", hw_start_sec_ - i);
  }

  // command and state should be equal when starting
  for (uint i = 0; i < hw_states_.size(); i++) {
    hw_commands_[i] = hw_states_[i];
  }

  RCLCPP_INFO(logger_, "Successfully activated!");

  return CallbackReturn::SUCCESS;
}

CallbackReturn DiffDriveArduino::on_deactivate(const rclcpp_lifecycle::State & /*previous_state*/)
{
  RCLCPP_INFO(logger_, "Deactivating ...please wait...");

  for (int i = 0; i < hw_stop_sec_; i++) {
    rclcpp::sleep_for(std::chrono::seconds(1));
    RCLCPP_INFO(logger_, "%.1f seconds left...", hw_stop_sec_ - i);
  }

  RCLCPP_INFO(logger_, "Successfully deactivated!");

  return CallbackReturn::SUCCESS;
}

hardware_interface::return_type DiffDriveArduino::read(const rclcpp::Time & time, const rclcpp::Duration & period)
{
  if (!arduino_.connected()) {
    return hardware_interface::return_type::ERROR;
  }

//  RCLCPP_INFO(logger_, "Reading...");

//  for (uint i = 0; i < hw_states_.size(); i++) {
    // Simulate RRBot's movement
//    hw_states_[i] = hw_states_[i] + (hw_commands_[i] - hw_states_[i]) / hw_slowdown_;
//    RCLCPP_INFO(logger_, "Got state %.5f for joint %d!", hw_states_[i], i);
//  }

//  RCLCPP_INFO(logger_, "Joints successfully read!");

  return hardware_interface::return_type::OK;
}

hardware_interface::return_type DiffDriveArduino::write(const rclcpp::Time & time, const rclcpp::Duration & period)
{
  if (!arduino_.connected()) {
    return hardware_interface::return_type::ERROR;
  }

  new_value_l_ = hw_commands_[0] / rads_per_count_ / loop_rate_;
  new_value_r_ = hw_commands_[1] / rads_per_count_ / loop_rate_;

  if((new_value_l_ != old_value_l_) and (new_value_r_ != old_value_r_)){
    arduino_.setMotorValues(new_value_l_, new_value_r_);
    old_value_l_ = new_value_l_;
    old_value_r_ = new_value_r_;
  }

//  RCLCPP_INFO(logger_, "Writing...");

//  for (uint i = 0; i < hw_commands_.size(); i++) {
    // Simulate sending commands to the hardware
//    RCLCPP_INFO(logger_, "Got command %.5f for joint %d!", hw_commands_[i], i);
//  }

//  RCLCPP_INFO(logger_, "Joints successfully written!");

  return hardware_interface::return_type::OK;
}

} // namespace diffdrive_arduino

#include "pluginlib/class_list_macros.hpp"

PLUGINLIB_EXPORT_CLASS(
  diffdrive_arduino::DiffDriveArduino,
  hardware_interface::SystemInterface
)
