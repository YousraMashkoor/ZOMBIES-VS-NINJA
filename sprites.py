#all sprites
import pygame
import random
from graphics import *
from initials import *

#defining vector
vec=pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game=game
        pygame.sprite.Sprite.__init__(self)
        #loading image
        
        self.image=pygame.transform.scale(ninja_image.convert(),(50,94))
        self.image.set_colorkey(purple)
        
        self.rect=self.image.get_rect()
        self.rect.center=(100,height/2)
        self.pos=vec(100,height/2)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
        self.k=0
        #self.speedx=0
        #self.speedy=0

    def shoot(self):
        self.bullet=bullet(self,self.rect.centerx,self.rect.left)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
        
    def jump(self):
        hits=pygame.sprite.spritecollide(self,self.game.floors,False)
        if hits:
            self.vel.y = -20
        #velcity to jump in y direction

    def update(self):
        self.acc=vec(0,player_g)
        self.k=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.acc.x=-player_acc
            self.k=-1
        if keystate[pygame.K_RIGHT]:
            self.acc.x=player_acc
            self.k=1
##        if keystate[pygame.K_SPACE]:
##            self.bullet=bullet(self.game,self.rect.centerx,self.rect.left)
##            self.game.all_sprites.add(self.bullet)
##            self.game.bullets.add(self.bullet)


        if self.rect.bottom<height-80:
            self.speedy=5
        if self.rect.bottom>height-10:
            self.rect.bottom=height-10

        #equations of motions
        #v=at
        #s=vit+1/2at^2
        self.acc.x +=self.vel.x * player_friction
        self.vel+=self.acc
        self.pos+=self.vel+(0.5*self.acc)

        #wrapping around adges

        if self.pos.x>width:
            self.pos.x=width
        if self.pos.x<0:
            diff=self.pos.x-0
            self.pos.x-=diff

        self.rect.midbottom=self.pos

class floor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        if x==0:
            self.image=pygame.transform.scale(floor1_image.convert(),(WIDTH,40))
            self.image.set_colorkey(white)
        else:
            self.image=pygame.transform.scale(floor2_image.convert(),(128,50))
            self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Zombie(pygame.sprite.Sprite):
    def __init__(self,game,x,w,h,s):
        self.game=game
        pygame.sprite.Sprite.__init__(self)

        if w==40:
            self.image=pygame.transform.scale(zombie1_image.convert(),(78,94))
            self.image.set_colorkey(black)
        else:
            self.image=pygame.transform.scale(zombie2_image.convert(),(298,458))
            self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        pos=self.game.player.rect.right+random.choice([width/2+random.randrange(20,50),-width/2+random.randrange(-50,-20)])
        if pos<0:
            self.rect.right=pos
        else:
            self.rect.left=pos
        self.rect.y=x
        self.speedx=s


    def update(self):

        #moving towards the player
        if self.game.player.rect.right <= self.rect.left:
            self.rect.x-=self.speedx
        if self.game.player.rect.left >= self.rect.right:
            self.rect.x+=self.speedx

        
         #if hit:
##        test=pygame.sprite.Group()
##        zoom=self.game.Bzombie
##        for zoom in range(zoom,self.game.zombies):
##            for zom in self.game.zombies:
##                if zoom==zom:
##                    continue
##                else:
##                    test.add(zom)
##            hits=pygame.sprite.spritecollide(zoom,test,False)
##            if hits:
##                if zoom.rect.x>self.game.player.rect.x:
##                    zoom.rect.right+=50
            #    if zoom.rect.centerx==zom.rect.centerx:
             #       if zoom.rect.x>self.game.player.rect.x:
              #          zoom.rect.x-=50
class bullet(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game=game
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(bullet_image.convert(),(60,16))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.centery=y
        K=1
        if not self.game.player.k == 0:
            K=self.game.player.k
            
        if K == -1:
            self.speedx=-10
        if K == 1:
            self.speedx=10
    def update(self):
        
        self.rect.x+=self.speedx
        #kill the bullet if out of screeen
        if self.rect.left<0 or self.rect.right>WIDTH:
            self.kill()


    
