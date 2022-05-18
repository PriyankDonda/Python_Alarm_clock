from tkinter import *
from tkinter.ttk import *
from time import strftime
from playsound import playsound
import threading

root = Tk()
root.title(" Alarm Clock ")
root.geometry('750x500')
root.configure(bg='black')

#------------current time----------------
label1 = Label(root,text=" Current Time ",anchor='center')
label1.config(font=("Raleway",18),background = "black", foreground = "white")
label1.pack(side=TOP,pady=(30,10),anchor='center')

def time():
    # Get current time
    current_time = strftime("%I:%M:%S %p")
    # Changing current time
    label_time.config(text=current_time)
    label_time.after(1000, time)
        
    
label_time = Label(root,font=("ds-digital",40), background = "black", foreground = "cyan")
label_time.pack(anchor='center')

# Thread for showeing current time
thread1 = threading.Thread(target=time)
thread1.start()

#----------------------------------------

#------------set Alarm---------------
label2 = Label(root,text=" Set Alarm ",anchor='center')
label2.config(font=("Raleway",18),background = "black", foreground = "white")
label2.pack(side=TOP,pady=(30,20),anchor='center')
  
def alarm():
    # Get alarm time
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()} {am_pm.get()}"
    string = " Alarm Set : " + set_alarm_time
    label3.config(text=string)
    
    # Thread for playing alarm
    thread2 = threading.Thread(target=alarm_play)
    thread2.start()

def alarm_play():
    # Get alarm time
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()} {am_pm.get()}"
    
    # Infintite Loop
    while True:
        # Get current time
        current_time = strftime("%I:%M:%S %p")
       
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            string = " It's Time to Wake up!... "
            label3.config(text=string)
            # Playing sound
            playsound('./alarm_sound.mp3')
            break
        
    string = " Set Alarm again, No Alarm Set!... "
    label3.config(text=string)
    
# Frame for set alarm time
frame = Frame(root)
#frame.configure(bg="black",fg="cyan")
frame.pack()

#Set Hours  
hour = StringVar(root)
hours = ('Hour', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12'
        )
hour.set(hours[0])
  
hrs = OptionMenu(frame, hour, *hours)
#hrs.config(bg="black",fg="cyan")
#hrs["menu"].config(bg="black",fg="cyan")
hrs.pack(side=LEFT,padx=10)

#Set Minute  
minute = StringVar(root)
minutes = ('Minute', '00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
minute.set(minutes[0])
  
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT,padx=10)

#Set Second 
second = StringVar(root)
seconds = ('Second', '00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59')
second.set(seconds[0])
  
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT,padx=10)

#Set Am/Pm
am_pm = StringVar(root)
ap = ('Mode', 'AM', 'PM')
am_pm.set(ap[0])
  
ap_mode = OptionMenu(frame, am_pm, *ap)
ap_mode.pack(side=LEFT,padx=10)

#Button for set alarm
btn=Button(root,text="Set Alarm",command=(lambda: alarm()))
btn.pack(pady=20)

#alarm status
label3 = Label(root,text=" No Alarm Set yet!... ",anchor='center')
label3.config(font=("Raleway",20),background = "black", foreground = "cyan")
label3.pack(side=TOP,pady=20,anchor='center')

mainloop()
