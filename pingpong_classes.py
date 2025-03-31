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
    def position(self,x_pos=0,y_pos=0):
        self.x_pos=x_pos
        self.y_pos=y_pos
    #setting the velocity of the center
    def velocity(self,vx=0,vy=0):
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
    def get_color(self):
        return self.color
    def get_filled(self):
        return self.filled


    def describe(self):
        print(f"Circle #{self.object_id} is {self.color} and {'filled' if self.filled else 'not filled' } with radius {self.radius}")
    pass




def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    WIDTH, HEIGHT = 500, 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    #circle definition
    circle = my_Circle("red",True,25)
    circle.position(100,150)
    circle.velocity(10,10)
    running = True
    color=circle.get_color()
    x,y=circle.get_position()
    radius=circle.get_radius()
    while running:
        screen.fill((0, 0, 0))  # Clear screen with black
        pygame.draw.circle(screen, color, (x, y), radius)  # Draw circle
        pygame.display.flip()  # Update display

        # Move the circle
        circle.move(1)
        x,y=circle.get_position()
        vx,vy=circle.get_velocity()
        if x > WIDTH - radius or x < radius:
            vx=-vx
            circle.velocity(vx,vy)
        if y > HEIGHT - radius or y < radius:
            vy=-vy
            circle.velocity(vx,vy)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(30)  # Limit FPS

    pygame.quit()


    pass

if __name__ == "__main__":
    main()