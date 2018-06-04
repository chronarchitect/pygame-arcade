"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
#import spritesheet

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
# Set the height and width of the screen
screen_width = 700
screen_height = 400

#initialize pygame
pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])

class spritesheet(object):

    def __init__(self, filename):
        """
        Constructor
        """
        #Call the parent class constructor
        super().__init__()

        #Fetch the image and set it as sprite surface
        self.sheet = pygame.image.load(filename).convert()
        
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    #Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]
    #Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(tups, colorkey)

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.index = 0
        self.image = images[self.index]
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.dir = "R"

    def update(self, pos):
        if self.rect.x % 10 == 0:
            self.index = (self.index + 1)%4

ss = spritesheet('walk_sheet2.png')
#Sprite is 50x62 pixels
images = ss.load_strip([ 0, 0, 50, 62], 4, colorkey=-1)

def main():
    # This is a list of 'sprites.' Each block in the program is
    # added to this list. The list is managed by a class called 'Group.'
    block_list = pygame.sprite.Group()
 
    # This is a list of every sprite. 
    # All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()
     
    """for i in range(50):
        # This represents a block
        block = Block(WHITE, 20, 20)
     
        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(screen_height)
     
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
    """ 
    # Create a player block
    player = Block()
    player.rect.x = 0
    player.rect.y = screen_height - 200
    all_sprites_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    score = 0
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.x_speed = -2
                elif event.key == pygame.K_RIGHT:
                    player.x_speed = 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.x_speed = 0
        
        block_list.update()

        # Clear the screen
        screen.fill(BLACK)
 
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
           # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        player.rect.x = player.rect.x + player.x_speed
        #player.rect.y
 
        # See if the player block has collided with anything.
        #blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True, pygame.sprite.collide_circle_ratio(0.5))
 
        # Check the list of collisions.
        """for block in blocks_hit_list:
            score += 1
            print(score)
        """
        # Draw all the spites
        all_sprites_list.draw(screen)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    pygame.quit()

if __name__ == "__main__":
    main()
