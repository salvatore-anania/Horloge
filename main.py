
import time
from tkinter import * 
from tkinter.messagebox import *

instance="run"
def afficher_heure(heure):
    global instance
    global current_time
    global save
    
    heures=heure[0]
    minutes=heure[1]
    secondes=heure[2]
    current_time=(heures,minutes,secondes)
    
    if mode=="":
        affiche_heure.config(text=str("{:02d}".format(current_time[0]))+":"+str("{:02d}".format(current_time[1]))+":"+str("{:02d}".format(current_time[2])))
    else:
        if heures==0:
            affiche_heure.config(text=str(12)+":"+str("{:02d}".format(current_time[1]))+":"+str("{:02d}".format(current_time[2]))+"AM")
        elif heures<12:
            affiche_heure.config(text=str(current_time[0])+":"+str("{:02d}".format(current_time[1]))+":"+str("{:02d}".format(current_time[2]))+"AM")
        elif heures==12:
             affiche_heure.config(text=str(12)+":"+str("{:02d}".format(current_time[1]))+":"+str("{:02d}".format(current_time[2]))+"PM")
        else:
            affiche_heure.config(text=str(current_time[0]%12)+":"+str("{:02d}".format(current_time[1]))+":"+str("{:02d}".format(current_time[2]))+"PM")
    
    fenetre.update()
    
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
    
    my_alarm(alarm)
    calcul_chrono()
    
    #test si une pause a eu lieu pour arrêter la première recurrence de lhorloge et en lancer une nouvelle
    if instance=="run":
        fenetre.after(1000,lambda: afficher_heure(current_time))
    elif instance!="pause":
        instance="run"
    else:
        save=current_time

def instantiation():
    global instance
    
    
    try:
        int(set_heure.get())
        int(set_minute.get())
        int(set_seconde.get())
    except:
        erreur.pack(side=TOP)
    else:
        if instance=="pause":
            instance="pause"
        else:
            instance="new"
        temp=(int(set_heure.get()),int(set_minute.get()),int(set_seconde.get()))
        erreur.pack_forget()
        afficher_heure(temp)
    
def pause():
    global instance
    global save
    
    if instance=="run":
        save=current_time
        instance="pause"
    elif instance!="kill":
        instance="run"
        afficher_heure(save)
        
    
def time_mode():
    global mode
    if mode=="":
        mode="AM"
    else:
        mode=""

def my_alarm(heure_alarm):
    global alarm
    
    alarm=heure_alarm
    if "current_time" in globals():
        if alarm==current_time:
            affiche_alarme.pack(side = TOP,padx=5, pady=5)
        else:
            affiche_alarme.pack_forget()
            
 
def set_alarm(heure_alarm):
    set_label_alarm.config(text="Alarme régler pour "+str(heure_alarm[0])+"h"+str(heure_alarm[1])+"m"+str(heure_alarm[2])+"s"+"\nRégler une alarme :")
    my_alarm(heure_alarm)
    
def test_alarm():
    try:
            int(set_H_alarm.get())
            int(set_M_alarm.get())
            int(set_S_alarm.get())
    except:
        erreur.pack(side=TOP)
    else:
        temp=(int(set_H_alarm.get()),int(set_M_alarm.get()),int(set_S_alarm.get()))
        erreur.pack_forget()
        set_alarm(temp)


def calcul_chrono():
    global chrono_run
    global chrono_time
    
    if chrono_run=="run":
        if chrono_time[2]<59:
            chrono_time[2]+=1
        else:
            chrono_time[2]=0
            chrono_time[1]+=1
            if chrono_time[1]>59:
                chrono_time[1]=0
                chrono_time[0]+=1
                if chrono_time[0]>23:
                    chrono_time[0]=0
        affiche_chrono.config(text=chrono_time)

def set_chrono():
    global chrono_run
    global chrono_time
    
    if chrono_run=="kill":
        chrono_run="run"
        affiche_chrono.pack(side = TOP,padx=5)
    else:
        chrono_run="kill"
        for i in range(len(chrono_time)):
            chrono_time[i]=0
        affiche_chrono.pack_forget()
        affiche_chrono.config(text=chrono_time)

def pause_chronometre():
    global chrono_run
    
    if chrono_run=="run":
        chrono_run="pause"
    elif chrono_run!="kill":
        chrono_run="run"
    


fenetre = Tk()
fenetre.title("Horloge")
fenetre.configure(bg='grey')
fenetre.geometry("800x800")

Frame_horloge= Frame(fenetre,bg='grey',width=400)

erreur=Label(Frame_horloge,bg="grey",fg='red', text="Entrez un nombre compris entre 0 et 24 heures et 0 et 60 secondes/minutes",font=("Arial", 15))

#initialise les variables nécessaire au fonctionnement des fonctions
global mode
chrono_time=[0,0,0]
mode= ""
chrono_run="kill"


#partie liée à affichage de l'heure
affiche_heure=Label(Frame_horloge, text="current_time", bg="grey",font=("Arial", 60))
affiche_heure.pack(side = TOP,padx=5)

#partie liée à l'affichage du réglage de l'heure
frame_input_time= Frame(Frame_horloge,bg='grey',width=400)
set_label_heure=Label(frame_input_time,bg='grey', text="Changer l'heure :",font=("Arial", 20))
set_label_heure.pack(side=TOP,padx=5 ,pady=5)
set_heure=Entry(frame_input_time, text="",width=4,font=("Arial", 15))
set_heure.pack(side=LEFT,padx=5)
set_heure_label=Label(frame_input_time, text="H",font=("Arial", 20))
set_heure_label.pack(side=LEFT,padx=5)
set_minute=Entry(frame_input_time, text="",width=4,font=("Arial", 15))
set_minute.pack(side=LEFT,padx=5)
set_minute_label=Label(frame_input_time, text="M",font=("Arial", 20))
set_minute_label.pack(side=LEFT,padx=5)
set_seconde=Entry(frame_input_time, text="",width=4,font=("Arial", 15))
set_seconde.pack(side=LEFT,padx=5)
set_seconde_label=Label(frame_input_time, text="S",font=("Arial", 20))
set_seconde_label.pack(side=LEFT,padx=5)

frame_input_time.pack()

lancer_heure=Button(Frame_horloge, text="Regler l'heure",font=("Arial", 15), command= instantiation)
lancer_heure.pack(pady=5)

#partie liée à l'affichage de l'alarme
frame_input_alarm= Frame(Frame_horloge,bg='grey',width=400)
frame_test=Frame(frame_input_alarm,bg='grey',width=400)
set_label_alarm=Label(frame_input_alarm,bg='grey', text="Régler une alarme :",font=("Arial", 20))
set_label_alarm.pack(side=TOP,padx=5 ,pady=5)
set_H_alarm=Entry(frame_test, text="",width=4,font=("Arial", 15))
set_H_alarm.pack(side=LEFT,padx=5)
set_heure_label_alarm=Label(frame_test, text="H",font=("Arial", 20))
set_heure_label_alarm.pack(side=LEFT,padx=5)
set_M_alarm=Entry(frame_test, text="",width=4,font=("Arial", 15))
set_M_alarm.pack(side=LEFT,padx=5)
set_minute_label_alarm=Label(frame_test, text="M",font=("Arial", 20))
set_minute_label_alarm.pack(side=LEFT,padx=5)
set_S_alarm=Entry(frame_test, text="",width=4,font=("Arial", 15))
set_S_alarm.pack(side=LEFT,padx=5)
set_seconde_label_alarm=Label(frame_test, text="S",font=("Arial", 20))
set_seconde_label_alarm.pack(side=LEFT,padx=5)
frame_test.pack()
frame_input_alarm.pack()

lancer_alarm=Button(Frame_horloge, text="Regler l'alarme",font=("Arial", 15), command= test_alarm)
lancer_alarm.pack(side = TOP,padx=5, pady=5)
affiche_alarme=Label(Frame_horloge, text="Alarme activé",bg="red", pady=5,font=("Arial", 100))
affiche_alarme_set=Label(Frame_horloge, text="Alarme enregistré",bg="red", pady=5,font=("Arial", 50))
Pause=Button(Frame_horloge, text="Pause/reprise",font=("Arial", 15), command= pause)
Pause.pack(side = TOP,padx=5, pady=5)
Frame_horloge.pack()

#partie liée à l'affichage du changement de mode
mode_button=Button(Frame_horloge, text="Mode d'affichage",font=("Arial", 15), command= time_mode)
mode_button.pack(side = TOP,padx=5, pady=5)

#partie liée à l'affichage du chronometre
mode_button=Button(Frame_horloge, text="Chronometre",font=("Arial", 15), command= set_chrono)
mode_button.pack(side = TOP,padx=5, pady=5)
affiche_chrono=Label(Frame_horloge, text=chrono_time, bg="grey",font=("Arial", 60))
pause_chrono=Button(Frame_horloge, text="Pause/reprise chronometre",font=("Arial", 15), command= pause_chronometre)
pause_chrono.pack(side = TOP,padx=5, pady=5)

#lancement de l'horloge
my_alarm((30,0,0))
current_systeme = time.strftime("%H,%M,%S")
heure_systeme = tuple(map(int, current_systeme.split(',')))
afficher_heure(heure_systeme)

fenetre.mainloop()
