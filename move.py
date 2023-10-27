import RPi.GPIO as GPIO
import time
print("THIS IS TOTALLY FINE")
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the motors
motor1_pins = (18, 23)  # Motor 1: GPIO18 (PWM), GPIO23 (Direction)
motor2_pins = (17, 22)  # Motor 2: GPIO17 (PWM), GPIO22 (Direction)

# Set up GPIO pins
GPIO.setup(motor1_pins[0], GPIO.OUT)
GPIO.setup(motor1_pins[1], GPIO.OUT)
GPIO.setup(motor2_pins[0], GPIO.OUT)
GPIO.setup(motor2_pins[1], GPIO.OUT)

# Initialize PWM for motor control
motor1_pwm = GPIO.PWM(motor1_pins[0], 100)  # 100 Hz frequency
motor2_pwm = GPIO.PWM(motor2_pins[0], 100)

# Start PWM with a 0% duty cycle (motors are off)
motor1_pwm.start(0)
motor2_pwm.start(0)

# Define motor directions (HIGH for forward, LOW for backward)
def set_motor_direction(motor_pins, direction):
    GPIO.output(motor_pins[1], direction)

# Function to control motor speed
def set_motor_speed(pwm, speed):
    pwm.ChangeDutyCycle(speed)

# Function to move both motors forward
def move_forward(speed, duration):
    set_motor_direction(motor1_pins, GPIO.HIGH)  # Motor 1 forward
    set_motor_direction(motor2_pins, GPIO.HIGH)  # Motor 2 forward
    set_motor_speed(motor1_pwm, speed)
    set_motor_speed(motor2_pwm, speed)
    time.sleep(duration)
    set_motor_speed(motor1_pwm, 0)  # Stop motor 1
    set_motor_speed(motor2_pwm, 0)  # Stop motor 2

# Move forward at speed 50 for 3 seconds
move_forward(50, 3)

# Cleanup GPIO
GPIO.cleanup()

print("ended")
