# ROBOMASTER-S1-Python-Examples

# Learning how to program the Robomaster S1 in Python

# Note: you must install the Robomaster S1 app, either on your wireless mobile device or on your computer, via Wi-Fi.
# Next after installing the Robomaster S1 App, you will have to update the firmware for the Robomaster S1.
# Next you must calibrate the Robomaster S1 so it can work properly.

# Note: to be able to program the Robomaster S1 in Scratch or Python, you must run the Robomaster S1 app, then connect
# the Robomaster S1 to it, via wireless mobile device or on your computer, via Wi-Fi.

'''----------------------------------------------------------------------------------------------------------------'''

# Make the Robomaster drive non-stop while making all the LEDS flash-rotate two, different colours.
# Type and execute/run the program example below and see what happens.

def start():
    while True:
        chassis_ctrl.set_wheel_speed(50,50,50,50)
        led_ctrl.set_top_led(rm_define.armor_top_right,255,0,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_right,[1,3,5,7],rm_define.effect_always_on)
        led_ctrl.set_top_led(rm_define.armor_top_left,0,255,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_left,[1,3,5,7],rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,255,rm_define.effect_always_on)
        time.sleep(.095)
        led_ctrl.set_top_led(rm_define.armor_top_right,0,255,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_right,[2,4,6,8],rm_define.effect_always_on)
        led_ctrl.set_top_led(rm_define.armor_top_left,255,0,255,rm_define.effect_always_off)
        led_ctrl.set_single_led(rm_define.armor_top_left,[2,4,6,8],rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)
        time.sleep(.095)

'''----------------------------------------------------------------------------------------------------------------'''

# Make the blaster fire four times. Type and execute/run the program example below and see
# what happens.

def start():
    for count in range(4):
        led_ctrl.gun_led_on()
        gun_ctrl.fire_once()
        led_ctrl.gun_led_off()

'''----------------------------------------------------------------------------------------------------------------'''

# Make all the LEDs flash ten times a second, while making the chassis rocks back and forth.
# Type and execute/run the program example below and see what happens.

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    for i in range(2):
        led_ctrl.set_flash(rm_define.armor_all,10)
        led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
        chassis_ctrl.set_wheel_speed(50,-50,50,-50)
        time.sleep(1)
        chassis_ctrl.set_wheel_speed(-50,50,-50,50)
        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------'''

# Turn on the Robomaster's gun light and make the LEDs pulsate, while the chassis rocks back and forth.
# Type and execute/run this program example below and see what happens.

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    for i in range(2):
        led_ctrl.gun_led_on()
        led_ctrl.set_top_led(rm_define.armor_top_all,0,0,255,rm_define.effect_breath)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,255,rm_define.effect_breath)
        chassis_ctrl.set_wheel_speed(50,-50,50,-50)
        time.sleep(1)
        chassis_ctrl.set_wheel_speed(-50,50,-50,50)
        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------'''

# Turn on the Robomaster's gun light and make the LEDS pulsate, while rotating clockwise and anti
# clockwise. Type and execute/run the program example below and see what happens.

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    for i in range(2):
        led_ctrl.gun_led_on()
        led_ctrl.set_top_led(rm_define.armor_top_all,0,0,255,rm_define.effect_breath)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,255,rm_define.effect_breath)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,90)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise,90)

'''----------------------------------------------------------------------------------------------------------------'''

# Make the Robomaster recognize the red heart and make him wait for it to be recognized
# before he works his bright cyan lights and starts to move his chassis forward for one
# second each time the red heart is shown to him. Type and execute/run the program example
# below and see what happens.

def start():
    while True:
        media_ctrl.zoom_value_update(1)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
def vision_recognized_marker_trans_red_heart(msg):
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255,rm_define.effect_always_on)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_on)
    chassis_ctrl.set_wheel_speed(50,50,50,50)
    time.sleep(1)
    led_ctrl.set_top_led(rm_define.armor_top_all,0,255,255,rm_define.effect_always_off)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,255,255,rm_define.effect_always_off)
    chassis_ctrl.stop()

'''----------------------------------------------------------------------------------------------------------------'''

# Make the Robomaster recognize the red heart and make him wait for it to be recognized
# before he works his bright red lights and starts blinking them twice. Type and execute/run
# the program example below and see what happens.

def start():
    while True:
        media_ctrl.zoom_value_update(1)
        led_ctrl.set_top_led(rm_define.armor_top_all,0,0,0,rm_define.effect_always_off)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,0,0,0,rm_define.effect_always_off)
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
def vision_recognized_marker_trans_red_heart(msg):
    led_ctrl.set_flash(rm_define.armor_all,2)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------'''

# Red Heart Aim Example:

def start():
    while True:
        vision_ctrl.enable_detection(rm_define.vision_detection_marker)
        led_ctrl.set_top_led(rm_define.armor_top_all,255,255,255,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,255,rm_define.effect_always_on)
        vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
        led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_always_on)
        vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_red_heart)

'''----------------------------------------------------------------------------------------------------------------'''

# Rapid-fire blaster gun 8 times Example:

def start():
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()

'''----------------------------------------------------------------------------------------------------------------'''

# Turret fire and rotate 180 degrees Example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gun_ctrl.set_fire_count(2)
    gimbal_ctrl.set_rotate_speed(200)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    gun_ctrl.fire_once()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    time.sleep(0.5)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    gun_ctrl.fire_once()
    gun_ctrl.stop()
    time.sleep(0.5)

'''----------------------------------------------------------------------------------------------------------------'''

# Rotate the turret and set the speed to 20, while making the lights
# change from yellow to red, and back to yellow.

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(20)
    led_ctrl.set_flash(rm_define.armor_all,2)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    time.sleep(1)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    time.sleep(1)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    time.sleep(1)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()
    time.sleep(1)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)
    gun_ctrl.set_fire_count(8)
    gun_ctrl.fire_once()

'''----------------------------------------------------------------------------------------------------------------'''

# Rotate the turret and set the speed to 20, while changing all the lights from
# red to yellow.

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.set_rotate_speed(20)
    led_ctrl.set_flash(rm_define.armor_all,2)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,180)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,90)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)

'''----------------------------------------------------------------------------------------------------------------'''

# Rotate gimbal and pitch example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    gimbal_ctrl.recenter()
    time.sleep(0.5)
    led_ctrl.set_flash(rm_define.armor_all, 2)
    gimbal_ctrl.set_rotate_speed(30)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,90)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,180)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,90)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,55)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,55)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.pitch_ctrl(0)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,180)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right,360)
    led_ctrl.set_top_led(rm_define.armor_top_all,255,255,0,rm_define.effect_flash)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left,180)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive sideways side to side example 1:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-30,30,30,-30)
        time.sleep(3)
        chassis_ctrl.set_wheel_speed(30,-30,-30,30)
        time.sleep(3)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive sideways side to side example 2:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_trans_speed(0.2)
        chassis_ctrl.move_with_time(90,3)
        chassis_ctrl.move_with_time(-90,3)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle right example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(80,-80,-20,20)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-80,80,20,-20)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle right example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(20,-20,-80,80)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-20,20,80,-80)

# Drive front sideways circle right and left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-80,80,20,-20)
        time.sleep(10)
        chassis_ctrl.set_wheel_speed(80,-80,-20,20)
        time.sleep(10)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle right and left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(20,-20,-80,80)
        time.sleep(10)
        chassis_ctrl.set_wheel_speed(-20,20,80,-80)
        time.sleep(10)

'''----------------------------------------------------------------------------------------------------------------'''

# For-loop blinking LED's rate example:

def start():
    for i in range(10):
        led_ctrl.set_flash(rm_define.armor_all,i+1)
        led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,255,0,rm_define.effect_flash)
        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive and turn around example 1:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-30,30,-30,30)
        time.sleep(4)
        chassis_ctrl.set_wheel_speed(30,30,30,30)
        time.sleep(3)
        chassis_ctrl.set_wheel_speed(30,-30,30,-30)
        time.sleep(4)
        chassis_ctrl.set_wheel_speed(30,30,30,30)
        time.sleep(3)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive and turn around example 2:

def start():
    chassis_ctrl.set_rotate_speed(30)
    while True:
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.set_wheel_speed(30,30,30,30)
        time.sleep(4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.set_wheel_speed(30,30,30,30)
        time.sleep(4)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive and turn around example 3:

def start():
    chassis_ctrl.set_trans_speed(0.3)
    chassis_ctrl.set_rotate_speed(50)
    for i in range(2):
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_time(0,4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise,180)
        chassis_ctrl.move_with_time(0,4)
        
'''----------------------------------------------------------------------------------------------------------------'''

# Drive the chassis at -45, 45 and 135, -135 degrees
# Create a for-loop to repeat the sequence two times.
# Set the chassis translation speed to (0.5)
# Use a time.sleep(1) delay to allow the chassis to move
# for one second on each degee turn.

# Type and execute/run the program example below and
# see what happens.

def start():
    chassis_ctrl.set_trans_speed(0.5)
    for i in range(2):
        chassis_ctrl.move(-45)
        time.sleep(1)
        chassis_ctrl.move(45)
        time.sleep(1)
        chassis_ctrl.move(135)
        time.sleep(1)
        chassis_ctrl.move(-135)
        time.sleep(1)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle right example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(80,-80,-20,20)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-80,80,20,-20)
        
'''----------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle right example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(20,-20,-80,80)

'''----------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-20,20,80,-80)
        
'''----------------------------------------------------------------------------------------------------------------'''

# Drive front sideways circle right and left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(-80,80,20,-20)
        time.sleep(10)
        chassis_ctrl.set_wheel_speed(80,-80,-20,20)
        time.sleep(10)  
        
'''----------------------------------------------------------------------------------------------------------------'''

# Drive rear sideways circle right and left example:

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    while True:
        chassis_ctrl.set_wheel_speed(20,-20,-80,80)
        time.sleep(10)
        chassis_ctrl.set_wheel_speed(-20,20,80,-80)
        time.sleep(10)

'''----------------------------------------------------------------------------------------------------------------'''

# More future Robomaster s1 Python examples still to come as I learn more and more, each and every day.

'''----------------------------------------------------------------------------------------------------------------'''