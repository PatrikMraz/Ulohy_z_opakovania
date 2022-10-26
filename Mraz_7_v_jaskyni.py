import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',height=400,width=700) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

canvas.create_rectangle(0,0,700,30,fill='green',outline='') #vykreslím obdĺžnik
canvas.create_rectangle(0,370,700,400,fill='green',outline='') #vykreslím obdĺžnik

x=0 #premennú x si nastavím na 0
for i in range(700): #for cyklus na vykreslenie kvaplov
    y=random.randint(20,70) #náhodne si vyberám dĺžku kvaplov
    canvas.create_line(x,30,x,y,fill='green') #vykresľujem čiaru
    canvas.create_line(x,400-y,x,400,fill='green')  #vykresľujem čiaru
    x=x+1 #premennú x si zväčšujem o 1

a=5 #premennú a si nastavím na 5
def mlakyarebrik(): #funkcia mlakyarebrik, ktorá mi vykresľuje mláky a rebrík
    global a #premennú a si nastavím ako globálnu
    pocet=random.randint(1,20) #náhodne si vyberám počet mlák
    for i in range(pocet): #for cyklus na vykreslovanie mlák
        r=random.randint(20,100) #náhodne si vyberám polomer kružnice 
        y=random.randint(130,280) #náhodne si vyberám y-novú súradnicu
        x=random.randint(0,700) #náhodne si vyberám x-ovú súradnicu
        canvas.create_oval(x-r//2,y-r//2,x+r//2,y+r//2,fill='blue') #vykresľujem kružnicu
    canvas.create_line(5,250,805,250,fill='brown',width=2) #vykresľujem čiaru
    canvas.create_line(5,325,805,325,fill='brown',width=2) #vykresľujem čiaru
    for j in range(10): #for cyklus na vykreslenie rebríka
        canvas.create_line(a,250,a,325,fill='brown',width=2) #vykresľujem čiaru
        a=a+80 #premennú a zväčšujem o 80
        
mlakyarebrik() #volám funkciu mlakyarebrik