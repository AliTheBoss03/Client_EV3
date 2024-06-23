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
    if command == 'move_forward':
        motor_left.run(500)
        motor_right.run(500)
    elif command == 'stop':
        motor_left.stop()
        motor_right.stop()
    elif command == 'turn_left':
        motor_left.run(-100)
        motor_right.run(100)
    elif command == 'turn_right':
        motor_left.run(100)
        motor_right.run(-100)
    elif command == 'grab':
        grab_motor.run_time(500, 2000)
        motor_left.run(300)
        motor_right.run(300)
    elif command == 'beep':
        ev3.speaker.beep()
    # Add more commands as needed

def main():
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
