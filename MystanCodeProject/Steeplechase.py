"""
File: Steeplechase.py
Name: 周侑庭
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    pre-condition: Karel is on the left side of the wall, facing east.
    post-condition: Karel is on the right side of the wall.
    """
    up()
    cross()
    down()


def cross():
    """
    pre-condition: Karel is at the upper left of the wall, facing north.
    post-condition: Karel is at the upper right, facing south.
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition: Karel is at the upper right, facing south.
    post-condition:
    """
    while front_is_clear():
        move()



def up():
    """
    pre-condition: Karel is on the left side of the wall, facing east.
    post-condition: Karel is at the upper left of the wall, facing north.
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative:
    # while not front_is_clear():
    #    turn_left()
    #   move()
    #    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
