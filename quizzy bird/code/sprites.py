import pygame

from stuff import *
from random import choice,randint

# moves in the background
class Background(pygame.sprite.Sprite):
    def __init__(self, groups, sf):
        super().__init__(groups)
        background_image = pygame.image.load('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/enviroment/backgroundcute.png').convert()

        fh = background_image.get_height() * sf
        fw = background_image.get_width() * sf
        normal_image = pygame.transform.scale(background_image, (fw, fh))

        self.image = pygame.Surface((fw*2, fh))  # now it's twice as wide
        self.image.blit(normal_image, (0, 0))
        self.image.blit(normal_image, (fw, 0))

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, delta_time):
        #self.pos.x -= 200 * delta_time

        #if self.rect.centerx <= 700:
          #  self.pos.x = 0
        self.rect.x = round(self.pos.x)

class bird(pygame.sprite.Sprite):
    def __init__(self, groups, sf) -> None:
        super().__init__(groups)

        #flapping
        self.import_frames(sf)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        self.rect = self.image.get_rect(midleft = (WINDOW_WIDTH/8, WINDOW_HEIGHT/3))
        self.pos = pygame.math.Vector2(self.rect.midleft)
        

        # up and down
        self.direction = 0

        #jump sound
        #self.sound = pygame.mixer.Sound('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/sound/jump.wav')
        #self.sound.set_volume(0.3)

    def import_frames(self,sf):
        self.frames = []

        i = 0
        for i in range(3):
            seen_image = dbird_image = pygame.image.load(f'/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/bird/bird{i}.png').convert_alpha()
            scaled_bird = pygame.transform.scale(seen_image,pygame.math.Vector2(seen_image.get_size())*5)
            self.frames.append(scaled_bird)
    
    def space_bar(self):
        key = pygame.key.get_pressed()
        dist = -7
        if key[pygame.K_SPACE]:
            self.pos.y += dist
            #self.sound.play()
    
    def animate(self,delta_time):
        self.frame_index += 5 * delta_time
        if self.frame_index >= len(self.frames):
            self.frame_index = 0;  
        self.image = self.frames[int(self.frame_index)]
   
        
    def update(self, delta_time):
        self.space_bar()
        self.animate(delta_time)
        
        self.pos.y += 200 * delta_time
        self.rect.y = round(self.pos.y)

class obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, sf):
        super().__init__(groups)

        orientation = choice(('a','b'))
        ob = pygame.image.load(f'/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/obstacles/{choice((0,1,2))}.png').convert_alpha()
        self.image = pygame.transform.scale(ob,pygame.math.Vector2(ob.get_size())*sf*1.5)
        print(orientation)

        x = WINDOW_WIDTH + randint(40,100)
    
        if orientation == 'a':
            #upy = WINDOW_HEIGHT + randint(10,50)    
            self.rect = self.image.get_rect(midbottom = (x,720))
        else:
            downy = randint(-20,-5)
            print(downy)
            self.image = pygame.transform.flip(self.image, False,True) #ob,horizontal,vertical
            self.rect = self.image.get_rect(midtop = (x,downy))
    
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self,delta_time):
        self.pos.x -= 400 * delta_time
        self.rect.x = round(self.pos.x)
        if self.rect.right <= 0:
            self.kill()

class timer(pygame.sprite.Sprite):
    def __init__(self, groups, sf):
        super().__init__(groups)
        timer_image = pygame.image.load('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/card3.png').convert()
        self.image = pygame.transform.scale(timer_image,pygame.math.Vector2(timer_image.get_size())*4)
        self.rect = self.image.get_rect(bottomleft=(50, 600))
        self.pos = pygame.math.Vector2(self.rect.bottomleft)

    def update(self, delta_time):
        self.rect.x = round(self.pos.x)

    
class menu(pygame.sprite.Sprite):
    def __init__(self,groups,sf):
        super().__init__(groups)
        
        menu_image = pygame.image.load('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/menu.png').convert()
        self.image = pygame.transform.scale(menu_image,pygame.math.Vector2(menu_image.get_size())*11)
        self.rect = self.image.get_rect(midtop = (360, 200))
        self.pos = pygame.math.Vector2(self.rect.midtop)

    def update(self, delta_time):
        self.rect.x = round(self.pos.x)
            



            

            
        