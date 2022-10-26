import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',height=300,width=700) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

for i in range(50): #for cyklus na vykreslovanie čiar
    y=random.randint(0,700) #náhodne si vyberám pozíciu čiary
    z=random.randint(0,700) #náhodne si vyberám pozíciu čiary
    hrubka=random.randint(1,10) #náhodne si vyberám hrúbku čiary
    farba=random.choice(('pink','purple','turquoise','blue','green','orange','dark blue','grey','yellow','black','red','lime','brown')) #náhodne si vyberám farbu
    canvas.create_line(y,0,z,300,fill=farba,width=hrubka) #vykresľujem čiaru
