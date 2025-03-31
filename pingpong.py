"""
-----------------------------------------------------
Author: Yousf Al Salti
Date: 31/03/2025
Time: 2:08 PM
Version: 1.0
-----------------------------------------------------

Filename: pingpong

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

from pingpong_classes import *


def main():
    pygame.init()

    pygame.display.set_caption("My PingPong")

    # Screen setup
    WIDTH, HEIGHT = 800, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Fonts setup
    font = pygame.font.Font(None, 36)

    #scores
    player_score = 0
    computer_score = 0
    rounds=1

    #Ball setup
    ball = my_Circle("yellow",True,10)
    ball.set_position(WIDTH//2,HEIGHT//2)
    ball.set_velocity(10,10)

    #Paddle setup
    paddle = my_Rectangle("white",True,50,10)
    paddle.set_xpos(WIDTH-50)
    paddle.set_ypos(HEIGHT//2-40)
    paddle.set_width(10)
    paddle.set_length(80)
    paddle.set_vy(10)
    paddle_velocity =0 # will be changed later

    #computer paddle setup
    computer_paddle = my_Rectangle("white",True,50,10)
    computer_paddle.set_xpos(50)
    computer_paddle.set_ypos(HEIGHT//2-40)
    computer_paddle.set_width(10)
    computer_paddle.set_length(80)
    computer_paddle.set_vy(5)
    computer_paddle_velocity = 0 # will be changed later during execution

    running = True
    while running:
        screen.fill("black")  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddle_velocity = -paddle.get_vy()
                elif event.key == pygame.K_DOWN:
                    paddle_velocity = paddle.get_vy()

            # Stop movement when key is released
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle_velocity = 0

        #move paddle
        paddle.move_y(paddle_velocity)
        # Keep the line within the screen
        paddle.set_ypos(max(0,min(HEIGHT-paddle.get_length(),paddle.get_ypos())))

        # minimizing the distance between computer paddle and ball (y distance)
        computer_paddle_velocity = ball.get_position()[1] - (computer_paddle.get_ypos() + computer_paddle.get_length()//2)

        #computer paddle motion
        computer_paddle.move_y(computer_paddle_velocity)
        #keep the line within the screen
        computer_paddle.set_ypos(max(0,min(HEIGHT-computer_paddle.get_length(),computer_paddle.get_ypos())))

        #move the ball
        ball.move(1)

        #ball collision with top and bottom walls
        if ball.get_position()[1]-ball.get_radius()<0 or ball.get_position()[1]+ball.get_radius()>HEIGHT:
            ball.set_velocity(ball.get_velocity()[0],-ball.get_velocity()[1])

        #ball collision with the left wall
        if ball.get_position()[0]-ball.get_radius()<0:
            ball.set_velocity(-ball.get_velocity()[0],ball.get_velocity()[1])

        #ball periodic boundary conditions on the sides
        """if ball.get_position()[0]-ball.get_radius()<0:
            ball.set_position(WIDTH-ball.get_radius(),ball.get_position()[1])

        if ball.get_position()[0]+ball.get_radius()>WIDTH:
            ball.set_position(ball.get_radius(),ball.get_position()[1])"""
        #ball boundary conditions and counter
        if ball.get_position()[0]+ball.get_radius()>WIDTH:
            ball.set_position(WIDTH//2,HEIGHT//2)
            ball.set_velocity(-ball.get_velocity()[0],-ball.get_velocity()[1])
            computer_score += 1
            print(f"Round {rounds} : Player Score = {player_score} , Computer Score = {computer_score}")

            rounds+=1
        elif ball.get_position()[0]-ball.get_radius()<0:
            ball.set_position(WIDTH//2,HEIGHT//2)
            ball.set_velocity(ball.get_velocity()[0], ball.get_velocity()[1])
            player_score += 1
            print(f"Round {rounds} : Player Score = {player_score} , Computer Score = {computer_score}")

            rounds+=1

        # ball collision with the paddle

        if (paddle.get_xpos()<= ball.get_position()[0] +ball.get_radius() <= paddle.get_xpos() + paddle.get_width()) and \
                (paddle.get_ypos() <= ball.get_position()[1]<= paddle.get_ypos() +paddle.get_length()):
            ball.set_velocity(-ball.get_velocity()[0],ball.get_velocity()[1])

        # ball collision with computer paddle
        if (computer_paddle.get_xpos()<= ball.get_position()[0] -ball.get_radius() <= computer_paddle.get_xpos() + computer_paddle.get_width()) and \
                (computer_paddle.get_ypos() <= ball.get_position()[1]<= computer_paddle.get_ypos() +computer_paddle.get_length()):
            ball.set_velocity(-ball.get_velocity()[0],ball.get_velocity()[1])

        #draw the elements
        pygame.draw.circle(screen,ball.get_color(),ball.get_position(),ball.get_radius())
        pygame.draw.rect(screen,paddle.get_color(),(paddle.get_xpos(),paddle.get_ypos(),paddle.get_width(),paddle.get_length()))
        pygame.draw.rect(screen,computer_paddle.get_color(),(computer_paddle.get_xpos(),computer_paddle.get_ypos(),computer_paddle.get_width(),computer_paddle.get_length()))
        pygame.draw.line(screen,"white",(WIDTH//2,0),(WIDTH//2,HEIGHT))
        pygame.draw.line(screen,"white",(0,0),(WIDTH,0),width=4)
        pygame.draw.line(screen, "white", (0, HEIGHT), (WIDTH, HEIGHT), width=4)

        # Render score text
        computer_score_text = font.render(f"Computer: {computer_score}", True, "white")
        player_score_text = font.render(f"Player: {player_score}", True, "white")
        screen.blit(computer_score_text, (20, 20))  # Draw text at (20,20)
        screen.blit(player_score_text,(WIDTH-140,20))

        pygame.display.flip()  # Update screen
        clock.tick(60)  # Limit FPS

    pygame.quit()

    pass

if __name__ == "__main__":
    main()