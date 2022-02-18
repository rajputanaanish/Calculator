import tkinter as tk

def fun1():
    a1=int(E1.get())
    a2=int(E2.get())
    a3=a1+a2
    L4.set(a3)
def fun2():
    a1=int(E1.get())
    a2=int(E2.get())
    a3=a1-a2
    L4.set(a3)
def fun3():
    a1=int(E1.get())
    a2=int(E2.get())
    a3=a1*a2
    L4.set(a3)
def fun4():
    a1=int(E1.get())
    a2=int(E2.get())
    a3=a1//a2
    L4.set(a3)
def fun5():
    a1=int(E1.get())
    a2=int(E2.get())
    a3=a1%a2
    L4.set(a3)
def fun6():
    a1=int(E1.get())
    a2=a1**3
    L4.set(a2)
def fun7():
    a1=int(E1.get())
    m=1
    for x in range(1,a1+1,1):
        m=m*x
    a2=m
    L4.set(a2)


    






window=tk.Tk()
window.title("ANISH KUMAR")
window.geometry("500x500")
window.resizable(True,False)
window.configure(bg="#abcdef")
L4=tk.StringVar()

L1=tk.Label(window,text="enter 1st number",bg="#ee0ef0",fg="#acddfe")
L1.place(relx=0.05,rely=0.08,relwidth=0.3,relheight=0.10)

E1=tk.Entry(window,text="",bd="9",bg="#00edfc")
E1.place(relx=0.05,rely=0.19,relwidth=0.5,relheight=0.10)

L2=tk.Label(window,text="Enter 2nd number",bg="#ee0ef0",fg="#ffffff")
L2.place(relx=0.05,rely=0.32,relwidth=0.3,relheight=0.10)

E2=tk.Entry(window,text="",bd="9",bg="#00edfc")
E2.place(relx=0.05,rely=0.45,relwidth=0.5,relheight=0.10)

B1=tk.Button(window,text="+",bd="6",bg="#ffff10",command=fun1)
B1.place(relx=0.05,rely=0.58,relwidth=0.1,relheight=0.10)

B2=tk.Button(window,text="-",bd="6",bg="#ffff10",command=fun2)
B2.place(relx=0.18,rely=0.58,relwidth=0.1,relheight=0.10)

B3=tk.Button(window,text="*",bd="6",bg="#ffff10",command=fun3)
B3.place(relx=0.31,rely=0.58,relwidth=0.1,relheight=0.10)

B4=tk.Button(window,text="/",bd="6",bg="#ffff10",command=fun4)
B4.place(relx=0.45,rely=0.58,relwidth=0.1,relheight=0.10)

B5=tk.Button(window,text="%",bd="6",bg="#ffff10",command=fun5)
B5.place(relx=0.58,rely=0.58,relwidth=0.1,relheight=0.10)

B6=tk.Button(window,text="cube",bd="6",bg="#ffff10",command=fun6)
B6.place(relx=0.72,rely=0.58,relwidth=0.1,relheight=0.10)

B7=tk.Button(window,text="!",bd="6",bg="#ffff10",command=fun7)
B7.place(relx=0.85,rely=0.58,relwidth=0.1,relheight=0.10)



L3=tk.Label(window,text="Result",bg="#ffffff",bd="9",textvariable=L4)
L3.place(relx=0.05,rely=0.72,relwidth=0.5,relheight=0.10)
     
     
     
     
                 
                 
                


