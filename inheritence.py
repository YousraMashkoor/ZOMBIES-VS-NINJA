class parent:
    def __init__(self):
        self.y=40
        self.x=50
    def update(self):
        print(self.y)

class child(parent):
    def __init__(self):
        parent.__init__(self)
   # def update(self):
    #    print(self.x)
c=child()
c.update()
