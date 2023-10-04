from tkinter import *
from tkinter.ttk import *
import pymysql
from tkinter import messagebox

# ahnaf

db = pymysql.connect(host="localhost", port=3306,
                     user="root", passwd="root", database="proj")
c1 = db.cursor()

toplog = Tk()

unm = StringVar()
pwd = StringVar()
unm1 = StringVar()
pwd1 = StringVar()
cpwd1 = StringVar()
op = StringVar()
np = StringVar()
u_web = StringVar()
u_unm = StringVar()
u_em = StringVar()
u_pass = StringVar()


def logout():
    top_log1.destroy()
    t1.focus_set()


def close1():
    top_viewp.destroy()


def delete_web():
    q = "delete from passwordmanager where id={}".format(sid)
    c1.execute(q)
    db.commit()
    messagebox.showinfo("Success", "Deleted Successfully")
    tv1.delete(0, END)
    tv2.delete(0, END)
    tv3.delete(0, END)
    tv4.delete(0, END)
    top_viewp.destroy()
    view_password()


def edit_web():
    we = u_web.get()
    ue = u_unm.get()
    eme = u_em.get()
    passe = u_pass.get()
    q = "update  passwordmanager set website='{}',user='{}',email='{}',pass2='{}' where id={}".format(
        we, ue, eme, passe, sid)
    c1.execute(q)
    db.commit()
    messagebox.showinfo("Success", "Modified Successfully")
    tv1.delete(0, END)
    tv2.delete(0, END)
    tv3.delete(0, END)
    tv4.delete(0, END)
    lbox.focus_set()


def select_item(event):
    global sid
    i = lbox.curselection()
    b = lbox.get(i)
    q = "select * from passwordmanager where uid={} and website='{}'".format(
        uid, b[0])
    c1.execute(q)
    d = c1.fetchall()
    sid = d[0][0]
    u_web.set(d[0][2])
    u_unm.set(d[0][3])
    u_em.set(d[0][4])
    u_pass.set(d[0][5])


def view_password():
    global top_viewp
    global lbox
    global tv1
    global tv2
    global tv3
    global tv4
    top_viewp = Toplevel()
    top_viewp.geometry("550x400")
    top_viewp.resizable(0, 0)
    q = "select website from passwordmanager where uid={}".format(uid)
    c1.execute(q)
    d = c1.fetchall()
    student_names = d
    sname = StringVar(value=student_names)
    lbox = Listbox(top_viewp, listvariable=sname, height=10)
    lbox.place(x=10, y=10)
    lbox.bind('<<ListboxSelect>>', select_item)
    lv1 = Label(top_viewp, text="Website", font=10)
    lv1.place(x=250, y=10)
    tv1 = Entry(top_viewp, textvariable=u_web, width=20)
    tv1.place(x=250, y=30)
    lv2 = Label(top_viewp, text="Username", font=10)
    lv2.place(x=250, y=70)
    tv2 = Entry(top_viewp, textvariable=u_unm, width=20)
    tv2.place(x=250, y=90)
    lv3 = Label(top_viewp, text="Email", font=10)
    lv3.place(x=250, y=130)
    tv3 = Entry(top_viewp, textvariable=u_em, width=20)
    tv3.place(x=250, y=150)
    lv4 = Label(top_viewp, text="Password", font=10)
    lv4.place(x=250, y=190)
    tv4 = Entry(top_viewp, textvariable=u_pass, width=20)
    tv4.place(x=250, y=210)
    bv1 = Button(top_viewp, text="Edit", command=edit_web)
    bv1.place(x=250, y=240)
    bv2 = Button(top_viewp, text="Delete", command=delete_web)
    bv2.place(x=350, y=240)
    bv3 = Button(top_viewp, text="Close", command=close1)
    bv3.place(x=450, y=240)


def store1():

    w = s_web.get()
    u = s_unm.get()
    e = s_em.get()
    p = s_pass.get()
    q = "insert into passwordmanager(uid,website,user,email,pass2) values({},'{}','{}','{}','{}')".format(
        uid, w, u, e, p)
    c1.execute(q)
    db.commit()
    messagebox.showinfo("Success", "Data is Saved")
    top_store.destroy()
    top_log1.destroy()
    login_entry()


def store_password():
    global top_store
    global s_web
    global s_unm
    global s_em
    global s_pass

    top_store = Toplevel()
    s_web = StringVar()
    s_unm = StringVar()
    s_em = StringVar()
    s_pass = StringVar()

    top_store.geometry("550x400")
    top_store.resizable(0, 0)
    lcp1 = Label(top_store, text="Website", font=10)
    lcp1.place(x=200, y=100)
    tcp1 = Entry(top_store, textvariable=s_web, width=20)
    tcp1.place(x=200, y=120)
    lcp2 = Label(top_store, text="Username", font=10)
    lcp2.place(x=200, y=160)
    tcp2 = Entry(top_store, textvariable=s_unm, width=20)
    tcp2.place(x=200, y=180)
    lcp3 = Label(top_store, text="Email", font=10)
    lcp3.place(x=200, y=220)
    tcp3 = Entry(top_store, textvariable=s_em, width=20)
    tcp3.place(x=200, y=240)
    lcp4 = Label(top_store, text="Password", font=10)
    lcp4.place(x=200, y=280)
    tcp5 = Entry(top_store, textvariable=s_pass, show="*", width=20)
    tcp5.place(x=200, y=300)
    bcp1 = Button(top_store, text="Store", command=store1)
    bcp1.place(x=220, y=330)


def check(p):
    f = 0
    cu = 0
    cd = 0
    cs = 0
    if p == "":
        messagebox.showerror("Error", "No Blank is allowed")
        f = 1
    if len(p) < 8:
        messagebox.showerror("Error", "Maximum 8 characters needed")
        f = 1
    else:
        l = ["!", "@", "#", "%", "^", "&"]
        for i in p:
            if i.isupper():
                cu = cu+1
            if i.isdigit():
                cd = cd+1
            if i in l:
                cs = cs+1
        if cu == 0 or cd == 0 or cs == 0:
            messagebox.showerror(
                "Error", "Atlesat one uppecase and one digit and one special character is needed")
            f = 1
    return f


def check_user(u):
    q = "select * from login where uname='{}'".format(u)
    res = c1.execute(q)
    if res > 0:
        return 1


def create_user():
    u = unm1.get()
    p = pwd1.get()
    cp = cpwd1.get()
    c = check_user(u)
    if c == 1:
        messagebox.showerror("Error", "Sorry, username is already existed")
        tp1.delete(0, END)
        tp2.delete(0, END)
        tp3.delete(0, END)
        tp1.focus_set()
    elif check(p) == 0:
        if p == cp:
            q = "insert into login(uname,pass1) values('{}','{}')".format(u, p)
            c1.execute(q)
            db.commit()
            messagebox.showinfo("Success", "User is created Successfully")
            tp1.delete(0, END)
            tp2.delete(0, END)
            tp3.delete(0, END)
            top_sign.destroy()  # To Close the current window
        else:
            messagebox.showerror("Error", "Password is not matching")
            tp1.delete(0, END)
            tp2.delete(0, END)
            tp3.delete(0, END)
            tp1.focus_set()
    else:
        tp1.delete(0, END)
        tp2.delete(0, END)
        tp3.delete(0, END)
        tp1.focus_set()


def signup():
    global tp1
    global tp2
    global tp3
    global top_sign
    top_sign = Toplevel()
    top_sign.geometry("550x400")
    top_sign.resizable(0, 0)
    label1 = Label(top_sign, text="Create a New User", font=20)
    label1.place(x=200, y=60)
    l1 = Label(top_sign, text="Username", font=10)
    l1.place(x=200, y=100)
    tp1 = Entry(top_sign, textvariable=unm1, width=20)
    tp1.place(x=200, y=120)
    l2 = Label(top_sign, text="Password", font=10)
    l2.place(x=200, y=160)
    tp2 = Entry(top_sign, textvariable=pwd1, show='*', width=20)
    tp2.place(x=200, y=180)
    l3 = Label(top_sign, text="Confirm Password", font=10)
    l3.place(x=200, y=220)
    tp3 = Entry(top_sign, textvariable=cpwd1, show='*', width=20)
    tp3.place(x=200, y=240)
    b1 = Button(top_sign, text="Create", command=create_user)
    b1.place(x=200, y=280)


def deactivate():
    ans = messagebox.askyesno(
        "Deletion", "Are you sure to Deavticate your Account")
    if ans:
        q = "delete from login where uname='{}'".format(u1)
        c1.execute(q)
        db.commit()
        messagebox.showinfo("Success", "Your account is deactivated")
        top_log1.destroy()
        t1.delete(0, END)
        t2.delete(0, END)
    else:
        bt1.focus_set()


def change_password1():
    op1 = op.get()
    np1 = np.get()
    q = "select * from login where uname='{}' and pass1='{}'".format(u1, op1)
    res = c1.execute(q)
    if res > 0:
        if check(np1) == 0:
            q = "update login set pass1='{}' where uname='{}'".format(np1, u1)
            c1.execute(q)
            db.commit()
            messagebox.showinfo("Success", "password is updated successfully")
            top_cp.destroy()
            top_log1.destroy()  # To Close the current window
            t1.delete(0, END)
            t2.delete(0, END)
        else:
            tcp2.delete(0, END)
            tcp2.focus_set()
    else:
        messagebox.showerror("Error", "Password is not matching")
        top_cp.destroy()
        bt1.focus_set()


def change_password():
    global top_cp
    global tcp2
    top_cp = Toplevel()
    top_cp.geometry("550x400")
    top_cp.resizable(0, 0)
    label1 = Label(top_cp, text="Change Password", font=20)
    label1.place(x=200, y=60)
    lcp1 = Label(top_cp, text="Old Password", font=10)
    lcp1.place(x=200, y=100)
    tcp1 = Entry(top_cp, textvariable=op, show='*', width=20)
    tcp1.place(x=200, y=120)
    lcp2 = Label(top_cp, text="New Password", font=10)
    lcp2.place(x=200, y=160)
    tcp2 = Entry(top_cp, textvariable=np, show='*', width=20)
    tcp2.place(x=200, y=180)
    bcp1 = Button(top_cp, text="Change", command=change_password1)
    bcp1.place(x=220, y=230)


def login_entry():
    global top_log1
    top_log1 = Toplevel()
    top_log1.geometry("550x400")
    top_log1.resizable(0, 0)
    lab1 = "Welcome "+u1
    label1 = Label(top_log1, text=lab1, font=20)
    label1.place(x=200, y=100)
    bt01 = Button(top_log1, text="Store Password", command=store_password)
    bt01.place(x=200, y=150)
    bt02 = Button(top_log1, text="View Password", command=view_password)
    bt02.place(x=200, y=200)
    bt1 = Button(top_log1, text="Change Password", command=change_password)
    bt1.place(x=200, y=250)
    bt2 = Button(top_log1, text="Log-Out", command=logout)
    bt2.place(x=200, y=300)


def login():
    global bt1
    global u1
    global p1
    global uid
    u1 = unm.get()
    p1 = pwd.get()
    q = "select * from login where uname='{}' and pass1='{}'".format(u1, p1)
    res = c1.execute(q)
    t1.delete(0, END)
    t2.delete(0, END)
    if res > 0:
        d = c1.fetchall()
        uid = d[0][0]
        login_entry()
    else:
        messagebox.showerror("Error", "Incorrect Username or Password")
        t1.delete(0, END)
        t2.delete(0, END)
        t1.focus_set()


toplog.geometry("550x400")
toplog.resizable(0, 0)
label1 = Label(toplog, text="Login Page", font=20)
label1.place(x=200, y=60)
l1 = Label(toplog, text="Username", font=10)
l1.place(x=200, y=100)
t1 = Entry(toplog, textvariable=unm, width=20)
t1.place(x=200, y=120)
l2 = Label(toplog, text="Password", font=10)
l2.place(x=200, y=160)
t2 = Entry(toplog, textvariable=pwd, show='*', width=20)
t2.place(x=200, y=180)
b1 = Button(toplog, text="Login", command=login)
b1.place(x=220, y=230)
b2 = Button(toplog, text="Sign Up for New User", command=signup)
b2.place(x=200, y=280)
toplog.mainloop()
