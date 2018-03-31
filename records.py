import pygame
from initials import *

class record:
    def __init__(self):
        self.names=[]
        self.scores=[]
        
    def add(self,name,score):
        flag=False
        for i in range(len(self.names)):
            if name==self.names[i]:
                flag=True
                if score>self.scores[i]:
                    self.scores[i]=score
        if not flag:
            self.names.append(name)
            self.scores.append(score)
        
    def show(self):
        screen=pygame.display.set_mode((width,height))
        
        for i in range(len(self.names)):
            print(self.names[i],"\t\t",self.scores[i])
        
        screen.fill(blue)
        pygame.display.flip()



