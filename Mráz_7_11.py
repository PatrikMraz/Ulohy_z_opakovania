import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',height=300,width=800) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

x=0 #nastavím si premennú x na 0
for i in range(20): #for cyklus na vykreslenie kružníc
    farba=random.choice(('pink','red','yellow','brown','green','orange','purple','blue','black','turquoise')) #náhodne si vyberám farbu
    r=random.randrange(50,100) #náhodne si vyberám polomer kružnice
    canvas.create_oval(110-r//2+x,110-r//2,110+r//2+x,110+r//2,outline=farba,width=3) #vykresľujem kružnice
    x=random.randrange(50,600) #náhodne si vyberám medzeru medzi kružnicami