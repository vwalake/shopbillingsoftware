from tkinter import *
from tkinter import messagebox
import random,os
import tempfile
#import pymysql
from datetime import datetime
import time;



root=Tk()
root.title("bill slip")
root.geometry('1455x720')
bg_color='red'
root.iconbitmap('icon.ico')


if not os.path.exists('bills'):
    os.mkdir('bills')
#======================variable=================
date_one=StringVar()
time_one=StringVar()
c_name=StringVar()
c_phone=StringVar()
c_email=StringVar()
item=StringVar()
Rate=IntVar()
quantity=IntVar()
bill_no=StringVar()
x=random.randint(1000,9999)
bill_no.set(str(x))


global l
l=[]

#=========================Functions================================
#def send_email():
    #if textarea.get(1.0,END)=='\n':
       # messagebox.showerror('Error','Bill is Empty')
    #else:
    #root1.Toplevel()
    #root1.title('send gmail')
    #root1.config(bg='gray20')
    #root1.resizable(0,0)
    #senderframe=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
    #senderframe.grid(row=0,column=0)
    #gmailIdLable=Label(senderframe,text="Sender's Email",font=('arial',14,'bold'))
    #gmailIdLable.grid(row=0,column=0)
    #root1.mainloop()



def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==bill_no.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')


def additm():
    n=Rate.get()
    m=quantity.get()*n
    l.append(m)
    if item.get()!='':
        textarea.insert((10.0+float(len(l)-1)), f"{item.get()}\t\t{quantity.get()}\t\t{ m}\n")
    else:
        messagebox.showerror('Error','Please enter the item')


def gbill():
    if c_name.get() == "" or c_phone.get() == "" or c_email.get()== "" or bill_no.get()== "":
        messagebox.showerror("Error", "Customer detail are must")
    else:
        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, textAreaText)
        textarea.insert(END, f"\n======================================")
        textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(l)}")
        textarea.insert(END, f"\n\n======================================")

        save_bill()


#def reset():
    #textarea.delete(1.0,END)
    #welcome()

def clear():
    #textarea.delete(1.0,END)
    date_one.set(("%d/%m/%y"))
    time_one.set(("%H:%M:%S"))
    c_name.set('')
    c_phone.set('')
    c_email.set('')
    bill_no.set('')
    item.set('')
    Rate.set(0)
    quantity.set(0)
    welcome()
def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        root.destroy()
def save_bill():
    op=messagebox.askyesno("Save bill","Do you want to save the Bill?")
    if op>0:
        bill_details=textarea.get('1.0',END)
        f1=open("bills/"+str(bill_no.get())+".txt","w")
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo("Saved",f"Bill no, :{bill_no.get()} Saved Successfully")
    else:
        return

def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, "\t  Welcome Shriram Paint's")
    textarea.insert(END, f"\nDate:\t\t\t\t{date_one.get()}")
    textarea.insert(END, f"\nTime:\t\t\t\t{time_one.get()}")
    textarea.insert(END, f"\n\nBill Number:\t\t{bill_no.get()}")
    textarea.insert(END, f"\nCustomer Name:\t\t{c_name.get()}")
    textarea.insert(END, f"\nPhone Number:\t\t{c_phone.get()}")
    textarea.insert(END,f"\nCustomer Email\t:\t{c_email.get()}")

    textarea.insert(END, f"\n\n======================================")
    textarea.insert(END, "\nProduct\t\tQTY\t\tPrice")
    textarea.insert(END, f"\n======================================\n")
    textarea.configure(font='arial 15 bold')


title=Label(root,pady=2,text="Billing Software",bd=12,bg=bg_color,fg='white',font=('times new roman', 25 ,'bold'),relief=GROOVE,justify=CENTER)
title.place(x=0,y=0,h=90,w=1455)

#///////datetime//////////////////
date_one=StringVar()
time_one=StringVar()
date_one.set(time.strftime("%d/%m/%y"))
time_one.set(time.strftime("%H:%M:%S"))
lblTitle = Label(title,textvariable=date_one,bd=12,bg=bg_color,fg="white",font=('times new roman',30,'bold'),relief=GROOVE,justify=LEFT)
lblTitle.place(x=0,y=3,h=60)
#lblTitle = Label(root,text="Billing Software",font=('times new roman',30,'bold'),pady=9,bd=5,bg='cadet blue').grid(row=0,column=1))
lblTime = Label(title,textvariable=time_one,bd=12,bg=bg_color,fg="white",font=('times new roman',30,'bold'),relief=GROOVE,justify=RIGHT)
lblTime.place(x=1263,y=3,h=60)



    #=================customer detail Frames=================
F1=LabelFrame(root,bd=10,relief=GROOVE,text='Customer Details',font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
F1.place(x=0,y=90,width=1455)

cname_lbl=Label(F1,text='Customer Name',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,textvariable=c_name,font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=5,pady=5)

cphone_lbl=Label(F1,text='Phone No.',font=('times new romon',18,'bold'),bg=bg_color,fg='white').grid(row=0,column=2,padx=10,pady=5)
cphone_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=5,pady=5)

cemail_lbl=Label(F1,text='Email',font=("times new roman",18,'bold'),bg=bg_color,fg='white').grid(row=0,column=4,padx=10,pady=5)
cemail_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=c_email,relief=SUNKEN,bd=7).grid(row=0,column=5,padx=5,pady=5)


billno_lbl=Label(F1,text='Bill no',font=("times new roman",18,'bold'),bg=bg_color,fg='white').grid(row=0,column=6,padx=10,pady=5)
billno_txt=Entry(F1,width=15,font='arial 15 bold',textvariable=bill_no,relief=SUNKEN,bd=7).grid(row=0,column=7,padx=5,pady=5)

btnsearch=Button(F1,text='SEARCH',bd=10,font='arial 7 bold',command=search_bill,padx=5,pady=10,bg='white',width=15)
btnsearch.grid(row=0,column=8,padx=0,pady=0)

 # =====================Product frame===================
F2 = LabelFrame(root, text='Product Details', font=('times new romon', 18, 'bold'), fg='gold', bg=bg_color)
F2.place(x=20, y=180, width=630, height=500)

itm = Label(F2, text='Product Name', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(row=0,column=0,padx=30,pady=20)
itm_txt = Entry(F2, width=20, textvariable=item, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=0, column=1,padx=10, pady=20)


rate = Label(F2, text='Product Rate', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(row=1, column=0, padx=30, pady=20)
rate_txt = Entry(F2, width=20, textvariable=Rate, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=1, column=1,padx=10, pady=20)

n = Label(F2, text='Quantity', font=('times new romon', 18, 'bold'), bg=bg_color, fg='lightgreen').grid(row=2,column=0, padx=30,pady=20)
n_txt = Entry(F2, width=20, textvariable=quantity, font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=2, column=1,padx=10, pady=20)


#========================Bill area================
F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=655,y=180,width=500,height=470)

bill_title=Label(F3,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()

btnprint=Button(root,text='Print',bd=5,font='arial 15 bold',command=print_bill,bg='Light yellow')
btnprint.place(x=655,y=645,height=35,width=550)

#======================================================
#=====================calci============================
def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnClear():
    global val
    val=""
    data.set("")

def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)

val=""
data=StringVar()
#operator=""
#text_Input = StringVar()

Cal_Frame=Frame(root,bg="white",relief=RIDGE,bd=10)
Cal_Frame.place(x=1155,y=180,width=300,height=500)
#display = Entry(Cal_Frame,textvariable=data,font=('arial',20,'bold'),bd=29,bg="powder blue",justify='right')
#display.place(x=0,y=0)
txt_Result = Entry(Cal_Frame, bg="powder blue",bd=25, textvariable=data, font=("times new roman", 20, "bold"),justify=RIGHT).place(x=0, y=0, relwidth=1, height=85)

# /////////row1/////////////////////
btn_7 = Button(Cal_Frame, text="7",bd=5,bg='white', command=lambda: btnClick(7), font=("times new roman", 15, "bold")).place( x=0, y=85, w=70, h=90)
btn_8 = Button(Cal_Frame, text="8", bd=5,bg='white',command=lambda: btnClick(8), font=("times new roman", 15, "bold")).place(x=70, y=85, w=70, h=90)
btn_9 = Button(Cal_Frame, text="9", bd=5,bg='white', command=lambda: btnClick(9), font=("times new roman", 15, "bold")).place( x=140, y=85, w=70, h=90)
btn_div = Button(Cal_Frame, text="/",bd=5,bg='white', command=lambda: btnClick('/'),  font=("times new roman", 15, "bold")).place(x=210, y=85, w=70, h=90)

# /////////row2/////////////////////
btn_4 = Button(Cal_Frame, text="4", bd=5, bg='white',command=lambda: btnClick(4),font=("times new roman", 15, "bold")).place(x=0, y=170, w=70, h=90)
btn_5 = Button(Cal_Frame, text="5", bd=5, bg='white',command=lambda: btnClick(5),font=("times new roman", 15, "bold")).place(x=70, y=170, w=70, h=90)
btn_6 = Button(Cal_Frame, text="6",  bd=5,bg='white',command=lambda: btnClick(6),font=("times new roman", 15, "bold")).place(x=140, y=170, w=70, h=90)
btn_mul = Button(Cal_Frame, text="*",bd=5, bg='white',command=lambda: btnClick('*'),font=("times new roman", 15, "bold")).place(x=210, y=170, w=70, h=90)

# /////////row3/////////////////////
btn_1 = Button(Cal_Frame, text="1",bd=5,bg='white', command=lambda: btnClick(1), font=("times new roman", 15, "bold")).place( x=0, y=260, w=70, h=90)
btn_2 = Button(Cal_Frame, text="2",bd=5, bg='white',command=lambda: btnClick(2), font=("times new roman", 15, "bold")).place(x=70, y=260, w=70, h=90)
btn_3 = Button(Cal_Frame, text="3",bd=5, bg='white', command=lambda: btnClick(3),font=("times new roman", 15, "bold")).place(x=140, y=260, w=70, h=90)
btn_min = Button(Cal_Frame, text="-",bd=5,bg='white', command=lambda: btnClick('-'),font=("times new roman", 15, "bold")).place(x=210, y=260, w=70, h=90)
# /////////row4/////////////////////
btn_0 = Button(Cal_Frame, text="0",bd=5,bg='white', command=lambda: btnClick(0),font=("times new roman", 15, "bold")).place( x=0, y=350, w=70, h=100)
btn_dot = Button(Cal_Frame, text=".",bd=5,bg='white',command=lambda: btnClick("."),font=("times new roman", 15, "bold")).place(x=70,y=350,w=70,h=100)
btn_sum = Button(Cal_Frame, text="+",bd=5,bg='white', command=lambda: btnClick('+'),font=("times new roman", 15, "bold")).place(x=140, y=350, w=70, h=100)
btn_equal = Button(Cal_Frame, text="=", bd=5,bg='white',command=btnEquals, font=("times new roman", 15, "bold")).place(x=210, y=350, w=70,h=100)

#////////////////row5////////////////////
btn_clear = Button(Cal_Frame, text="Clear",bd=3,bg='white',command=btnClear,font=("times new roman", 15, "bold")).place(x=0,y=450,w=285,h=35)

welcome()
#=========================Buttons======================
btn1=Button(F2,text='Add Item',bd=10,font='arial 15 bold',command=additm,bg='white')
btn1.place(x=40,y=330,height=50,width=230)


btn3=Button(F2,text='Generate Bill',bd=10,font='arial 15 bold',command=gbill,bg='white')
btn3.place(x=310,y=330,height=50,width=230)

btn3=Button(F2,text='Clear',bd=10,font='arial 15 bold',command=clear,bg='white')
btn3.place(x=40,y=400,height=50,width=230)

btn4=Button(F2,text='Exit',bd=10,font='arial 15 bold',command=exit,bg='white')
btn4.place(x=310,y=400, height=50,width=230)





#=================extra===================
#==============all functions stary hear========================
def Calculate():
    print(c_name.get(),
    c_phone .get(),
    c_email.get(),
    item.get(),
    Rate.get(),
    quantity.get(),
    bill_no.get(),
    )

#def check_connection():
 #   try:
  #      con = pymysql.connect(host='localhost', user='root', password='', db='cstmr')
   #     cur = con.cursor()
    #    cur.execute("select * from cstmr_details")
     #   rows = cur.fetchall()
      #  print(rows)
  #  except Exception as ex:
   #     messagebox.showerror("Error", f'Error due to: {str(ex)}')








root.mainloop()