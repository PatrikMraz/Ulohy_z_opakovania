import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',height=130,width=200) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def balon(): #funkcia balon, ktorá vykreslí balón
    canvas.create_oval(80,10,130,60,fill='blue') #vykreslím balón v podobe kruhu 
    canvas.create_line(80,40,105,100) #vykreslím čiaru
    canvas.create_line(130,40,105,100) #vykreslím čiaru
    canvas.create_rectangle(90,100,120,115,fill='red') #vykreslím kôš v podobe obdĺžnika
balon() #volám funkciu balon