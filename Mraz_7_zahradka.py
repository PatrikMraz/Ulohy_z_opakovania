import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',width=550,height=330) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno
 
def muchotravka(x,y): #funkcia, ktorá mi vykreslí muchotrávku
    canvas.create_oval(x,y+130,x+28,y+150,outline='',fill='brown') #vykresľujem elipsu
    canvas.create_oval(x-31,y+10,x+59,y+80,outline='',fill='red') #vykresľujem elipsu
    canvas.create_rectangle(x-31,y+60,x+60,y+80,outline='',fill='white') #vykresľujem obdĺžnik
    canvas.create_rectangle(x,y+60,x+29,y+140,outline='',fill='brown') #vykresľujem obdĺžnik
    canvas.create_oval(x+10,y+25,x,y+35,outline='',fill='white') #vykresľujem elipsu
    canvas.create_oval(x-20,y+40,x-10,y+50,outline='',fill='white') #vykresľujem elipsu
    canvas.create_oval(x+10,y+40,x+20,y+50,outline='',fill='white') #vykresľujem elipsu
    canvas.create_oval(x+40,y+25,x+50,y+35,outline='',fill='white') #vykresľujem elipsu
muchotravka(51,130) #volám funkciu muchotravka s danými parametrami

j=5 #nastavím si premennú j na 5
l=235 #nastavím si premennú l na 235
def trava(): #funkcia, ktorou vykresľujem trávu
    global j,l #premenné j,l nastavím ako globálne
    canvas.create_rectangle(0,305,550,500,outline='',fill='green') #vykresľujem obdĺžnik
    for i in range(55): #for cyklus, ktorým vykresľujem trávu
        canvas.create_line(j,l+50,j,l+115,width=3,fill='green') #vykresľujem obdĺžnik
        j=j+10 #premennú j zväčšujem o 10
trava() #volám funkciu trava
    
p=370 #nastavím si premennú p na 370
o=130 #nastavím si premennú o na 130
c=520 #nastavím si premennú c na 520
m=280 #nastavím si premennú m na 280
def jazierko(): #funkcia, ktorou vykresľujem jazierko
    global p,o,c,m #premenné p,o,c,m nastavím ako globálne
    for j in range(20): #for cyklus, ktorým vykresľujem jazierko
        canvas.create_oval(p,o,c,m,outline='blue') #vykresľujem elipsu
        p=p+5 #premennú p zväčšujem o 5
        o=o+5 #premennú o zväčšujem o 5
        c=c-5 #premennú c zväčšujem o 5
        m=m-5 #premennú m zväčšujem o 5
jazierko() #volám funkciu jazierko

def slnko(): #funkcia, ktorou vykresľujem slnko
    for i in range(40): #for cyklus, ktorým vykresľujem slnko
        x=random.randint(10,100) #vyberám náhodnú dĺžku lúčov
        y=random.randint(20,90) #vyberám náhodnú dĺžku lúčov
        canvas.create_line(0,0,x,y,width=3,fill='yellow') #vykresľujem čiaru
slnko() #volám funkciu slnko

x=320 #nastavím si premennú x na 320
z=320 #nastavím si premennú z na 320
w=320 #nastavím si premennú w na 320
def pozemky(): #funkcia, ktorou vykresľujem pozemky
    global x,z,w #premenné x,z,w nastavím ako globálne
    for i in range(5): #for cyklus, ktorým vykresľujem pozemky
        y=random.randint(0,30) #náhodne si vyberám dĺžku strany
        canvas.create_rectangle(x,10,x+30-y,40-y) #vykresľujem pozemky v podobe štvorcov
        x=x+40 #premennú x zväčšujem o 40
    for i in range(5): #for cyklus, ktorým vykresľujem pozemky
        y=random.randint(0,30) #náhodne si vyberám dĺžku strany
        canvas.create_rectangle(z,50,z+30-y,80-y)  #vykresľujem pozemky v podobe štvorcov
        z=z+40 #premennú a zväčšujem o 40
    for i in range(5): #for cyklus, ktorým vykresľujem pozemky
        y=random.randint(0,30) #náhodne si vyberám dĺžku strany
        canvas.create_rectangle(w,90,w+30-y,120-y)  #vykresľujem pozemky v podobe štvorcov
        w=w+40 #premennú w zväčšujem o 40        
pozemky() #volám funkciu pozemky

