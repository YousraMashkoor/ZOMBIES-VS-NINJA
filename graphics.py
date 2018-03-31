
#loading all of the images
import os
import pygame




game_folder=os.path.dirname(__file__)


#background image
bgimage_folder=os.path.join(game_folder,"img")
bg=pygame.image.load(os.path.join(bgimage_folder,"BG.png"))
bgl=pygame.image.load(os.path.join(bgimage_folder,"BG.png"))


#ninjas
ninja_image=pygame.image.load(os.path.join(game_folder,"img\\NinjaRun\\Idle__000.png"))


#zombie
zombie1_image=pygame.image.load(os.path.join(game_folder,"img\\Idle (15).png"))
zombie2_image=pygame.image.load(os.path.join(game_folder,"img\\Walk (2)-.png"))


#bullet
bullet_image=pygame.image.load(os.path.join(game_folder,"img\\Kunai.png"))

#floors
floor1_image=pygame.image.load(os.path.join(game_folder,"img\\Tile (2).png"))
floor2_image=pygame.image.load(os.path.join(game_folder,"img\\Tile (15).png"))






