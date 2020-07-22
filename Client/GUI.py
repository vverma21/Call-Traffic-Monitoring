import subprocess
import os
import tkinter
from tkinter import *
top = Tk()

def Query(i, j, k, l, p):
    ip=i.get()
    user=j.get()
    password=k.get()
    database=l.get()
    command_schema = "mysql" + " -h " + ip + " -u" + user + " -p" + password + " " + database + " -e \"desc cdr_data;\""
    uj=subprocess.check_output(command_schema+"| awk 'NR>1{print $1}'",shell=True)
    uj=str(uj)
    uj=uj[2:-3]
    col_names = uj.split("\\n")
    if col_names==['']:
        uj=Toplevel()
        uj.geometry("1600x900")
        ko=Label(uj,text="CDR Analysis Client",font="42").grid(row=0,column=0)
        phk=PhotoImage(image=r"/root/Downloads/cdotlogo.gif")
        bn=Label(uj,image=phk).grid(row=0,column=1)
        io=Label(uj,text="Invalid Credentials",font="42").grid(row=1,column=0)
        bo=Button(uj,text='OK',font="42",command=uj.destroy).grid(row=2,column=0)
        uj.wait_window()
        top.destroy()
    else:
     op = Toplevel()
     op.geometry("1600x900")
     mb = Menubutton(op, text="Select the option",font="42", relief=RAISED)
     mb.grid()
     mb.menu = Menu(mb, tearoff=0)
     mb["menu"] = mb.menu
     n = {}
     n["*"]=IntVar()
     n["Default "]=IntVar()
     for t in col_names:
        n[t] = IntVar()
     ty = []
     mb.menu.add_checkbutton(label="*(for all)",font="40",variable=n["*"])
     mb.menu.add_checkbutton(label="default", font="40", variable=n["Default "])
     for r in col_names:
        mb.menu.add_checkbutton(label=r, variable=n[r])
     mb.grid(row=1, column=0)
     v=StringVar()
     kuy=Label(op,text="Is there a condition?",font="42").grid(row=2,column=0)
     r=Radiobutton(op,text="yes",font='42',variable=v,value="yes").grid(row=3,column=0)
     r1 = Radiobutton(op, text="no",font='42', variable=v, value="no").grid(row=3, column=1)
     bt=Button(op,text="Submit",font='42',command=op.destroy)
     bt.grid(row=4,column=1)
     op.wait_window()

     if n["*"].get():
        ty.append("*")
     if n["Default "].get():
         ty.append("NGCPE_id,Sequence_Number,write_time_stamp,caller_no,called_no")
     else:
      for r in col_names:
        if n[r].get():
            ty.append(r)

     cloumn = ''
     for strvar in ty:
        cloumn = cloumn + strvar + ','
     cloumn = cloumn[:-1]
     condition= v.get()
     tyu=0
     if condition == 'yes':
        tyu=1
        rt=Toplevel()
        mbt = Menubutton(rt, text="Select the variable",font="42", relief=RAISED)
        mbt.grid()
        mbt.menu = Menu(mbt, tearoff=0)
        mbt["menu"] = mbt.menu
        nt = {}
        for t in col_names:
            nt[t] = IntVar()
        tyt = []

        for r in col_names:
            mbt.menu.add_checkbutton(label=r, variable=nt[r])

        mbt.grid(row=1, column=0)

        v1=StringVar()
        ki=Label(rt,text="Variable value(multiple values to be seperated by ,)",font='42').grid(row=2,column=0)
        ei=Entry(rt,textvariable=v1).grid(row=2,column=1)
        bh=Button(rt,text="Submit",font='42',command=rt.destroy).grid(row=3,column=1)
        rt.wait_window()
        for r in col_names:
            if nt[r].get():
                tyt.append(r)
        va = ""
        va = v1.get()
        variable_value = va.split(',')
        fstr = ''
        for (s1,s2) in zip(tyt,variable_value):
            fstr = fstr + s1 + '=' + s2 + ','
        fstr = fstr[:-1]
        command = "mysql" + " -h " + ip + " -u" + user +" -p" + password + " " + database + " -e \"select " + " " + cloumn + " from cdr_data where "+ fstr +"\G;\">/home/cdot/ffile.txt"
     else :
        command = "mysql"+" -h "+ ip +" -u"+user+" -p"+password+" "+database+" -e \"select "+" "+cloumn+" from cdr_data\G;\">/home/cdot/ffile.txt"
     print(command)
     os.system(command)
     ft=open("/home/cdot/ffile.txt",'r').read()
     lk=Toplevel()
     lk.geometry("1600x900")
     T=Text(lk,height=400,width=350)
     scr = Scrollbar(lk)

     scr.pack(side=RIGHT, fill=Y)
     scr.config(command=T.yview)
     T.pack()
     T.insert(END,ft)
     bj=Button(lk,text="OK",font='42',command=lk.destroy).pack()
     scr = Scrollbar(lk)
     T.configure(yscrollcommand=scr.set)
     scr.pack(side=RIGHT, fill=Y)
     lk.wait_window()
     top.destroy()

def thuy():
    i = StringVar()
    j = StringVar()
    k = StringVar()
    l = StringVar()
    p = StringVar()
    top.title("CDR Analysis Client")
    top.geometry("1600x900")
    op=PhotoImage(file=r"/root/Downloads/CDOT_Logo.gif")
    opl=PhotoImage(file=r"/root/Downloads/CDRAC.gif")
    L=Label(image=op).grid(row=0,column=0)
    jk=Label(image=opl).grid(row=0,column=1)
    #lp=Label(top,text="CDR Analysis Client",font="120",foreground="steelblue").grid(row=0,column=1)
    L1 = Label(top, text="IP Address:",font="42",bg="steelblue",foreground="white")
    L1.grid(row=1, column=0)
    E1 = Entry(top, textvariable=i,font="42")
    E1.grid(row=1, column=1)
    L2 = Label(top, text="Username:",font="42",bg="steelblue",foreground="white")
    L2.grid(row=2, column=0)
    E2 = Entry(top, textvariable=j,font="42")
    E2.grid(row=2, column=1)
    L3 = Label(top, text="Password",font="42",bg="steelblue",foreground="white")
    L3.grid(row=3, column=0)
    E3 = Entry(top, textvariable=k,font="42")
    E3.grid(row=3, column=1)
    L4 = Label(top, text="Database:",font="42",bg="steelblue",foreground="white")
    L4.grid(row=4, column=0)
    E4 = Entry(top, textvariable=l,font="42")
    E4.grid(row=4, column=1)
    b = Button(top, text='Submit',font="42",bg="steelblue",foreground="white", command=lambda: Query(i, j, k, l, p))
    b.grid(row=6, column=1)
    top.mainloop()

if __name__ == "__main__":
    thuy()


