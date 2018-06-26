import pygame
import constants

class Gun(pygame.sprite.Sprite):
    """
    This is the player
    """
    def __init__(self, color, width, height):
        """ Constructor """
        super().__init__()

        # Create the surface of the block
        self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        # Draw the image onto the surface
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

    def move(self, direction):
        if direction == 'left':
            self.change_x = -3
        elif direction == 'right':
            self.change_x = 3
        elif direction == 'up':
            self.change_y = -3
        elif direction == 'down':
            self.change_y = 3
    
    def stop(self, direction):
        if direction == 'left' or direction == 'right':
            self.change_x = 0
        elif direction == 'up' or direction == 'down':
            self.change_y = 0

    def update(self):
        self.rect.x = self.rect.x + self.change_x
        self.rect.y = self.rect.y + self.change_y
        if self.rect.bottom > constants.SCREEN_HEIGHT:
            self.rect.bottom = constants.SCREEN_HEIGHT
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.right > constants.SCREEN_WIDTH:
            self.rect.right = constants.SCREEN_WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

class Bullet(pygame.sprite.Sprite):
    """
    This is the bullet
    """
    def __init__(self, color, width, height):
        """ Constructor """
        super().__init__()

        # Create the surface of the block
        self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        # Draw the image onto the surface
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def update(self):
        """ Called every frame """
        self.rect.x += 3

pygame.init()

# Set the width and height of the screen [width, height]
size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Gun")

#Initializing everything here
bullet_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

gun = Gun(constants.BLUE, 20, 15)
all_sprites_list.add(gun)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(constants.BLACK, 5, 5)
                bullet.rect.x = gun.rect.x
                bullet.rect.y = gun.rect.y
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
            elif event.key == pygame.K_w:
                gun.move('up')
            elif event.key == pygame.K_s:
                gun.move('down')
            elif event.key == pygame.K_d:
                gun.move('right')
            elif event.key == pygame.K_a:
                gun.move('left')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                gun.stop('up')
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                gun.stop('left')

    # --- Game logic should go here
    all_sprites_list.update()

    #Calculate mechanics for each bullet
    for bullet in bullet_list:
        if bullet.rect.x > constants.SCREEN_WIDTH:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
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
