from gpiozero import Robot
#Below this is code that would go into corresponding button presses

#forward button press
#mdm.stop()
#mdm.forward()

#left button press
#mdm.stop()
#mdm.left()

#right button press
#mdm.stop()
#mdm.right()

#reverse button press
#mdm.stop()
#mdm.backward()

#stop button press
#mdm.stop()
robot = Robot(left=(4, 14), right=(17, 27)) #This assigns the motor to its respective GPIO Pin
robot.forward() #This moves the robot forward


