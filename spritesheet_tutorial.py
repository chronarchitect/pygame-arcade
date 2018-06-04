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
        self.walking_frames_l = sprite_sheet.load_strip([0, 0, 50, 62], 4, colorkey=WHITE)

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

