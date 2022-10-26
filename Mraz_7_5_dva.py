import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',width='250') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno
canvas.create_rectangle(0,300,250,225,fill='green') #vykreslím obdĺžnik
canvas.create_rectangle(10,250,100,100,fill='red') #vykreslím obdĺžnik
canvas.create_oval(15,160,50,120,fill='blue') #vykreslím elipsu
canvas.create_oval(60,160,95,120,fill='blue') #vykreslím elipsu
canvas.create_line(10,100,55,60,width=3) #vykreslím elipsu
canvas.create_line(100,100,55,60,width=3) #vykreslím čiaru
canvas.create_line(30,120,30,160,width=3) #vykreslím čiaru
canvas.create_line(75,120,75,160,width=3) #vykreslím čiaru
canvas.create_line(15,140,50,140,width=3) #vykreslím čiaru
canvas.create_line(60,140,95,140,width=3) #vykreslím čiaru
canvas.create_rectangle(35,250,70,180,fill='gray') #vykreslím obdĺžnik
canvas.create_oval(40,220,45,210,fill='black') #vykreslím elipsu
canvas.create_oval(160,15,240,90,outline='',fill='yellow') #vykreslím elipsu
