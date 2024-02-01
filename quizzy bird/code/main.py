import sys, time, pygame
 
from stuff import *
from sprites import Background, bird, obstacle, timer, menu

class Game:
    def __init__ (self):
        pygame.init() 
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Quizzy Bird")
        self.clock = pygame.time.Clock()
        self.active = True # check if the player is playing

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        #scaling
        background_height = pygame.image.load('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/enviroment/backgroundcute.png').get_height()
        self.sf = (WINDOW_HEIGHT / background_height)

        # sprite setup
        Background(self.all_sprites,self.sf)
        self.bird = bird(self.all_sprites,self.sf)
        self.timer = timer(self.all_sprites,self.sf)

        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer,1500)
        
        self.font = pygame.font.Font('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/font.ttf',30)
        self.score = 0

        #menu
        self.menu_surf = pygame.image.load('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/menu.png').convert_alpha()
        self.actual_menu_surf = pygame.transform.scale(self.menu_surf,(100,100))
        self.menu_rect = self.actual_menu_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

        #score card
        #self.card_surf = pygame.image.load('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/card2.png').convert_alpha()
        #self.actual_card_surf = pygame.transform.scale(self.card_surf,(100,100))
        #self.card_rect = self.actual_card_surf.get_rect(center = (50,600))

        # background music
        self.background_music = pygame.mixer.Sound('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/sound/background.wav')
        self.background_music.play(loops = -1)

    def collisions(self):
        if pygame.sprite.spritecollide(self.bird,self.collision_sprites,False):
            self.active = False
            self.bird.kill()
        if round(self.bird.rect.y) == 700:
            self.active = False
            self.bird.kill()
    
    #timer
    def display_score(self):
        if self.active:
            self.score = round(pygame.time.get_ticks()/1500) 
            x = 103
            y = 595
        else:
            x = 600   
            y =  200
            self.font = pygame.font.Font('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/graphics/font.ttf',100)
            self.timer.kill()

        score_surf = self.font.render(str(self.score),True,'black')
        score_rect = score_surf.get_rect(bottomleft = (x,y))
        self.display_surface.blit(score_surf,score_rect)
        
    
    # while it's running 
    def run(self):
        last_time = time.time()
        while True:

            delta_time = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()   
                if (event.type == self.obstacle_timer):
                    obstacle([self.all_sprites,self.collision_sprites],self.sf)
      
            self.all_sprites.update(delta_time)
            self.all_sprites.draw(self.display_surface)
            #self.display_surface.blit(self.card_surf,self.card_rect)
            self.display_score()
            if self.active: 
                self.collisions() 
            else:
                #self.display_surface.blit(self.menu_surf,self.menu_rect)
                menu(self.all_sprites,self.sf)
            pygame.display.update()
            self.clock.tick(FRAME_RATE)
            #background_music = pygame.mixer.Sound('/Users/isabellee/Desktop/Compsci/VS Code/AP/Midyear/quizzy bird/sound/background.wav').convert
            #pygame.mixer.Sound.play(background_music)
 
if __name__ == '__main__':
        game = Game()
        game.run()



