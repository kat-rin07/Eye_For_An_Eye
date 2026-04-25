import pygame
import sys

# 1. Setup - This happens once
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My RPG Game")

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Game Clock (controls how fast the game runs)
clock = pygame.time.Clock()


def main():
    running = True

    # 2. The Game Loop
    while running:
        # Check for events (clicks, key presses)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 3. Logic - This is where you'll update player positions later

        # 4. Drawing
        screen.fill(BLUE)  # Fill the background

        # (This is where you'll draw your player and UI later)

        pygame.display.flip()  # Update the screen

        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()