"""
-----------------------------------------------------
Author: Yousf Al Salti
Date: 31/03/2025
Time: 3:14 PM
Version: 1.0
-----------------------------------------------------

Filename: pingpong_classes

-----------------------------------------------------
Description: [Describe the purpose of the script]
-----------------------------------------------------

Inputs: [Describe inputs]
Outputs: [Describe outputs]
-----------------------------------------------------

Contact Information:
📧 Outlook: [yousefalsalti2411@outlook.com]
📧 Gmail: [yousefalsalti024@gmail.com]
🔗 GitHub: [https://github.com/yoyo24ii]
🔗 LinkedIn: [https://www.linkedin.com/in/yousfsalti24ii/]
-----------------------------------------------------

Copyright (c) 2025 Yousf Al Salti. All rights reserved.
-----------------------------------------------------
"""

import pygame

class my_Object:
    object_count=0
    def __init__(self,color,filled):
        my_Object.object_count += 1
        self.object_id = my_Object.object_count
        self.color=color
        self.filled=filled

    def get_color(self):
        return self.color

    def get_filled(self):
        return self.filled

        pass
    def describe(self):
        print(f"Object #{self.object_id} is {self.color} and {'filled' if self.filled else 'not filled' }")

class my_Circle(my_Object):
    def __init__(self,color, filled, radius):
        super().__init__(color,filled)
        self.radius=radius
        self.x_pos = 0
        self.y_pos = 0
        self.vx = 0
        self.vy = 0
        pass
    #Seting the position of the center
    def set_position(self,x_pos=0,y_pos=0):
        self.x_pos=x_pos
        self.y_pos=y_pos
    #setting the velocity of the center
    def set_velocity(self,vx=0,vy=0):
        self.vx=vx
        self.vy=vy

    #moves the ball a given amount
    def move(self,dt):
        self.x_pos+=self.vx*dt
        self.y_pos+=self.vy*dt

    #Coordinates of the ball
    def get_position(self):
        return self.x_pos,self.y_pos
    def get_velocity(self):
        return self.vx,self.vy

    #getter functions for attributes
    def get_radius(self):
        return self.radius


    def describe(self):
        print(f"Circle #{self.object_id} is {self.color} and {'filled' if self.filled else 'not filled' } with radius {self.radius}")
    pass


class my_Rectangle(my_Object):
    def __init__(self,color,filled,length,width):
        super().__init__(color,filled)
        self.length=length
        self.width=width
        self.x_pos = 0
        self.y_pos = 0
        self.vx = 0
        self.vy = 0
    #setters
    def set_xpos(self,x_pos=0):
        self.x_pos=x_pos

    def set_ypos(self,y_pos=0):
        self.y_pos=y_pos

    def set_vx(self,vx=0):
        self.vx=vx

    def set_vy(self,vy=0):
        self.vy=vy

    def set_width(self,width):
        self.width=width

    def set_length(self,length):
        self.length=length

    #getters
    def get_xpos(self):
        return self.x_pos

    def get_ypos(self):
        return self.y_pos

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length
    #move methods
    def move_x(self,dx):
        self.x_pos+=dx
    def move_y(self,dy):
        self.y_pos+=dy


def main():
    print("Hello World!")


    pass

if __name__ == "__main__":
    main()