class MagicButton():
    def __init__(self,some_function):
        self.press = some_function

def jump():
    print("jump")

def hop():
    print("hop")

#a = MagicButton(jump)
#b = MagicButton(hop)


#for x in [a.press,b.press]:
#    x()

def fireworks(*args, **kwargs):
    for x in args: 
        print(x)

    for k,y in kwargs.items(): 
        print(k,y)

a = MagicButton(fireworks)
a.press(20, explosions=3)
a.press(12,52,duds=255, fatal_accidents=4)
        
    
