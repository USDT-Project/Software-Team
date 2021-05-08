# All the functions will be here.

key_pressed = input
while key_pressed == True:
    if key_pressed == "U":
        d.up()
    if key_pressed == "I":
        d.down()
    if key_pressed == "A":
        d.roll_left()
    if key_pressed == "D":
        d.roll_right()
    if key_pressed == "W":
        d.forward()
    if key_pressed == "S":
        d.backward()
    if key_pressed == "E":
        d.yaw_right()
    if key_pressed == "R":
        d.yaw_left()
