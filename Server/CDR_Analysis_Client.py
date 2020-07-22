from tkinter import *
from tkinter import filedialog
import os
import mysql.connector as mariadb

root = Tk()
root.withdraw()

def search_for_data_file():
    lk=Toplevel()
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilenames(parent=lk, initialdir=currdir, title='Please select file containing data')
    filedata = list(tempdir)
    if len(filedata) > 0:
        print ("You chose: %s" % filedata)
        lk.destroy()
    return filedata

def search_for_format_file():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select file containing data format')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

def Main():
    ff=search_for_format_file()
    file_format = open(ff, "r")
    mariadb_connection = mariadb.connect(user='root', password='root123', database='CDR')
    cursor = mariadb_connection.cursor()
    num_lines = 0
    fstr = ''
    ctbl = ''
    with open(ff, 'r') as abc:
        for line in abc:
            num_lines += 1
    for efg in range(num_lines):
        if efg == num_lines - 1:
            f = file_format.readline()
            fstr = fstr + f + ','
            ctbl = ctbl + f + ' VARCHAR(40) ,'
        else:
            f = file_format.readline()
            f = f[:-1]
            fstr = fstr + f + ','
            ctbl = ctbl + f + ' VARCHAR(40) ,'
    fstr = fstr + "Date_Inserted"
    ctbl = ctbl + "Date_Inserted DATE"
    fd = search_for_data_file()
    '''po=StringVar()
    ok=Toplevel()
    ok.geometry("350x600")
    ok.title("CDR Analysis Server")
    phot=PhotoImage(file=r"/root/Downloads/cdotlogo.gif")
    lkj=Label(ok,image=phot).pack()
    li=Label(ok,text='Tablename').pack()
    e=Entry(ok,textvariable=po).pack()
    bt=Button(ok,text='Submit',command=ok.destroy).pack()
    ok.wait_window()
    lo=po.get()'''
    y="CREATE TABLE IF NOT EXISTS cdr_data (" + ctbl + ");"
    cursor.execute(y)
    for fdvar in fd:
        file_data = open(fdvar, "r")
        j=0
        while 1:
           d = file_data.readline()
           if(j%2==0):
               for i in d:
                   if(i=='\n'):
                       d=d[:-1]
               if d=='':
                   file_data.close()
                   break
               else:
                   s=''
                   for xyz in range(num_lines):
                       x = d.split(';')[xyz]
                       s = s + "'" + x + "'" + ','
                   s = s + "DATE(current_timestamp)"
                   s = "INSERT INTO cdr_data (" + fstr + ") VALUES (" + s + ");"
                   cursor.execute(s)
           j += 1
    mariadb_connection.commit()

if __name__ == "__main__" :
    Main()