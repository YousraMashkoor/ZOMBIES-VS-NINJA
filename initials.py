import os
#initials and constants

width=1300
WIDTH=3*width
height=660
fps=60
font_name='arial'

mob_freq=10000

#**************************player properties******************
player_acc=0.5
player_friction=-0.12
player_g=0.8


#*************************Starting platforms****************
floor_list=[(width/2,height-200),
            (WIDTH/4,height-150),
            (300,height-200),
            (width+300,height-130),
            (WIDTH/2,height-300),
            (WIDTH/3,height-200),
            (WIDTH-400,height-150),
            (WIDTH-900,height-140),
            (WIDTH-1200,height-180)]
base=(0,height-40)

#**************************colors satches***********************
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
pink=(255,0,255)
purple=(32,2,30)
yellow=(255,255,0)
blue=(0,147,217)
brown=(60,48,48)

title="Zombies VS Ninja Beta"
#game_folder=os.path.dirname(__file__)
