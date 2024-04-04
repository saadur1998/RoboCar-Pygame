# Imports
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
ROBOT_SIZE = 30
ROBOT_SPEED = 0.5

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Robot Simulator")

#robot
robot = pygame.image.load('car60_40.png')
robot = pygame.transform.scale(robot, (ROBOT_SIZE, ROBOT_SIZE))

# Initialize robot position
robot_x = 100
robot_y = 100

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # Move the robot based on arrow key inputs
    if keys[pygame.K_UP]:
        print("UP-KEY")
        robot_y = max(0, robot_y - ROBOT_SPEED)
    if keys[pygame.K_DOWN]:
        print("DOWN-KEY")
        robot_y = min(HEIGHT - ROBOT_SIZE, robot_y + ROBOT_SPEED)
    if keys[pygame.K_LEFT]:
        print("LEFT-KEY")
        robot_x = max(0, robot_x - ROBOT_SPEED)
    if keys[pygame.K_RIGHT]:
        print("RIGHT_KEY")
        robot_x = min(WIDTH - ROBOT_SIZE, robot_x + ROBOT_SPEED)

    # Fill the background color
    screen.fill(BG_COLOR)

    # Draw the robot
    screen.blit(robot, (robot_x, robot_y))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()