import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',width='350') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

canvas.create_line(10,50,110,250) #vykreslím čiaru
canvas.create_line(50,50,150,250) #vykreslím čiaru

a=10 #nastavím si premennú a na 10
b=60 #nastavím si premennú b na 60
c=60 #nastavím si premennú c na 60
for i in range(18): #for cyklus na vykreslenie čiar
    canvas.create_line(a,b,c,b) #vykresľujem čiary
    a=a+5 #premennú a zväčšujem o 5
    b=b+10 #premennú b zväčšujem o 10
    c=c+5 #premennú c zväčšujem o 5
    
canvas.create_line(260,50,160,250) #vykreslím čiaru
canvas.create_line(300,50,200,250) #vykreslím čiaru

x=250 #nastavím si premennú x na 250
y=60 #nastavím si premennú y na 60
z=300 #nastavím si premennú z na 300
for j in range(18): #for cyklus na vykreslenie čiar
    canvas.create_line(x,y,z,y) #vykresľujem čiary
    x=x-5 #premennú x zmenšujem o 5
    y=y+10 #premennú y zväčšujem o 10
    z=z-5 #premennú z zmenšujem o 5




