import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Chase Light in Pygame")

# Create a semi-transparent surface for the light effect
light_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
light_color = (255, 255, 0, 200)  # RGBA color with partial transparency

# Define obstacle rectangles
obstacle1 = pygame.Rect(200, 200, 100, 100)
obstacle2 = pygame.Rect(450, 350, 150, 50)
obstacle3 = pygame.Rect(600, 200, 100, 100)

# Initialize robot position and speed
robot_x, robot_y = 100, 100
robot_speed = 0.3

# Light source position
light_x, light_y = 700, 500

# Main game loop
running = True
No_obstruction = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the light surface
    light_surface.fill((0, 0, 0, 0))

    # Calculate the angle to the light source
    dx = light_x - robot_x
    dy = light_y - robot_y
    angle = math.atan2(dy, dx)

    # Move the robot towards the light source while avoiding obstacles
    if No_obstruction:
        robot_x += robot_speed * math.cos(angle)
        robot_y += robot_speed * math.sin(angle)

    # Check for collisions with obstacles
    if obstacle1.colliderect(pygame.Rect(robot_x+5 , robot_y+5 , 20, 20 )):
        No_obstruction = False
       # Calculate the distances from the robot to each edge of obstacle1
        left_distance = abs(robot_x - obstacle1.left)
        right_distance = abs(robot_x - obstacle1.right)
        top_distance = abs(robot_y - obstacle1.top)
        bottom_distance = abs(robot_y - obstacle1.bottom)

        if min(left_distance, right_distance, top_distance, bottom_distance) == left_distance:
            robot_y += robot_speed * math.sin(angle)
            print(f"Distance from the obstacle1: {left_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == right_distance:
            robot_y += robot_speed * math.sin(angle)
            print(f"Distance from the obstacle1: {right_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == top_distance:
            robot_x += robot_speed*math.cos(angle)
            print(f"Distance from the obstacle1: {top_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == bottom_distance:
            robot_x += robot_speed*math.cos(angle)
            print(f"Distance from the obstacle1: {bottom_distance}")

    elif obstacle2.colliderect(pygame.Rect(robot_x +5 , robot_y+5 , 20, 20)):
        No_obstruction = False
       # Calculate the distances from the robot to each edge of obstacle2
        left_distance = abs(robot_x - obstacle2.left)
        right_distance = abs(robot_x - obstacle2.right)
        top_distance = abs(robot_y - obstacle2.top)
        bottom_distance = abs(robot_y - obstacle2.bottom)

        if min(left_distance, right_distance, top_distance, bottom_distance) == left_distance:
            robot_y += robot_speed * math.sin(angle)
            print(f"Distance from the obstacle2: {left_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == right_distance:
            robot_y += robot_speed * math.sin(angle)
            print(f"Distance from the obstacle2: {right_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == top_distance:
            robot_x += robot_speed*math.cos(angle)
            print(f"Distance from the obstacle2: {top_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == bottom_distance:
            robot_x += robot_speed*math.cos(angle)
            print(f"Distance from the obstacle2: {bottom_distance}")

    elif obstacle3.colliderect(pygame.Rect(robot_x-10 , robot_y-10 , 20, 20)):
        No_obstruction = False
       # Calculate the distances from the robot to each edge of obstacle3
        left_distance = abs(robot_x - obstacle3.left)
        right_distance = abs(robot_x - obstacle3.right)
        top_distance = abs(robot_y - obstacle3.top)
        bottom_distance = abs(robot_y - obstacle3.bottom)

        if min(left_distance, right_distance, top_distance, bottom_distance) == left_distance:
            robot_y += robot_speed * math.sin(angle)
            print(f"Distance from the obstacle3: {left_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == right_distance:
            robot_y += robot_speed * math.sin(angle)
            print(f"Distance from the obstacle3: {right_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == top_distance:
            robot_x += robot_speed*math.cos(angle)
            print(f"Distance from the obstacle3: {top_distance}")
        elif min(left_distance, right_distance, top_distance, bottom_distance) == bottom_distance:
            robot_x += robot_speed*math.cos(angle)
            print(f"Distance from the obstacle3: {bottom_distance}")

    else:
        No_obstruction = True
        print(f"Distance from light sourse: {((light_x - robot_x)**2 + (light_y - robot_y)**2)**(0.5)}")


    screen.fill(BLACK)

    # Draw the light source
    pygame.draw.circle(light_surface, light_color, (int(light_x), int(light_y)), 30)

    # Draw obstacles
    pygame.draw.rect(screen, WHITE, obstacle1)
    pygame.draw.rect(screen, WHITE, obstacle2)
    pygame.draw.rect(screen, WHITE, obstacle3)


    # Draw the robot
    robot = pygame.image.load('car60_40.png')
    robot = pygame.transform.scale(robot, (30, 30))
    screen.blit(robot, (int(robot_x) - 10, int(robot_y) - 10))

    # Blit the light surface onto the screen
    screen.blit(light_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)  # Additive blending

    if abs(robot_x-light_x)<1 and abs(robot_y-light_y)<1:
        print("Light Sourse Reached")
        running = False

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()




