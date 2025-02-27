import qrcode
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk , filedialog ,messagebox


def CreateQr(*args):
    data=Entry_text.get()
    if data:
        img=qrcode.make(data)
        resized_img=img.resize((230,240))
        tkimage=ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0,0,anchor=tk.NW,image=tkimage)
        qr_canvas.image=tkimage
    else:
        messagebox.showwarning("Error","Enter some Data first")
    

def SaveQr(*agr):
     data=Entry_text.get()
     if data:
        img=qrcode.make(data)
        resized_img=img.resize((230,240))
        
        path=filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Sucess","QR Code is saved")
            
        else:
            messagebox.showwarning("Error","Enter some Data first")


root=tk.Tk()
root.title("QR maker ")
root.geometry("250x350")
root.config(bg="white")
root.resizable(0,0)

frame1=tk.Frame(root,bd=2,relief=tk.RAISED)
frame1.place(x=10,y=10,width=230,height=240)

frame2=tk.Frame(root,bd=2,relief=tk.RAISED)
frame2.place(x=10,y=260,width=230,height=80)

cover_img=tk.PhotoImage(file="Qr.png")
qr_canvas=tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW,image=cover_img)
qr_canvas.image=cover_img
qr_canvas.bind("<Double-1>",SaveQr)
qr_canvas.pack(fill=tk.BOTH)

Entry_text=ttk.Entry(frame2,width=26,font=("Sitka samll",11) ,background="blue",justify=tk.CENTER)
Entry_text.bind("<Return>",CreateQr)
Entry_text.place(x=5,y=5)

b1=ttk.Button(frame2,text="Create",width=10,command=CreateQr)
b1.place(x=10,y=40)

b1=ttk.Button(frame2,text="Save",width=10,command=SaveQr)
b1.place(x=80,y=40)

b1=ttk.Button(frame2,text="Exit",width=10,command=root.quit)
b1.place(x=150,y=40)

root.mainloop()