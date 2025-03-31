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

import matplotlib.pyplot as plt
class my_Object:
    object_count=0
    def __init__(self,color,filled):
        my_Object.object_count += 1
        self.object_id = my_Object.object_count
        self.color=color
        self.filled=filled

        pass
    def describe(self):
        print(f"Object #{self.object_id} is {self.color} and {'filled' if self.filled else 'not filled' }")

class my_Circle(my_Object):
    def __init__(self,color, filled, radius):
        super().__init__(color,filled)
        self.radius=radius
        self.x_pos = 0
        self.y_pos = 0
    #Seting the position of the center
    def position(self,x_pos=0,y_pos=0):
        self.x_pos=x_pos
        self.y_pos=y_pos

    #moves the ball a given amount
    def move(self,dx,dy):
        self.x_pos+=dx
        self.y_pos+=dy

    #Coordinates of the ball
    def get_position(self):
        return self.x_pos,self.y_pos

    #getter functions for attributes
    def get_radius(self):
        return self.radius
    def get_color(self):
        return self.color
    def get_filled(self):
        return self.filled


    def describe(self):
        print(f"Circle #{self.object_id} is {self.color} and {'filled' if self.filled else 'not filled' } with radius {self.radius}")
    pass

def main():
    circle=my_Circle(color="cyan",filled= True,radius=2)



    pass

if __name__ == "__main__":
    main()