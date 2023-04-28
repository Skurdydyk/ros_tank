#include "diffdrive_arduino/arduino_comms.h"

#include <rclcpp/rclcpp.hpp>
#include <sstream>
#include <cstdlib>


void ArduinoComms::setup(const std::string &serial_device, int32_t baud_rate, int32_t timeout_ms){  
    serial_conn_.setPort(serial_device);
    serial_conn_.setBaudrate(baud_rate);
    serial::Timeout tt = serial::Timeout::simpleTimeout(timeout_ms);
    serial_conn_.setTimeout(tt); // This should be inline except setTimeout takes a reference and so needs a variable
    serial_conn_.open();
}

void ArduinoComms::sendEmptyMsg(){
    std::string response = sendMsg("\r");
}

void ArduinoComms::setMotorValues(int val_1, int val_2){
    std::stringstream ss;
    ss << "m " << val_1 << " " << val_2 << "\r\n";
    sendMsg(ss.str(), true);
}

void ArduinoComms::setPidValues(float k_p, float k_d, float k_i, float k_o){
    std::stringstream ss;
    ss << "u " << k_p << ":" << k_d << ":" << k_i << ":" << k_o << "\r";
    sendMsg(ss.str());
}

std::string ArduinoComms::sendMsg(const std::string &msg_to_send, bool print_output){
    serial_conn_.write(msg_to_send);
    std::string response = serial_conn_.readline();

    if (print_output){
        RCLCPP_INFO_STREAM(logger_,"Sent: " << msg_to_send);
        RCLCPP_INFO_STREAM(logger_,"Received: " << response);
    }

    return response;
}
