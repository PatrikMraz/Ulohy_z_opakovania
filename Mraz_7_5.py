import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(bg='white',width='600') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno
canvas.create_rectangle(10,250,120,120,fill='lime') #vykreslím obdĺžnik
canvas.create_rectangle(45,250,85,210,fill='black') #vykreslím obdĺžnik
canvas.create_rectangle(30,130,50,150,fill='blue') #vykreslím obdĺžnik
canvas.create_rectangle(30,170,50,190,fill='blue') #vykreslím obdĺžnik
canvas.create_rectangle(80,130,100,150,fill='blue') #vykreslím obdĺžnik
canvas.create_rectangle(80,170,100,190,fill='blue') #vykreslím obdĺžnik
canvas.create_line(65,50,120,120,fill='brown') #vykreslím čiaru
canvas.create_line(65,50,10,120,fill='brown') #vykreslím čiaru
canvas.create_rectangle(120,250,280,190,fill='dark orange') #vykreslím obdĺžnik
canvas.create_rectangle(160,220,180,200,fill='blue') #vykreslím obdĺžnik
canvas.create_rectangle(220,220,200,200,fill='blue') #vykreslím obdĺžnik
canvas.create_rectangle(260,250,240,220,fill='black') #vykreslím obdĺžnik
canvas.create_oval(360,150,310,200,fill='dark green') #vykreslím elipsu
canvas.create_oval(430,150,380,200,fill='dark green') #vykreslím elipsu
canvas.create_rectangle(340,250,330,200,fill='brown') #vykreslím obdĺžnik
canvas.create_rectangle(410,250,400,200,fill='brown') #vykreslím obdĺžnik
