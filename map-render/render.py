import pygame
import constants
import os
from spritesheet import SpriteSheet

# Get level map from file
file_in = open('MAP')
maps = file_in.read().split()

# Initialize pygame
pygame.init()


# Making a sprite block class
class Block(pygame.sprite.Sprite):
    """
    This class represents the sprite
    """

    def __init__(self, color, width, height):
        """ Constructor, accepts the color
        and dimensions of the block """

        super().__init__()

        sprite_sheet = SpriteSheet('lol.png')
        #Create an image of the block
        picture = sprite_sheet.image_at([0, 0, 20, 20])
        picture = pygame.transform.scale(picture, (width, height))
        self.image = picture

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position by setting the values of
        # rect.x and rect.y
        self.rect = self.image.get_rect()

all_sprites_list = pygame.sprite.Group()

# Set the width and height of the screen [width, height]
size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

x_var = 0
y_var = 0

for line in maps:
    x_var = 0
    for char in line:
        if char == 'W':
            wall = Block(constants.RED, 40, 40)

            wall.rect.x = x_var
            wall.rect.y = y_var

            all_sprites_list.add(wall)
        x_var += 40
    y_var += 40


pygame.display.set_caption("Level Map")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(constants.WHITE)
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
