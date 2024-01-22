
import pygame, sys, random
#tao func
def draw_mm():
    screen.blit(mm,(mm_x_pos,-70)) 
    screen.blit(mm,(mm_x_pos+900,-70)) 
def create_pip():
    random_pip_pos = random.choice(pip_height)
    bottom_pip = pip_surface.get_rect(midtop = (800,random_pip_pos))
    top_pip = pip_surface.get_rect(midtop =(800,random_pip_pos-1020))
    return bottom_pip,top_pip 
def move_pip(pips):
    for pip in pips:
        pip.centerx -= 5
    return pips  
def draw_pip(pips):
    for pip in pips:
        if pip.bottom >= 730:
            screen.blit(pip_surface,pip)
        else:
            flip_pip = pygame.transform.flip(pip_surface,False,True)
            screen.blit(flip_pip,pip)
def check_collision(pips):

        

       
    for pip in pips:
        if iron_rect.colliderect(pip):
            hit_sound.play()
            return False 
    if iron_rect.top <= -75 or iron_rect.bottom >= 1020:
       return False
    return True   
def rotate_iron(iron1):  
    new_iron = pygame.transform.rotozoom(iron1,iron_movement,1)
    return new_iron
def iron_animation():
    new_iron = iron_list[iron_index]
    new_iron_rect=new_iron.get_rect(center=(300,iron_rect.centery))
    return new_iron, new_iron_rect
def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int((score))),True,(255,255,255))
        score_rect = score_surface.get_rect(center=(450,100))
        screen.blit(score_surface,score_rect)
    if game_state == 'game over':
         score_surface = game_font.render(f'score: {int(score)}',True,(255,255,255))
         score_rect = score_surface.get_rect(center=(450,100))
         screen.blit(score_surface,score_rect) 
         high_score_surface = game_font.render(f' Highscore: {int(high_score)}',True,(255,255,255))
         high_score_rect = high_score_surface.get_rect(center=(450,500))
         screen.blit(high_score_surface,high_score_rect)
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2,buffer=512)       
pygame.init()
screen= pygame.display.set_mode((900,730))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.TTF', 40)
# tao conts
g = 0.5
iron_movement = 0
game_active = True
score = 0
high_score = 0
#bg
bg = pygame.image.load('assets/a.png').convert()
#fl
mm = pygame.image.load('assets/c.png')
mm_x_pos=-60
#iron
iron1 = pygame.image.load('assets/ir.png').convert_alpha()
iron2 = pygame.image.load('assets/hu.png').convert_alpha()
iron3 = pygame.image.load('assets/ha.png').convert_alpha()
iron_list = [iron1,iron2,iron3]
#012
iron_index = 0
iron = iron_list[iron_index]
iron_rect=iron.get_rect(center=(300,384))
#timer cho iron
ironfly = pygame.USEREVENT + 1
pygame.time.set_timer(ironfly,1200)
#tao_ong
pip_surface = pygame.image.load('assets/u.png').convert()
pip_list = []
#tao_time
spawnpip=pygame.USEREVENT
pygame.time.set_timer(spawnpip,1200)
pip_height = [300, 350, 400, 450]
#end game
game_over_surface = pygame.image.load('assets/ir.png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(450,365))
#chen sound
fly_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown =100
#while loop game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys. exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    iron_movement = 0
                    iron_movement = -9
                    fly_sound.play()
                if event.key == pygame.K_SPACE and game_active==False: 
                     game_active = True 
                     pip_list.clear()
                     iron_rect,center = (300,384)
                     iron_movement = 0
        if event.type == spawnpip:
            pip_list.extend(create_pip())
        if event.type == ironfly:
            if iron_index <2:
                iron_index +=1
            else:
                iron_index =0    
            iron, iron_rect = iron_animation()                         
        screen.blit(bg,(-500,-250))
        if game_active:
             #chim
            iron_movement += g
            rotated_iron = rotate_iron(iron)
            iron_rect.centery += iron_movement
            screen.blit(rotated_iron,iron_rect)
            game_active=check_collision(pip_list)
            #ống
            pip_list = move_pip(pip_list)
            draw_pip(pip_list)
            score +=0.01
            score_display('main game')
            score_sound_countdown -=1
            if score_sound_countdown<=0:
                score_sound.play()
                score_sound_countdown=100
        else:
            screen.blit(game_over_surface,game_over_rect)
            score_display('main_over')
           
           
             
        
        
        #sàn
        mm_x_pos-=1 
        draw_mm()
        if mm_x_pos <= -900:
            mm_x_pos =0
        pygame.display.update()
        clock.tick(120)
       
  