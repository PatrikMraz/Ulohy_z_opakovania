import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

a=30 #nastavím si premennú a na 30
b=55 #nastavím si premennú b na 55
for i in range(8): #for cyklus na vykreslenie balónov
    farba=random.choice(('dark green','green','purple','light blue','dark orange','turquoise','lime','light green')) #náhodne si vyberám farbu
    canvas.create_oval(a,25,a+60,80,fill=farba) #vykresľujem elipsu
    canvas.create_line(b,80,160,200) #vykresľujem čiaru
    a=a+30 #premennú a zväčšujem o 30
    b=b+30 #premennú b zväčšujem o 30
