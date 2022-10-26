import tkinter #naimportujem si plátno
import random #naimportujem si knižnicu random
canvas=tkinter.Canvas(bg='white',height=500,width=600) #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

x=100 #nastavím si premennú x na 100
cislo=1 #nastavím si premennú cislo na 1
def ciarovy_kod(): #funkcia, ktorá vykreslí čiarový kód
    global cislo,x #premenné cislo,x si nastavím ako globálne
    for i in range(20): #for cyklus, ktorým vykreslujem čiarový kód
        hrubka=random.randrange(1,15) #premenná hrubka, kde si náhodne vyberám číslo 
        print(f'{cislo}. čiara má hrúbku: {hrubka}') #vypisujem hrúbku čiar do shellu
        canvas.create_line(x,100,x,400,width=hrubka) #vykreslujem čiary čiarového kódu
        x=x+20 #premennú x zväčšujem o 20
        cislo=cislo+1 #premennú cislo zväčšujem o 1
        
ciarovy_kod() #volám funkciu ciarovy_kod
    