
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
    chrono()
    if instance==1:
        fenetre.after(1000,lambda: afficher_heure(current_time))
    elif instance!=3:
        instance=1

def instantiation():
    global instance
    instance+=1
    temp=(int(set_heure.get()),int(set_minute.get()),int(set_seconde.get()))
    afficher_heure(temp)
    
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
            
def chrono():
    global chrono_run
    global chrono_time
    if chrono_run==True:
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
    if chrono_run==False:
        chrono_run=True
        affiche_chrono.pack(side = TOP,padx=5, pady=5)
    else:
        chrono_run=False
        for i in range(len(chrono_time)):
            chrono_time[i]=0
        affiche_chrono.pack_forget()
        affiche_chrono.config(text=chrono_time)
        
    


fenetre = Tk()
fenetre.title("Horloge")
fenetre.configure(bg='grey')
fenetre.geometry("800x600")

Frame_horloge= Frame(fenetre,bg='grey',width=400)

global mode
chrono_time=[0,59,54]
mode= ""
chrono_run=False
affiche_heure=Label(Frame_horloge, text="current_time", bg="grey",font=("Arial", 100))
affiche_heure.pack(side = TOP,padx=5, pady=5)


frame_input_time= Frame(Frame_horloge,bg='grey',width=400)
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

frame_input_time.pack(pady=5)

lancer_heure=Button(Frame_horloge, text="Regler heure",font=("Arial", 15), command= instantiation)
lancer_heure.pack()

frame_input_alarm= Frame(Frame_horloge,bg='grey',width=400)
set_H_alarm=Entry(frame_input_alarm, text="",width=4,font=("Arial", 15))
set_H_alarm.pack(side=LEFT,padx=5)
set_heure_label_alarm=Label(frame_input_alarm, text="H",font=("Arial", 20))
set_heure_label_alarm.pack(side=LEFT,padx=5)
set_M_alarm=Entry(frame_input_alarm, text="",width=4,font=("Arial", 15))
set_M_alarm.pack(side=LEFT,padx=5)
set_minute_label_alarm=Label(frame_input_alarm, text="M",font=("Arial", 20))
set_minute_label_alarm.pack(side=LEFT,padx=5)
set_S_alarm=Entry(frame_input_alarm, text="",width=4,font=("Arial", 15))
set_S_alarm.pack(side=LEFT,padx=5)
set_seconde_label_alarm=Label(frame_input_alarm, text="S",font=("Arial", 20))
set_seconde_label_alarm.pack(side=LEFT,padx=5)
frame_input_alarm.pack(pady=5)

lancer_alarm=Button(Frame_horloge, text="Regler alarme",font=("Arial", 15), command=lambda: my_alarm((int(set_H_alarm.get()),int(set_M_alarm.get()),int(set_S_alarm.get()))))
lancer_alarm.pack(side = TOP,padx=5, pady=5)
affiche_alarme=Label(Frame_horloge, text="Alarme activé",bg="red")
lancer_alarm=Button(Frame_horloge, text="Pause/reprise",font=("Arial", 15), command= pause)
lancer_alarm.pack(side = TOP,padx=5, pady=5)
Frame_horloge.pack()

mode_button=Button(Frame_horloge, text="Mode d'affichage",font=("Arial", 15), command= time_mode)
mode_button.pack(side = TOP,padx=5, pady=5)

mode_button=Button(Frame_horloge, text="Chronometre",font=("Arial", 15), command= set_chrono)
mode_button.pack(side = TOP,padx=5, pady=5)
affiche_chrono=Label(Frame_horloge, text=chrono_time, bg="grey",font=("Arial", 80))

my_alarm((30,0,0))
current = time.strftime("%H,%M,%S")
res = tuple(map(int, current.split(',')))
afficher_heure(res)

fenetre.mainloop()
