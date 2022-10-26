import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',height=100,width=120) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def zmrzlina(): #funkcia, ktorá vykreslí zmrzlinu
    canvas.create_line(20,40,40,100) #vykreslím čiaru
    canvas.create_line(60,40,40,100) #vykreslím čiaru
    canvas.create_line(20,40,60,40) #vykreslím čiaru
    canvas.create_oval(25,10,55,35,fill='red') #vykreslím kopček zmrliny
    canvas.create_oval(20,20,50,40,fill='yellow') #vykreslím kopček zmrliny
    canvas.create_oval(35,20,60,40,fill='green') #vykreslím kopček zmrliny
    canvas.create_rectangle(20,30,60,40,fill='white') #vykreslím obdĺžnik
    
zmrzlina() #volám funkciu zmrzlina
    
