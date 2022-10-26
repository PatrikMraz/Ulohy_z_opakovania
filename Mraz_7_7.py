import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',height=500,width=300) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

for i in range(50): #for cyklus na vykreslovanie čiar
    y=random.randint(0,500) #náhodne si vyberám pozíciu čiary
    z=random.randint(0,500) #náhodne si vyberám pozíciu čiary
    hrubka=random.randint(1,10) #náhodne si vyberám hrúbku čiary
    farba=random.choice(('pink','purple','turquoise','blue','green','orange','dark blue','grey','yellow','black','red','lime','brown')) #náhodne si vyberám farbu
    canvas.create_line(0,y,300,z,fill=farba,width=hrubka) #vykresľujem čiaru
