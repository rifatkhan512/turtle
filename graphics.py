import turtle as tt
import random
wn=tt.Screen()
wn.bgcolor("#333333")
size=0
tt.speed(0)
for i in range (185):
        
        rn="#"
        for i in range(6):
            x=random.randint(0,2)
            if x:
                x=random.randint(0,9)
                rn+=str(x)
            else:
                x=random.randint(0,5)
                ami="abcdef"
                rn+=ami[x]
        
        colour=rn
        print(rn)
        tt.color(colour)
        tt.forward(size)
        tt.right(71.5)
        size+=3

