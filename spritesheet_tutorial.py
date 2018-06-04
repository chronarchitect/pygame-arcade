import pygame
import constants
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    """
    This class represents the sprite that the player controls
    """

#--- Methods
    def __init__(self):
        """
        Constructor
        """
        super().__init__()

#------ Attributes
        # Speed of the player
        self.change_x = 0
        self.change_y = 0

        #This list holds images for our player
        self.walking_frames_l = []
        self.walking_frames_r = []

        #Direction of walking
        self.direction = "R"

        sprite_sheet = SpriteSheet("walk_sheet2.png")
        #Load all the left facing images into a list
        self.walking_frames_l = sprite_sheet.load_strip([0, 0, 50, 62], 4, constants.WHITE)

        #Load all the left facing images then flip them right
        for image in self.walking_frames_l:
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_r.append(image)
        
        #Set the image tge player starts with
        self.image = self.walking_frames_r[0]

        #Set a reference to the image rect
        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player """
        self.rect.x += self.change_x
        pos = self.rect.x
        if self.direction == "R":
            frame = (pos//30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos//30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

    #Player controlled self movement
    def go_left(self):
        """ Called when user hits the left button """
        self.change_x = -6
        self.direction = "L"
    
    def go_right(self):
        """ Called when user hits the right button """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard """
        self.change_x = 0

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

    # This is the player
    player = Player()
    player.rect.x = 0
    player.rect.y = (constants.SCREEN_HEIGHT - 100)
    
    # This is a list of all sprites
    all_sprites_list = pygame.sprite.Group()

    # Adding the player to all sprites list
    all_sprites_list.add(player)

    # Loop until user wants to quit
    done = False

    # Used to manage FPS
    clock = pygame.time.Clock()

    #---- Main Program Loop
    while not done:
        #---- Catch events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                elif event.key == pygame.K_RIGHT:
                    player.go_right()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.stop()
        
        # Game logic
        # Calling the update method
        player.update()

        font = pygame.font.SysFont('Calibri', 25, True, False)
        position = "[ "+str(player.rect.x)+", "+str(player.rect.y)+"]"
        text = font.render(position, True, constants.WHITE)

        # Clearing the screen
        screen.fill(constants.BLACK)
        
        # Drawing code
        screen.blit(text, [30, 20])
        # We need a pygame.sprite,Group() object to draw sprites
        all_sprites_list.draw(screen)

        # Updating the display with what has been drawn
        pygame.display.flip()

        #Framerate limit
        clock.tick(60)

    # Close the window and quit
    pygame.quit()

if __name__ == '__main__':
    main()
