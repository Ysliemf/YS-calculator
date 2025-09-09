































from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("YF calclature")
root.geometry("650x700")
root.resizable(height=0,width=0)



back_image=Image.open("clc.jpg")
back_image=back_image.resize((650, 700))
bg_image=ImageTk.PhotoImage(back_image)
canvas=Canvas(root,width="600",height="800")
canvas.pack(fill="both",expand=True)
canvas.create_image(0,0, image=bg_image, anchor="nw")


main_lble=Label(root,text="",fg="#4e4957",bg="#ada7b5",font=("Amiri",26),width=23,height=1,anchor=W)
canvas.create_window(326,130,window=main_lble)


properties=[]



def btn1():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"1")
        properties.append("1")



def btn2():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"2")
        properties.append("2")


def btn3():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"3")
        properties.append("3")


def btn4():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"4")
        properties.append("4")


def btn5():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"5")
        properties.append("5")

def btn6():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"6")
        properties.append("6")

def btn7():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"7")
        properties.append("7")

def btn8():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"8")
        properties.append("8")

def btn9():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"9")
        properties.append("9")

def btn0():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"0")
        properties.append("0")

def btn00():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"00")
        properties.append("00")






def btnsw():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num) + "=")
        main_lble.config(text=int(eval("".join(properties))))
        properties.clear()







def btntrh():
              
        old_num=main_lble["text"]  
        main_lble.config(text=str(old_num)+"-")
        properties.append("-")   

def btnksm():
              
        old_num=main_lble["text"]  

        main_lble.config(text=str(old_num)+"÷")
        properties.append("/")

def btndrb():
              
        old_num=main_lble["text"]  

        main_lble.config(text=str(old_num)+"X")
        properties.append("*")  
def btnaw():
              
        old_num=main_lble["text"]  

        main_lble.config(text=str(old_num)+"%")
        properties.append("/100")
def btntrb():
         
        old_num=main_lble["text"]  

        main_lble.config(text="√"+str(old_num))
        properties.append("**0.5")


def btntkb():
    old_num = main_lble["text"]
      
    main_lble.config(text="∛" + str( old_num))
    properties.append("**(1/3)")
    






def btnrb():
              
        old_num=main_lble["text"]  
        main_lble.config(text="("+old_num+" )²")
        properties.append("*"+str(old_num))
        

def btnmkb():
              
        old_num=main_lble["text"]  
        main_lble.config(text="("+ old_num+" )³")
        properties.append("*"+str(old_num)+"*"+str(old_num))


def btnarb():
              
        old_num=main_lble["text"]  
        main_lble.config(text="("+old_num+" )⁴")
        properties.append("*"+str(old_num)+"*"+str(old_num)+"*"+ str(old_num))
        



def btngm():
              
        old_num=main_lble["text"]  
        main_lble.config(text=old_num+"+")
        properties.append("+")
        
def btncl():
              
        main_lble.config(text="")  
        


def btnex():

        root.destroy()    


def btn99():
              
        old_num=main_lble["text"]  
        main_lble.config(text=old_num+".")



bt1=Button(root,text="1",command=btn1 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt1.place(x=149,y=516,height="61",width="77")
bt2=Button(root,text="2",command=btn2 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt2.place(x=239,y=516,height="61",width="77")
bt3=Button(root,text="3",command=btn3 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt3.place(x=329,y=516,height="61",width="77")
bt4=Button(root,text="4",command=btn4 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt4.place(x=149,y=446,height="61",width="77")
bt5=Button(root,text="5",command=btn5 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt5.place(x=240,y=446,height="61",width="77")
bt6=Button(root,text="6",command=btn6 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt6.place(x=330,y=446,height="61",width="77")
bt7=Button(root,text="7",command=btn7 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt7.place(x=149,y=376,height="61",width="77")
bt8=Button(root,text="8",command=btn8 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt8.place(x=240,y=376,height="61",width="77")
bt9=Button(root,text="9",command=btn9 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt9.place(x=330,y=375,height="61",width="77")
bt0=Button(root,text="0",command=btn0 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt0.place(x=149,y=585,height="61",width="77")
bt00=Button(root,text="00",command=btn00 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt00.place(x=239,y=585,height="61",width="77")
bt99=Button(root,text=".",command=btn99 ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bt99.place(x=329,y=585,height="61",width="77")
btsw=Button(root,text="=",command=btnsw ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
btsw.place(x=520,y=585,height="61",width="77")
bttrh=Button(root,text="-",command=btntrh ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bttrh.place(x=520,y=516,height="61",width="77")
btksm=Button(root,text="÷",command=btnksm ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
btksm.place(x=520,y=446,height="61",width="77")
btdrb=Button(root,text="X",command=btndrb ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
btdrb.place(x=429,y=446,height="61",width="77")
btmaw=Button(root,text="%",command=btnaw ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
btmaw.place(x=429,y=375,height="61",width="77")
bttrb=Button(root,text="√",command=btntrb ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))

bttrb.place(x=520,y=375,height="61",width="77")
bttkb=Button(root,text="∛",command=btntkb ,bg="#363c47",fg="#dfe6f2",font=("Amiri",35))
bttkb.place(x=520,y=310,height="61",width="77")

btrb=Button(root,text="( )²",command=btnrb ,bg="#363c47",fg="#dfe6f2",font=("Amiri",22))
btrb.place(x=429,y=310,height="61",width="77")
btmkb=Button(root,text="( )³",command=btnmkb ,bg="#363c47",fg="#dfe6f2",font=("Amiri",22))
btmkb.place(x=520,y=245,height="61",width="77")
btarb=Button(root,text="( )⁴",command=btnarb ,bg="#363c47",fg="#dfe6f2",font=("Amiri",22))
btarb.place(x=429,y=245,height="61",width="77")

btgm=Button(root,text="+",command=btngm ,bg="#363c47",fg="#dfe6f2",font=("Amiri",44))
btgm.place(x=429,y=516,height="133",width="77")

btcl=Button(root,text="مسح\clear",command=btncl ,bg="#413A37",fg="#dfe6f2",font=("Amiri",13))
btcl.place(x=48,y=516,height="135",width="83")

btex=Button(root,text="EXIT\خروج",command=btnex ,bg="#413A37",fg="#dfe6f2",font=("Amiri",13))
btex.place(x=51,y=370,height="135",width="81")

lb1=Label(root,text="created by Youssef Sliem",fg="#5b32a8",bg="#dfe6f2",font=("Calibri",16),height=2,width=32)
canvas.create_window(230,343, window=lb1)


root.mainloop()
