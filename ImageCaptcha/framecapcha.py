from Tkinter import *
import tkMessageBox
import Tkinter
import random
import ttk

list=[0,0,0,0,0,0]
right1=0
right2=0
right3=0
wrong1=0
wrong2=0
wrong3=0

def msg(event=None):
     val()
     setwrong()
     setval()
     

def helpp(event=None):
      tkMessageBox.showinfo("Info","Select all asked images by click on them and then click on next ")

def randompics():
    mainset()
    Apic=[]
    while len(Apic)!=len(picflag[1]):
        sample=random.choice(picflag[1])
        if sample not in Apic:
            Apic.append(sample)
    global mainApic
    mainApic=Apic[:]
    captcha(Apic)

def val():
    list[0]=Var1.get()
    list[1]=Var2.get()
    list[2]=Var3.get()
    list[3]=Var4.get()
    list[4]=Var5.get()
    list[5]=Var6.get()

    
def setval():
    right1=check[0]
    right2=check[1]
    right3=check[2]
    wrong1=wronglist[0]
    wrong2=wronglist[1]
    wrong3=wronglist[2]
    if (right1==1 and right2==1 and right3==1 and wrong1==0 and wrong2==0 and wrong3==0) :
        tkMessageBox.showinfo("Congratulations","Congratulations")
        root.destroy()
    else:
        tkMessageBox.askretrycancel("Sorry","No image or incorrect image selected")
        mainset()
        randompics()


def setwrong():
    j=0
    k=0
    g=0
    for i in mainApic:
        if i in picflag[2]:
            check[j]=list[g]
            j+=1
        else:
            wronglist[k]=list[g]
            k+=1
        g+=1

def mainset():
     global picflag
     direct=[["  Select all the images of \"IRON MAN\" ",pic,correct],["  Select all the images of \"A FLOWER\" ",pic5,correct5],["  Select all the images of \"A LION\" ",pic4,correct4],["  Select all the images of \"Store Front\" ",pic6,correct6],["  Select all the images of  \"A COUPLE\" ",pic3,correct3],["  Select all the images of a \"BABY KID\" ",pic2,correct2]]
     picflag=random.choice(direct)


def captcha(Apic):

    
    head=Label(root,text=picflag[0],activebackground="blue",height=3,width=28,foreground="midnight blue",font="Times 20 bold italic")
    head.grid(row=0,column=0,columnspan=2,rowspan=2)
    But1=Checkbutton(root,image=Apic[0],variable=Var1,onvalue=1,offvalue=0,height=100,width=200)
    But1.deselect()
    But2=Checkbutton(root,image=Apic[1],variable=Var2,onvalue=1,offvalue=0,height=100,width=200)
    But2.deselect()
    But3=Checkbutton(root,image=Apic[2],variable=Var3,onvalue=1,offvalue=0,height=100,width=200)
    But3.deselect()
    But4=Checkbutton(root,image=Apic[3],variable=Var4,onvalue=1,offvalue=0,height=100,width=200)
    But4.deselect()
    But5=Checkbutton(root,image=Apic[4],variable=Var5,onvalue=1,offvalue=0,height=100,width=200)
    But5.deselect()
    But6=Checkbutton(root,image=Apic[5],variable=Var6,onvalue=1,offvalue=0,height=100,width=200)
    But6.deselect()

    But1.grid(row=2,column=0)
    But2.grid(row=2,column=1)
    But3.grid(row=3,column=0)
    But4.grid(row=3,column=1)
    But5.grid(row=4,column=0)
    But6.grid(row=4,column=1)


root=Tk()
root.title("Image Captcha")

Var1=IntVar()
Var2=IntVar()
Var3=IntVar()
Var4=IntVar()
Var5=IntVar()
Var6=IntVar()

#root.geometry("400x400+300+300")

#root.resizable(width=False, height=False)

A0=PhotoImage(file="pics/iron.gif")
A1=PhotoImage(file="pics/iron2.gif")
A2=PhotoImage(file="pics/iron3.gif")
A3=PhotoImage(file="pics/sam1.gif")
A4=PhotoImage(file="pics/samp5.gif")
A5=PhotoImage(file="pics/samp4.gif")

B0=PhotoImage(file="pics/kid1.gif")
B1=PhotoImage(file="pics/kid2.gif")
B2=PhotoImage(file="pics/kid3.gif")
B3=PhotoImage(file="pics/sa1.gif")
B4=PhotoImage(file="pics/sa2.gif")
B5=PhotoImage(file="pics/sa3.gif")

C0=PhotoImage(file="pics/cup1.gif")
C1=PhotoImage(file="pics/cup2.gif")
C2=PhotoImage(file="pics/cup3.gif")
C3=PhotoImage(file="pics/alo1.gif")
C4=PhotoImage(file="pics/alo2.gif")
C5=PhotoImage(file="pics/alo3.gif")


E0=PhotoImage(file="pics/flower1.GIF")
E1=PhotoImage(file="pics/flower2.gif")
E2=PhotoImage(file="pics/flower3.gif")
E3=PhotoImage(file="pics/palnt1.gif")
E4=PhotoImage(file="pics/plant2.gif")
E5=PhotoImage(file="pics/plant3.gif")

F0=PhotoImage(file="pics/store1.gif")
F1=PhotoImage(file="pics/store2.gif")
F2=PhotoImage(file="pics/store3.gif")
F3=PhotoImage(file="pics/home1.gif")
F4=PhotoImage(file="pics/home2.gif")
F5=PhotoImage(file="pics/home3.gif")

D0=PhotoImage(file="pics/lion.gif")
D1=PhotoImage(file="pics/lion2.gif")
D2=PhotoImage(file="pics/lion3.gif")
D3=PhotoImage(file="pics/cat.gif")
D4=PhotoImage(file="pics/cat2.gif")
D5=PhotoImage(file="pics/dog.gif")

pic2=[B0,B1,B2,B3,B4,B5]
pic=[A0,A1,A2,A3,A4,A5]
pic3=[C0,C1,C2,C3,C4,C5]
pic4=[D0,D1,D2,D3,D4,D5]
pic5=[E0,E1,E2,E3,E4,E5]
pic6=[F0,F1,F2,F3,F4,F5]
correct3=[C0,C1,C2]
correct2=[B0,B1,B2]
correct=[A0,A1,A2]
correct4=[D0,D1,D2]
correct5=[E0,E1,E2]
correct6=[F0,F1,F2]
direct=[["  Select all the images of \"IRON MAN\" ",pic,correct],["  Select all the images of \"A FLOWER\" ",pic5,correct5],["  Select all the images of \"A LION\" ",pic4,correct4],["  Select all the images of \"Store Front\" ",pic6,correct6],["  Select all the images of  \"A COUPLE\" ",pic3,correct3],["  Select all the images of  \"BABY KID\" ",pic2,correct2]]
picflag=random.choice(direct)

check=[1,2,3]
wronglist=[1,2,3]
mainApic=[]
while len(mainApic)!=len(picflag[1]):
    sample=random.choice(picflag[1])
    if sample not in mainApic:
        mainApic.append(sample)


captcha(mainApic)
theBut=Button(root,text="Next",relief="raised",activebackground="blue",height=2,width=10,command=msg)
theBut.grid(row=5,column=1,rowspan=2 ,columnspan=2)
refresh=Button(root,text="Refresh",relief="raised",activebackground="blue",cursor="exchange",height=2,width=10,command=randompics)
refresh.grid(row=5,column=0,rowspan=2)#,columnspan=3)
hel=Button(root,text="Info",bitmap="info",relief="raised",activebackground="blue",cursor="circle",height=10,width=20,command=helpp)
hel.grid(row=5,column=3,rowspan=2)

root.mainloop()
