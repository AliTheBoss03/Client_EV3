#!/usr/bin/env pybricks-micropython

import socket
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait

# Initialize EV3 brick
ev3 = EV3Brick()

# Initialize motors
motor_left = Motor(Port.A)
motor_right = Motor(Port.B)
grab_motor = Motor(Port.C)

def handle_command(command):
    if command == 'move_backward':
        motor_left.run(-300)
        motor_right.run(-300)
    elif command == 'move_forward':
        motor_left.run(300)
        motor_right.run(300)
    elif command == 'stop':
        motor_left.stop()
        motor_right.stop()
    elif command == 'turn_left':
        motor_left.run(-150)
        motor_right.run(150)
    elif command == 'turn_right':
        motor_left.run(150)
        motor_right.run(-150)
    elif command == 'move_to_goal':
        motor_left.run(300)
        motor_right.run(300)
        wait(30000)  # Run towards the goal for 30 seconds (adjust as necessary)
        motor_left.stop()
        motor_right.stop()
    elif command == 'beep':
        ev3.speaker.beep()
    elif command == 'move_to_target_point':
        # Code to move to the specific point
        motor_left.run(200)
        motor_right.run(200)
        wait(20000)  # Adjust this duration to reach the point
        motor_left.stop()
        motor_right.stop()
    elif command == 'align_to_target_point':
        # Code to align the robot to the target point
        motor_left.run(100)
        motor_right.run(-100)
        wait(10000)  # Adjust this duration to align the robot
        motor_left.stop()
        motor_right.stop()
    elif command == 'start_grabber_reverse':
        grab_motor.run(1000)  # Start the grabber motor in reverse
    elif command == 'stop_grabber':
        grab_motor.stop()
    # Add more commands as needed

def main():
    # Start the grabber motor at 1000 RPM continuously
    grab_motor.run(-1000)
    
    ip = '0.0.0.0'
    port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    print("Waiting for commands...")
    while True:
        data, _ = sock.recvfrom(1024)
        command = data.decode()
        print("Received command: {}".format(command))
        handle_command(command)

if __name__ == "__main__":
    main()
