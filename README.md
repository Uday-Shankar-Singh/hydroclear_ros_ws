These files are version 1 of Hydroclear project and autonomous surface water vehicle which is inteneded to remove water hyacinth from water bodies.
This ROS2 package contains our first iteration which uses teleop_subscriber run on raspberry pi 4 and input given from teleop_keyboard_twist from host machine.
The commands from the host computer is turned to PWM values for BLDC thrusters in subscriber node.
This control is accompanied by a custom hydroclear_arduino_firmware which is connected to raspberry pi over UART.
