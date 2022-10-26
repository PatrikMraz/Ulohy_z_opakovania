import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',height=321,width=501) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

y=2 #nastavím si premennú y na 2
for i in range(17): #for cyklus na vykreslovanie čiar
    canvas.create_line(0,y,510,y)  #vykresľujem čiaru
    y=y+20 #premennú y zväčšujem o 20

x=2 #nastavím si premennú x na 2
for j in range(26): #for cyklus na vykreslovanie čiar
    canvas.create_line(x,0,x,350) #vykresľujem čiaru
    x=x+20 #premennú x zväčšujem o 20