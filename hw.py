from tkinter import *

def converter():
    KG=input1.get()
    if KG.replace(".","",1).isdigit():
        Pounds=float(KG)*2.20462
        Grams=float(KG)*1000
        output.config(text=f"The weight in grams is: {Grams} grams\nThe Weight in pounds is: {Pounds} pounds")

root=Tk()
root.geometry("750x500")
root.title("weight converter")
root.config(background="#36413E")
lbl_heading=Label(root,text="KG --> Grams And Pounds", font=("consolas",15,"bold"),bg="#36413E",fg="#537A5A")
lbl_heading.place(x=0,y=0)
input1=Entry(root)
input1.place(x=475,y=106)
lbl_input=Label(root,text="Input the weight you want to convert:", font=("consolas",15,"bold"),bg="#36413E",fg="#537A5A")
lbl_input.place(x=50,y=100)

output=Label(root,font=("consolas",20,"bold"),bg="#36413E",fg="#537A5A")
output.place(x=75,y=300)
             
convertBut=Button(root,text="Convert",font=("consolas",18,"bold"),bg="#36413E",fg="#537A5A",command=converter)
convertBut.place(x=315,y=200)




root.mainloop()
