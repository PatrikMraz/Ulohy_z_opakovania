import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',height=310,width=500) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

a=481 #nastavím si premennú a na 481
for i in range(29): #for cyklus na vykreslovanie čiar 
    canvas.create_line(a,1,500,310,fill='blue') #vykresľujem čiary
    a=a-17 #premennú a zmenšujem o 17
    