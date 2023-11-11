#Importation of necessary libraries and general setup
from adafruit_motorkit import MotorKit
kit=MotorKit(0x40)
import time

#forward
kit.motor1.throttle=0.8
kit.motor2.throttle=-0.8
#wait to stop motors to allow for forward movement
time.sleep(4.3)
#stop motors in preparation for next step
kit.motor1.throttle=0.0
kit.motor2.throttle=0.0
time.sleep(0.25)

#Right
kit.motor1.throttle=0.8
kit.motor2.throttle=0.8
#turn time
time.sleep(0.85)
#stop
kit.motor1.throttle=0.0
kit.motor2.throttle=0.0
time.sleep(0.25)

#forward
kit.motor1.throttle=0.8
kit.motor2.throttle=-0.8
#wait to stop motors to allow for forward movement
time.sleep(2.2)
#stop motors in preparation for next step
kit.motor1.throttle=0.0
kit.motor2.throttle=0.0
time.sleep(0.25)

#backward
kit.motor1.throttle=-0.8
kit.motor2.throttle=0.8
#wait to stop motors to allow for forward movement
time.sleep(5.5)
#stop motors in preparation for next step
kit.motor1.throttle=0.0
kit.motor2.throttle=0.0
time.sleep(0.25)
