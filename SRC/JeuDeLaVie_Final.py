#-*- coding:utf-8 -*-

from tkinter import *
import random


Largeur = 660 #Largeur du tableau.
Taille = 660 #Hauteur du tableau.

#La Largeur et la hauteur sont à modifier selon la taille de l'écran utilisé pour afficher la grille.

S=10 #Taille de la cellule
Valeur={} #Valeur au tour n
Valeur_Suivante={} #Valeur au tour n+1
Booleen=False
Speed=1 #Vitesse entre 2 frames en ms


#Création de la grille

for i in range(1,int(Largeur/S+1)):
    for j in range(1,int(Taille/S+1)):
       Valeur[i,j]=0
       Valeur_Suivante[i,j]=0
       
def Vertical():
    c_x=Largeur
    while c_x != 0:
       Canevas.create_line(c_x,0,c_x,Taille,width=1,fill="black")
       c_x=c_x-S

def Horizontal():
    c_y=Taille
    while c_y !=0:
       Canevas.create_line(0,c_y,Largeur,c_y,width=1,fill="black")
       c_y=c_y-S

def Grid():
    Vertical()
    Horizontal()

def Left_Click(event): #Déclaration de l'action attribuée au clic gauche.
    x=event.x-(event.x%S)
    y=event.y-(event.y%S)
    Canevas.create_rectangle(x,y,x+S,y+S,fill="black")
    Valeur[int(x/S),int(y/S)]=1

def Right_Click(event): #Déclaration de l'action attribuée au clic droit.
    x=event.x-(event.x%S)
    y=event.y-(event.y%S)
    Canevas.create_rectangle(x,y,x+S,y+S,fill="white")
    Valeur[int(x/S),int(y/S)]=0

def Start(): #Déclaration de la fonction du début de boucle.
    global Booleen
    if Booleen == False:
      Booleen = True
      compteur()

def Stop(): #Déclaration de la fonction de fin de boucle.
    global Booleen
    Booleen = False

def compteur(): #Déclaration de la fonction qui compte les cellules vivantes autour d'une cellule donnée.a
    for i in range(1,int(Largeur/S+1)):
        for j in range(1,int(Taille/S+1)):
            compteur_vivant=0
            if i==1 and j==1: #Coin Superieur Gauche
                if Valeur[1,2]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[2,2]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[2,1]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[1,1]=compteur_vivant
        	
            elif i==1 and j==int(Taille/S): #Coin Inferieur Gauche
                if Valeur[1,Taille/S-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[2,Taille/S-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[2,Taille/S]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[1,Taille/S]=compteur_vivant
        	
            elif i==int(Largeur/S) and j==1: #Coin Superieur Droit
                if Valeur[Largeur/S-1,1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[Largeur/S-1,2]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[Largeur/S,2]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[Largeur/S,1]=compteur_vivant	
        	
            elif i==int(Largeur/S) and j==int(Taille/S): #Coin Inferieur Droit
                if Valeur[Largeur/S-1,Taille/S]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[Largeur/S-1,Taille/S-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[Largeur/S,Taille/S-1]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[Largeur/S,Taille/S]=compteur_vivant
        	
            elif i==1 and 1<j<int(Taille/S): #Cote Gauche Sans Coins
                if Valeur[1,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[1,j+1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[2,j]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[2,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[2,j+1]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[1,j]=compteur_vivant
        
            elif i==int(Largeur/S) and 1<j<int(Taille/S): #Cote Droit Sans Coins
                if Valeur[i,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i,j+1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i-1,j]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i-1,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i-1,j+1]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[i,j]=compteur_vivant
        	
            elif 1<i<int(Largeur/S) and j==1: #Cote Superieur Sans Coins
                if Valeur[i-1,1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i+1,1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i-1,2]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i,2]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i+1,2]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[i,j]=compteur_vivant
        	
            elif 1<i<int(Largeur/S) and j==int(Taille/S): #Cote Inferieur Sans Coins
                if Valeur[i-1,j]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i+1,j]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i-1,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i+1,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[i,j]=compteur_vivant
        	
            else:
                if Valeur[i+1,j]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i+1,j+1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i+1,j-1]==1:
                    compteur_vivant=compteur_vivant+1	
                if Valeur[i-1,j+1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i-1,j-1]==1:
                    compteur_vivant=compteur_vivant+1	
                if Valeur[i-1,j]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i,j+1]==1:
                    compteur_vivant=compteur_vivant+1
                if Valeur[i,j-1]==1:
                    compteur_vivant=compteur_vivant+1
                Valeur_Suivante[i,j]=compteur_vivant
    Image_Suivante()
    if Booleen==True:
        Root.after(Speed,compteur)

def Image_Suivante():
    Canevas.delete(ALL)
    Grid()
    for i in range(1,int(Largeur/S+1)):
        for j in range(1,int(Taille/S+1)):
            if Valeur_Suivante[i,j]==2:
                if Valeur[i,j]==1:
                    Canevas.create_rectangle((i-1)*S,(j-1)*S,i*S,j*S,fill="black")
                else:
                    Canevas.create_rectangle((i-1)*S,(j-1)*S,i*S,j*S,fill="white")
            elif Valeur_Suivante[i,j]==3:
                Valeur[i,j]=1
                Canevas.create_rectangle((i-1)*S,(j-1)*S,i*S,j*S,fill="black")
            elif Valeur_Suivante[i,j]<2 or Valeur_Suivante[i,j]>3:
                Valeur[i,j]=0
                Canevas.create_rectangle((i-1)*S,(j-1)*S,i*S,j*S,fill="white")

def Random():
    for i in range(1,int(Largeur/S+1)):
        for j in range(1,int(Taille/S+1)):
            Valeur[i,j]=random.randint(0,1)
            if Valeur[i,j]==1:
                Canevas.create_rectangle((i-1)*S,(j-1)*S,i*S,j*S,fill="black")
                
def Delete():
    Canevas.delete(ALL)
    Grid()
        
  		  

Root=Tk()
Root.title("Jeu de La Vie ARE")
Canevas=Canvas(Root,width=Largeur,height=Taille,bg="white")

#Création des boutons

Canevas.bind("<Button-1>",Left_Click)
Canevas.bind("<Button-3>",Right_Click)
Canevas.pack(side=TOP,padx=5,pady=5)
Button1=Button(Root,text="Commencer",command=Start)
Button2=Button(Root,text="Arrêter",command=Stop)
Button3=Button(Root,text="Aléatoire",command=Random)
Button4=Button(Root,text="Effacer",command=Delete)
Button1.pack(side=LEFT,padx=5,pady=5)
Button2.pack(side=LEFT,padx=5,pady=5)
Button3.pack(side=LEFT,padx=5,pady=5)
Button4.pack(side=LEFT,padx=5,pady=5)
Quit=Button(Root,text="Quitter",command=Root.destroy)
Quit.pack(side=LEFT,padx=5,pady=5)
Grid()
Root.mainloop()
