import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',height=130,width=120) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

def strom(): #funkcia,ktorá vykreslí strom
    canvas.create_rectangle(35,55,60,120,fill='black') #vykreslím kmeň v podobe obdĺžnika
    canvas.create_oval(20,10,75,65,fill='green') #vykreslím korunu stromu v podobe kruhu
    canvas.create_line(45,45,55,35,width=2) #vykreslím čiaru
    canvas.create_line(55,35,65,45,width=2) #vykreslím čiaru
    canvas.create_oval(40,45,50,55,fill='red') #vykreslím čerešňu v podobe kruhu
    canvas.create_oval(60,45,70,55,fill='red') #vykreslím čerešňu v podobe kruhu
strom() #zavolám funkciu strom