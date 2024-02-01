# import the pygame module 
import pygame, sys, time
import random
import os
  
# Define the background colour 
# using RGB color coding. 
lgrey = (255, 245, 252)
vlight_pink = (255, 219, 245)
light_pink = (245, 196, 231) 
light_pink_2 = (245, 181, 227)
medium_pink = (245, 152, 219)
WIDTH = 100
HEIGHT = 100

class Bird(pygame.sprite.Sprite): 
    def __init__(self, color, height, width): 
        super().__init__() 
  
        self.image = pygame.Surface([width, height]) 
        self.image.fill(medium_pink) 
        self.image.set_colorkey(lgrey) 
  
        pygame.draw.rect(self.image, 
                         color, 
                         pygame.Rect(0, 0, width, height)) 
  
        self.rect = self.image.get_rect() 

    def space_bar(self):
        key = pygame.key.get_pressed()
        dist = -15
        if key[pygame.K_SPACE]:
            bird.rect.y += dist
    
    def game_over(self):
        if(bird.rect.y == 700):
            return False
        
         
pygame.init()
  
# Define the dimensions of 
# screen object(width,height) 
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode((1300, 700)) 
  
# Set the caption of the screen 
pygame.display.set_caption('quizzy bird!') 
all_sprites = pygame.sprite.Group()

bird = Bird(medium_pink,50,50)
bird.rect.x = 100
bird.rect.y = 250
all_sprites.add(bird)  
  
exit = True
clock = pygame.time.Clock() 

  
while exit:  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = False
    
    if(bird.game_over() == False):
        bird.rect.y = 350
        pygame.quit() # change to smth else later
    else:
        bird.rect.y += 3
        bird.space_bar()
        all_sprites.update() 
        screen.fill(light_pink) 
        all_sprites.draw(screen) 
    
    pygame.display.flip() 
    clock.tick(60) 
  
pygame.quit() 
# Fill the background colour to the screen 



