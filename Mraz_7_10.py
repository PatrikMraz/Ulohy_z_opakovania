import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',height=310,width=700) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

x=350 #nastavím si premennú x na 350
a=350 #nastavím si premennú a na 350
for i in range(20): #for cyklus na vykreslovanie čiar
    canvas.create_line(x,10,350,300) #vykreslujem čiary
    x=x-17 #premennú x zmenšujem o 17
for j in range(20): #for cyklus na vykreslovanie čiar
    canvas.create_line(a,10,350,300) #vykreslujem čiary
    a=a+17 #premennú a zväčšujem o 17
    