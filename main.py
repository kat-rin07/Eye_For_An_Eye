import pygame
import sys
from scripts.player import Pip
from scripts.settings import WIDTH
from scripts.settings import HEIGHT
import os

# 1. Setup - This happens once
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("An Eye For An Eye")

# Game Clock (controls how fast the game runs)

# Colors
BLUE = (0, 0, 180)
WHITE = (255, 255, 255)




def main():
    print(f"Current Directory: {os.getcwd()}")
    print(f"Files in images folder: {os.listdir('assets/images')}")

    running = True

    all_sprites = pygame.sprite.Group()
    player = Pip((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    all_sprites.add(player)

    clock = pygame.time.Clock()  # because our character moves through time 0.o

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)  # mark to note later

    # get_width takes the width of the screen and divides by 2 same with height this helps us put the player in the middle

    # 2. The Game Loop
    while running:
        # set the clock stuff/delta time in seconds since last frame
        # used for framerate independent physics
        dt = clock.tick(60) / 1000  # Limit to 60 frames per second

        # Check for events (clicks, key presses)
        for event in pygame.event.get():
            #pygame.QUIT even means that the user clicked the 'X' to close the window
            if event.type == pygame.QUIT:
                running = False

        # 3. Logic - This is where you'll update player positions later


        # 4. Drawing
        screen.fill(BLUE)  # Fill the background

        # update
        all_sprites.update()
        all_sprites.draw(screen)

        # (This is where you'll draw your player and UI later)
        #pygame.draw.circle(screen, "#ffffff", player_pos, 40)

        keys = pygame.key.get_pressed() #defines key as a button to press

        #if keys[pygame.K_UP]: #uses pygame logic to define the up arrow key
        #     player_pos.y -= 300 * dt
        #if keys[pygame.K_DOWN]:
        #    player_pos.y += 300 * dt

        #if keys[pygame.K_LEFT]:
        #    player_pos.x -= 300 * dt
        #if keys[pygame.K_RIGHT]:
        #    player_pos.x += 300 * dt

        pygame.display.flip()  # Update the screen


    pygame.quit()

    sys.exit()


if __name__ == "__main__":
    main()