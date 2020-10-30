#Inteliigent traffic system
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import sys
import tkinter
root = tkinter.Tk()

root.title("Intelligent Traffic Control System")
 

HEIGHT = 1080
WIDTH =1920

#think of the canvas as a fitter that widen the window, thats it, HOWEVER all frams still stick on root, even bg image
canvas = Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

image = Image.open('hell.jpg')

background_image = ImageTk.PhotoImage(image)
background_label = Label(root,image=background_image)
background_label.place(relheight=1,relwidth=1)



def showMsg( answer):
    # tkWindow = Tk()
    # tkWindow.geometry('1010x420')
    # tkWindow.title('PythonExamples.org - Tkinter Example')
    import sys
    stdoutOrigin=sys.stdout
    sys.stdout = open("log.txt", "w")
    frame_3 = Frame(root,bg='#66B2FF')
    frame_3.place(relx=0.35,rely=0.15,relwidth=0.655,relheight=0.55,anchor='n')
    f=open("log.txt",'r')
    data= "The current traffic level is " +str(answer)+' %'
    f.close()
    Results = Label(frame_3, text = data,background = "#66B2FF" ,relief=RAISED,font=("Helvetica", 15),anchor=CENTER,foreground="black",padx = 10 , pady = 10)
    Results.grid(row = 1, column = 1)
#
# def showInput():
#     # frame_4 = Frame(root,bg='#B8204E')
#     # frame_4.place(relx=0.8,rely=0.15,relwidth=0.23,relheight=0.10,anchor='n')
#     # name_label1=Label(frame_4,text="Cars Incoming  ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',15))
#     # name_label1.place(relx =0,relwidth=0.7,relheight=1)
#     name_label1=Label(frame_4,text=carsIncoming,fg='#0D0D11',bg='#FB2865',font=('Footlight MT Light',25))
#     name_label1.place(relx =.5,relwidth=0.7,relheight=1)
#
#
#     # frame_5 = Frame(root,bg='#B8204E')
#     # frame_5.place(relx=0.8,rely=0.40,relwidth=0.23,relheight=0.10,anchor='n')
#     # name_label2=Label(frame_5,text="Cars Waiting   ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',15))
#     # name_label2.place(relx =0,relwidth=0.7,relheight=1)
#     name_label2=Label(frame_5,text=carsWaiting,fg='#0D0D11',bg='#FB2865',font=('Footlight MT Light',25))
#     name_label2.place(relx =.5,relwidth=0.7,relheight=1)

def fuzz():
    cw = int(v1.get())
    ci = int(v2.get())
    # a=eval(input("Enter the number of cars waiting :"))
    a = cw
    b = ci

    rule_simulation.input['carsWaiting']=a
    # b=eval(input("Enter the number of incoming cars :"))
    rule_simulation.input['carsIncoming']=b

    rule_simulation.compute()
    # print("Traffic  %f "%rule_simulation.output['Traffic'],"%")
    answer = rule_simulation.output['Traffic']
    Traffic.view(sim=rule_simulation)
    showMsg(answer)




frame_1 = Frame(root,bg='#B8204E',bd=5)
frame_1.place(relx=0.5,rely=0.0,relwidth=0.6,relheight=0.1,anchor='n')


frame_4 = Frame(root,bg='#B8204E')
frame_4.place(relx=0.8,rely=0.15,relwidth=0.23,relheight=0.10,anchor='n')
name_label1=Label(frame_4,text="Cars Incoming  ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',15))
name_label1.place(relx =0,relwidth=0.7,relheight=1)
v1 = StringVar()
e = Entry(frame_4, textvariable=v1,bg='#B8204E',fg='#0D0D11',font=('Footlight MT Light',25),justify=CENTER)
e.place(relx=0.85,rely=0,relwidth=.3,relheight=1,anchor='n')


frame_5 = Frame(root,bg='#B8204E')
frame_5.place(relx=0.8,rely=0.40,relwidth=0.23,relheight=0.10,anchor='n')
name_label2=Label(frame_5,text="Cars Waiting   ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',15))
name_label2.place(relx =0,relwidth=0.7,relheight=1)
v2 = StringVar()
e = Entry(frame_5, textvariable=v2,bg='#B8204E',fg='#0D0D11',font=('Footlight MT Light',25),justify=CENTER)
e.place(relx=0.85,rely=0,relwidth=.3,relheight=1,anchor='n')


name_label=Label(frame_1,text="Intelligent Traffic Control System   ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',25))
name_label.place(relx =0,relwidth=0.7,relheight=1)



# button_go = Button(frame_1,text="Fuzzy Logic",command=lambda:[showMsg(),showInput()],font=('Forte',25),bg='#79FBAB')
# button_go.place(relwidth=.20,relx=.80,relheight=1)
#
# clearx = Button(root,text="CLEAR",command=lambda:[showMsg()],font=('Footlight MT Light',25),bg='red')
# clearx.place(relwidth=.15,relx=.83,rely=.05,relheight=0.05)


default = Button(root,text="Default",command=lambda:[fuzz()],font=('Footlight MT Light',25),bg='red')
default.place(relwidth=.15,relx=.83,rely=.30,relheight=0.05)


# frame_2 = Frame(root,bg='#B8204E')
# frame_2.place(relx=0.5,rely=0.15,relwidth=0.30,relheight=0.40,anchor='n')





# name_label1=Label(frame_2,text="Output in log.txt file",background = "pink")
# name_label1.place(relx =0,relwidth=1,relheight=1)
#
# image = Image.open('scale.jpg')
#
# background_imag = ImageTk.PhotoImage(image)
# background_label = Label(name_label1,image=background_imag)
# background_label.place(relheight=1,relwidth=1)
import numpy as np;
import skfuzzy as sk;
from skfuzzy import control as ctrl;
carsWaiting=ctrl.Antecedent(np.arange(1,200,1),'carsWaiting')
carsIncoming =ctrl.Antecedent(np.arange(1,200,1),'carsIncoming')
Traffic=ctrl.Consequent(np.arange(1,101,1),'Traffic')
carsWaiting['low']=sk.trimf(carsWaiting.universe,[1,5,10])
carsWaiting['medium']=sk.trimf(carsWaiting.universe,[8,15,20])
carsWaiting['high']=sk.trimf(carsWaiting.universe,[18,50,200])

carsIncoming['low']=sk.trimf(carsIncoming.universe,[1,5,10])
carsIncoming['medium']=sk.trimf(carsIncoming.universe,[8,15,20])
carsIncoming['high']=sk.trimf(carsIncoming.universe,[18,50,200])

Traffic['low']=sk.trimf(Traffic.universe,[1,20,40])
Traffic['medium']=sk.trimf(Traffic.universe,[30,60,80])
Traffic['high']=sk.trimf(Traffic.universe,[70,80,100])

carsWaiting.view()
carsIncoming.view()
Traffic.view()

Rule1=ctrl.Rule(carsWaiting['low']|carsIncoming['low'],Traffic['low'])
Rule2=ctrl.Rule(carsWaiting['low']|carsIncoming['high'],Traffic['high'])
Rule3=ctrl.Rule(carsWaiting['low']|carsIncoming['medium'],Traffic['medium'])
Rule4=ctrl.Rule(carsWaiting['high']|carsIncoming['low'],Traffic['high'])
Rule5=ctrl.Rule(carsWaiting['high']|carsIncoming['high'],Traffic['high'])
Rule6=ctrl.Rule(carsWaiting['medium']|carsIncoming['low'],Traffic['low'])
Rule7=ctrl.Rule(carsWaiting['medium']|carsIncoming['medium'],Traffic['medium'])
Rule8=ctrl.Rule(carsWaiting['medium']|carsIncoming['high'],Traffic['high'])
Rule9=ctrl.Rule(carsWaiting['high']|carsIncoming['medium'],Traffic['high'])

rule_control_system=ctrl.ControlSystem([Rule1,Rule2,Rule3,Rule4,Rule5,Rule6,Rule7,Rule8,Rule9])
rule_simulation=ctrl.ControlSystemSimulation(rule_control_system)



root.mainloop()
