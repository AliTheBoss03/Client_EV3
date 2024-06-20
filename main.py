#!/usr/bin/env python3

import socket
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sound import Sound

# Initialize motors and sound
motor_left = LargeMotor(OUTPUT_A)
motor_right = LargeMotor(OUTPUT_B)
grab_motor = LargeMotor(OUTPUT_C)
sound = Sound()

def handle_command(command):
    if command == 'move_forward':
        motor_left.on(SpeedPercent(50))
        motor_right.on(SpeedPercent(50))
    elif command == 'stop':
        motor_left.off()
        motor_right.off()
    elif command == 'turn_left':
        motor_left.on(SpeedPercent(-25))
        motor_right.on(SpeedPercent(25))
    elif command == 'turn_right':
        motor_left.on(SpeedPercent(25))
        motor_right.on(SpeedPercent(-25))
    elif command == 'grab':
        grab_motor.on_for_seconds(SpeedPercent(50), 2)
        motor_left.off()
        motor_right.off()
    elif command == 'beep':
        sound.beep()
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
