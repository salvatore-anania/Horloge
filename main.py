
import time
from tkinter import * 
from tkinter.messagebox import *

instance=1
def afficher_heure(heure):
    global instance
    global current_time
    heures=heure[0]
    minutes=heure[1]
    secondes=heure[2]
    if secondes<59:
        secondes+=1
    else:
        secondes=0
        minutes+=1
        if minutes>59:
            minutes=0
            heures+=1
            if heures>23:
                heures=0
    current_time=(heures,minutes,secondes)
    if mode=="":
        affiche_heure.config(text=str(current_time[0])+":"+str(current_time[1])+":"+str(current_time[2]))
    else:
        if heures==0:
            affiche_heure.config(text=str(12)+":"+str(current_time[1])+":"+str(current_time[2])+"AM")
        elif heures<12:
            affiche_heure.config(text=str(current_time[0])+":"+str(current_time[1])+":"+str(current_time[2])+"AM")
        elif heures==12:
             affiche_heure.config(text=str(12)+":"+str(current_time[1])+":"+str(current_time[2])+"PM")
        else:
            affiche_heure.config(text=str(current_time[0]%12)+":"+str(current_time[1])+":"+str(current_time[2])+"PM")
    fenetre.update()
    my_alarm(alarm)
    if instance==1:
        fenetre.after(1000,lambda: afficher_heure(current_time))
    elif instance!=3:
        instance=1

def instantiation():
    global instance
    instance+=1
    temp=list(map(int, regler_heure.get().split(',')))
    if temp[2]!=0:
        temp[2]-=1
        envoi=tuple(temp)
    else:
        envoi=temp
    afficher_heure(envoi)
    
def pause():
    global instance
    global save
    if instance==1:
        save=current_time
        instance=3
    else:
        instance=1
        afficher_heure(save)

def reprise():
    global instance
    global save
    instance=1
    afficher_heure(save)
    
def time_mode():
    global mode
    if mode=="":
        mode="AM"
    else:
        mode=""

def my_alarm(heure_alarm):
    global alarm
    global de_set
    alarm=heure_alarm
    if "current_time" in globals():
        if alarm==current_time:
            affiche_alarme.pack(side = TOP,padx=5, pady=5)
        else:
            affiche_alarme.pack_forget()

        
        
    


fenetre = Tk()
fenetre.title("Horloge")
fenetre.configure(bg='grey')

Frame_horloge= Frame(fenetre,bg='grey')

global mode
mode= ""

Frame_user = Frame(Frame_horloge, borderwidth=2, relief=GROOVE)
Frame_user.pack( padx=30, pady=30)
affiche_heure=Label(Frame_horloge, text="current_time")
affiche_heure.pack(side = TOP,padx=5, pady=5)

regler_heure=Entry(Frame_horloge, textvariable="Entrez heure")
regler_heure.pack(side = TOP,padx=5, pady=5)
lancer_heure=Button(Frame_horloge, text="Regler heure", command= instantiation)
lancer_heure.pack(side = TOP,padx=5, pady=5)

regler_alarm=Entry(Frame_horloge, text="current_time")
regler_alarm.pack(side = TOP,padx=5, pady=5)
lancer_alarm=Button(Frame_horloge, text="Regler alarme", command=lambda: my_alarm(tuple(map(int, regler_alarm.get().split(',')))))
lancer_alarm.pack(side = TOP,padx=5, pady=5)
affiche_alarme=Label(Frame_horloge, text="Alarme activé")
lancer_alarm=Button(Frame_horloge, text="Pause/reprise", command= pause)
lancer_alarm.pack(side = TOP,padx=5, pady=5)
Frame_horloge.pack()

mode_button=Button(Frame_horloge, text="Mode d'affichage", command= time_mode)
mode_button.pack(side = TOP,padx=5, pady=5)

my_alarm((30,0,0))
current = time.strftime("%H,%M,%S")
res = tuple(map(int, current.split(',')))
test=list(res)
afficher_heure(test)
fenetre.mainloop()
