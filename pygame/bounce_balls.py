#Pygame bounce balls Demo Game
#Created By github.com/rajatbhatia1998

import pygame
import random

#Setting Up the pygme window elements
speed = [-2,-1,1,2,3,4,5,6]
height = 600
width = 800
black = (0,0,0)
display = pygame.display.set_mode([width,height])
clock = pygame.time.Clock()
ball_list = []
size = 30

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move_x = 0
        self.move_y = 0
        self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

def draw():
    ball = Ball()
    ball.x = random.randrange(size,width-size)
    ball.y = random.randrange(size,height-size) #Random choose loactions of ball
    ball.move_x = random.choice(speed)#Random default speed selection
    ball.move_y = random.choice(speed)
    return ball
    


def main():
    ball = draw() #creating a ball object
    ball_list.append(ball)#Appending object into list
    while True:
        display.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:#Creat a new ball when user press (Space key)
                if event.key == pygame.K_SPACE:
                    ball = draw()
                    ball_list.append(ball)
        
        
        for ball in ball_list:
            pygame.draw.circle(display,ball.color,[ball.x,ball.y],size)
        for ball in ball_list:
            #Moving of ball X and Y axis
            ball.x += ball.move_x 
            ball.y += ball.move_y
            #Identifying The corners of the screen
            if ball.x < size or ball.x >width-size :
                ball.move_x *=-1
            if ball.y < size or ball.y > height-size:
                ball.move_y *= -1
        
        clock.tick(60)
        pygame.display.update()
if __name__ == "__main__":
    main()


'''This program need the pygme module pls ensure it must be installed before Executing  the program/
CLI:-pip install pygame'''
