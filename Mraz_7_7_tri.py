import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',height=500,width=500) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

for i in range(100): #for cyklus na vykreslovanie čiar
    x=random.randint(1,500) #náhodne si vyberám pozíciu čiary
    y=random.randint(1,500) #náhodne si vyberám pozíciu čiary
    hrubka=random.randint(1,10) #náhodne si vyberám hrúbku čiary
    farba=random.choice(('pink','purple','turquoise','blue','green','orange','dark blue','grey','yellow','black','red','lime','brown')) #náhodne si vyberám farbu
    canvas.create_line(x,y,250,250,fill=farba,width=hrubka) #vykresľujem čiaru