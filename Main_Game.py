import pygame
import random
import os
from initials import *
from sprites import *
from graphics import *
from records import *
import inputbox

class game:

    def __init__(self):
        self.s_m=False
        self.screen_level=300
        #initializes pygame
        pygame.init()
        #initializes sound
        pygame.mixer.init()
        #set our display at screen
        self.screen=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
        #set captions
        pygame.display.set_caption(title)
        self.clock=pygame.time.Clock()
        #saves atahe location where our python is installed
        #self.game_folder=os.path.dirname(__file__)
        self.game_folder=game_folder
        #loading background location
        self.bgimage_folder=bgimage_folder
        self.bg=bg.convert()
        self.bgx=0
        #testing width
        self.TW=width/2
        self.running=True
        self.die=0
        #matching font from setup
        self.font=pygame.font.match_font(font_name)
        #self.Bzombie=Zombie(self,300,width/3,height/3,1)
        #initializing record
        self.record=record()

    def new(self):
        #start a new game
        self.score=0
        self.die=0
        self.screen_level=300
        self.TW=width/2
        self.all_sprites=pygame.sprite.Group()
        self.floors=pygame.sprite.Group()
        self.zombies=pygame.sprite.Group()
        self.big_guy=pygame.sprite.Group()
        self.bullets=pygame.sprite.Group()

        self.mob_time=0
        self.bs=floor(base[0],base[1])
        self.all_sprites.add(self.bs)
        self.floors.add(self.bs)        
        for flr in floor_list:
            self.f=floor(flr[0],flr[1])
            self.all_sprites.add(self.f)
            self.floors.add(self.f)
        self.player=Player(self)
        self.all_sprites.add(self.player)
        self.name = inputbox.ask(self.screen, " Name")

        self.run()

    def run(self):
        #game loop
        self.playing=True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()
        

    def update(self):
        
        #game loop-update

            
        #zombies
        now=pygame.time.get_ticks()
        
        if self.player.rect.right>=width/2 and len(self.zombies)<15:
            now=pygame.time.get_ticks()
            if now-self.mob_time>5000+random.choice([-1000,-500,0,500,1000]):
                self.mob_timer=now                
                self.zombie=Zombie(self,height-130,40,40,random.choice([0.5,1,2,3,0.3]))
                self.zombies.add(self.zombie)
                self.all_sprites.add(self.zombie)
                
        if self.player.rect.right>=width/2 and mob_freq<now+self.mob_time and len(self.big_guy)<1:
            self.Bzombie=Zombie(self,200,width/3,height/3,1)
            self.all_sprites.add(self.Bzombie)
            self.big_guy.add(self.Bzombie)
            
        self.all_sprites.update()
        self.big_guy.update()
        #if self.bs.rect.left<0:
         #  pos=0-self.bs.rect.left
           # self.ds=floor(pos,base[1],base[2],base[3])
            #self.all_sprites.add(self.ds)
            #self.floors.add(self.ds)
        #move character left and right with the screen
        if (self.player.rect.right>=width/2 and self.TW<=(2*width)+(width/2)) or (self.player.rect.right<=width/2 and self.s_m):
                    self.s_m=True
                    diff = self.player.rect.right-width/2
                    self.screen_level+=diff
                    self.TW+=diff
                    #specifying the screen limit
                    if self.screen_level>=300 :
                        self.player.pos.x-=diff
                        #self.player.vel.y = 0
                        for flr in self.floors:
                            flr.rect.x-=diff
                        for zoom in self.zombies:
                            zoom.rect.x-=diff
                        for z in self.big_guy:
                            z.rect.x-=diff
                    #reset the screen limit for the next round
                    if self.screen_level<=300:
                        self.screen_level=300
                    if self.TW<=width/2:
                        self.TW=width/2
        #if bullet hit zombie
        colisn=pygame.sprite.groupcollide(self.zombies,self.bullets,True,True)
        if colisn:
            self.score+=10

        #if 20 bullet hit big guy
        hit_chan=pygame.sprite.groupcollide(self.big_guy,self.bullets,False,True)
        if hit_chan:
            self.die+=1
        if self.die>20:
            for b in self.big_guy:
                b.kill()
                self.score+=100
                self.die=0
               # self.Bzombie=Zombie(self,300,width/3,height/3,1)
                #self.all_sprites.add(self.Bzombie)
               # self.big_guy.add(self.Bzombie)
            
        
        #if zombie hit player
        colisn=pygame.sprite.spritecollide(self.player,self.zombies,False)
        if colisn:
            self.playing=False
            #polymorphism
            for p in self.all_sprites:
                p.kill()
        colisn=pygame.sprite.spritecollide(self.player,self.big_guy,False)
        if colisn:
            self.playing=False
            #polymorphism
            for p in self.all_sprites:
                p.kill()
            

        #respowning new random floors
        while len(self.floors)<3:
            w=random.randrange(100,200)
            f=floor(random.randrange(width+10,width+15),
                    random.randrange(height-100,height-60))
            self.floors.add(f)
            self.all_sprites.add(f)
 

            
        #land on floor  only if player is falling
        if self.player.vel.y>0:
            # if player comes in contact with the floor.... false as to dont
            # destroy the objects
            contact = pygame.sprite.spritecollide(self.player, self.floors, False)
            if contact:
                if self.player.pos.y<contact[0].rect.bottom:
                    self.player.pos.y = contact[0].rect.top + 1
                    # setting vel to zero so our character stops moving permanently
                    self.player.vel.y = 0
                

    def events(self):
        #game loop-event
        for event in pygame.event.get():
        
        #clossing window
            if event.type==pygame.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False

        #clasing the resized window
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    if self.playing:
                        self.playing=False
                    self.running=False
                if event.key==pygame.K_SPACE:
                    self.bullet=bullet(self,self.player.rect.centerx,self.player.rect.centery)
                    self.all_sprites.add(self.bullet)
                    self.bullets.add(self.bullet)
                if event.key==pygame.K_UP:
                    self.player.jump()


    def draw(self):
        #game loop-draw
        self.screen.fill(black)

        #moving our background to an
        #infinite loop
        self.rel_x=self.bgx % self.bg.get_rect().width
        self.screen.blit(self.bg ,(self.rel_x - self.bg.get_rect().width,-300))
        if self.rel_x<width:
            self.screen.blit(self.bg,(self.rel_x,-300))
        if self.player.k==1:
            self.bgx-=1
        if self.player.k==-1:
            self.bgx+=1

        #drawing our player on the screen
        self.all_sprites.draw(self.screen)

        #drawing text
        self.draw_text(str(self.score),22,red,width/2,15)

                #flip after drawing
        pygame.display.flip()

    def show_menu_screen(self):
        self.bgx=0
        waiting =True
        while waiting:

            self.clock.tick(fps)
            #event
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    waiting=False
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_ESCAPE:
                        waiting=False
                        self.running=False
                    if event.key==pygame.K_p:
                        
                        waiting=False
                    if event.key==pygame.K_l:
                        self.leader_board()
                        
            #draw
            self.rel_x=self.bgx % self.bg.get_rect().width
            self.screen.blit(self.bg ,(self.rel_x - self.bg.get_rect().width,-300))
            if self.rel_x<width:
                self.screen.blit(self.bg,(self.rel_x,-300))
            self.bgx-=10        
            self.draw_text("Zombies VS Ninja",100,black,width/2,height/4)
            self.draw_text("Zombies              ",100,green,width/2,height/4)
            self.draw_text("                     Ninja",100,blue,width/2,height/4)
            self.draw_text("          VS    ",100,white,width/2,height/4)
            self.draw_text("PLAY(P)",53,white,width/2,height/2)
            self.draw_text("LEADER BOARD(L)",53,white,width/2,height/2+100)
            self.draw_text("QUIT(ESC)",53,white,width/2,height/2+200)
            pygame.display.flip()

        

    def show_over_screen(self):
        if not self.running:
            return
        self.record.add(self.name,self.score)
        self.record.show()
        self.bgx=0
        waiting =True
        while waiting:

            self.clock.tick(fps)
            #event
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    waiting=False
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_ESCAPE:
                        waiting=False
                        self.running=False
                    if event.key==pygame.K_p:
                        waiting=False
                    if event.key==pygame.K_m:
                        waiting=False
                        self.show_menu_screen()
                        return
            #draw
            self.rel_x=self.bgx % self.bg.get_rect().width
            self.screen.blit(self.bg ,(self.rel_x - self.bg.get_rect().width,-300))
            if self.rel_x<width:
                self.screen.blit(self.bg,(self.rel_x,-300))
            self.bgx-=10        
            self.draw_text("GAME OVER",150,black,width/2,height/4-100)
            self.draw_text(" GAME OVER",150,red,width/2,height/4-100)
            self.draw_text("SCORE: "+ str(self.score),62,blue,width/2,height/2)
            self.draw_text("PLAY AGAIN(P)",51,white,width/2,height/2+100)
            self.draw_text("MAIN MENU(M)",51,white,width/2,height/2+170)
            self.draw_text("QUIT(ESC)",51,white,width/2,height/2+240)
            pygame.display.flip()

    def leader_board(self):
        waiting=True
        while  waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    waiting=False
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_ESCAPE:
                        waiting=False
                        self.running=False
                    else:
                        waiting=False
                        return
            bglc=bgl.convert()
            bgl_rect=bglc.get_rect()
            self.screen.fill(blue)
            self.screen.blit(bglc,bgl_rect)
            self.draw_text("LEADER BOARD",100,blue,width/2,height/4-100)
            for i in range(len(self.record.names)):
                self.draw_text(str(self.record.names[i])+"         "+str(self.record.scores[i]),50,white,width/2,height/4+(i*50))
            self.draw_text("press any key to go back",43,black,width/2,height-100)
            
            pygame.display.flip()
    def draw_text(self,text,size,color,x,y):
        font=pygame.font.Font(self.font,size)
        #true for antialiasim
        text_surface=font.render(text,True,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface,text_rect)

g=game()
g.show_menu_screen()
while g.running:
    g.new()
    g.show_over_screen()

pygame.quit()
