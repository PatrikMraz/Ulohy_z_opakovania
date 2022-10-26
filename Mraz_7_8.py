import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',height=500,width=700) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def ostrovavlajka(x,y): #funkcia, ktorá vykreslí ostrovavlajku a ľoďku
    a=random.randrange(50,100) #náhodne si vyberiem pozíciu mesiaca
    canvas.create_rectangle(x+90,y-200,x+200,y-120,width=5,fill='lime') #vykreslím obdĺžnik
    canvas.create_oval(x+120,y-185,x+170,y-135,outline='',fill='yellow') #vykreslím elipsu
    canvas.create_oval(x+135,y-185,x+170,y-135,outline='',fill='lime') #vykreslím elipsu
    canvas.create_line(x+90,y-200,x+90,y-30,width=5) #vykreslím čiaru
    canvas.create_oval(x+20,y-30,x+160,y+50,outline='',fill='brown') #vykreslím elipsu
    canvas.create_line(x+280,y-160,x+280,y-50,width=5) #vykreslím čiaru
    canvas.create_line(x+280,y-160,x+320,y-90,width=5) #vykreslím čiaru
    canvas.create_line(x+320,y-92,x+280,y-70,width=5) #vykreslím čiaru
    canvas.create_line(x+190,y-50,x+380,y-50,width=5) #vykreslím čiaru
    canvas.create_rectangle(x,y,x+710,y+250,outline='',fill='blue') #vykreslím obdĺžnik
    canvas.create_line(x+210,y+10,x+360,y+10,width=5) #vykreslím čiaru
    canvas.create_line(x+192,y-50,x+210,y+10,width=5) #vykreslím čiaru
    canvas.create_line(x+377,y-50,x+360,y+10,width=5) #vykreslím čiaru
    canvas.create_oval(x+550,y-a*2,x+650,y-a,outline='',fill='yellow') #vykreslím elipsu
    canvas.create_oval(x+580,y-a*2,x+650,y-a,outline='',fill='white') #vykreslím elipsu
    canvas.create_oval(x+550,y+a*2,x+650,y+a,outline='',fill='yellow') #vykreslím elipsu
    canvas.create_oval(x+580,y+a*2,x+650,y+a,outline='',fill='blue') #vykreslím elipsu
ostrovavlajka(0,250) #volám funkciu ostrovavlajka s danými parametrami
