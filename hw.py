from tkinter import *
from tkinter import messagebox
def add():    
    color=input1.get()
    colors.append(color)
    listbox.insert(END,color)
    input1.delete(0,END)

def apply():
    try:
        index=listbox.curselection()[0]
        selected_color=colors[index]
        root.config(bg=selected_color)
        frame.config(bg=selected_color)
    except IndexError:
        messagebox.showerror("ERROR","CHOOSE A COLOR TO APPLY")
        
def remove():
    index=listbox.curselection()
    if index:
        listbox.delete(index)


root=Tk()

root.title("Colors")
root.config(background="#4FDD4A")

input1=Entry(root,font=("consolas",13,"bold"),fg="#000000",width=30)
input1.pack(pady=10)
colors=["black","#FFFFFF","gray","#0000FF","#00FF00"]

listbox=Listbox(root,width=30,font=("consolas",16,"bold"))

for color in colors:
    listbox.insert(END,color)

listbox.pack(padx=10,pady=10)

frame=Frame(root,bg="#4FDD4A")
frame.pack(padx=10,pady=10)

add_btn=Button(frame,text="ADD",font=("consolas",15,"bold"),fg="#000000",bg="#4FDD4A",border=3,width=7,command=add)
add_btn.pack(side=LEFT,padx=5)

apply_btn=Button(frame,text="APPLY",font=("consolas",15,"bold"),fg="#000000",bg="#4FDD4A",border=3,width=7,command=apply)
apply_btn.pack(side=LEFT,padx=5)

remove_btn=Button(frame,text="REMOVE",font=("consolas",15,"bold"),fg="#000000",bg="#4FDD4A",border=3,width=7,command=remove)
remove_btn.pack(side=LEFT,padx=5)


root.mainloop()
