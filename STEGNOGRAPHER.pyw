import tkinter as tk                #importing tkinter module
from PIL import ImageTk, Image      #importing PIL for image processing. 
import tkinter.filedialog as tf
from stegano import exifHeader as stg
from tkinter import messagebox


def close_open():
    window.destroy()
    First_Screen()

def back_decode():
    Decode_tk.destroy()
    First_Screen()

def back():
    Encode_tk.destroy()
    First_Screen()

def Encode():
    S_Screen.destroy()

    global Encode_tk
    
    Encode_tk = tk.Tk()
    
    Encode_tk.title("Encode")
    
    Encode_tk.geometry("700x700")

    bg_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\bg_en.jpg")

    bg_img = ImageTk.PhotoImage(bg_img_load)

    bg_label = tk.Label(master= Encode_tk, image = bg_img)

    bg_label.place(x = 0, y= 0)

    back_button_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\bb.png")

    back_button_img = ImageTk.PhotoImage(back_button_img_load)

    back_button = tk.Button(master= Encode_tk, image = back_button_img,bd = 0,command = back)

    back_button.place(x = 0,y= 2)

    file_name_entry = tk.Entry(bd = 0.1)

    file_name_entry.place(x = 330, y = 194,height = 30,width = 242)

    message_text = tk.Text(bd = 0)

    message_text.place(x = 330 , y = 260,width = 240, height = 120)

    Encode_button_img_load =  Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\encode_b.png")

    Encode_button_img = ImageTk.PhotoImage(Encode_button_img_load)

    def openfile():
        global fileopen

        fileopen = tk.StringVar()

        fileopen = tf.askopenfilename(initialdir = "/Desktop", title = "Select File", filetypes = (("jpeg file", "*jpg"), ("all files","*.*")))

        dirlabel = tk.Entry(master = Encode_tk,bd= 0)

        dirlabel.insert(0, fileopen)

        dirlabel.place(x = 329, y = 402, width = 240, height = 35)

    def Encodee():  	
        response = messagebox.askyesno("pop up", "Do you want to encode?")
        
        if response == 1:    
        
            stg.hide(fileopen, file_name_entry.get()+'..jpg',message_text.get(1.0, tk.END))
            
        
            messagebox.showinfo("pop up", "Successfully encode")
        
        else:
        
            messagebox.showwarning('pop up', "Unsuccessful")

    Encode_button = tk.Button(master=Encode_tk, image = Encode_button_img, bd = 0, command = Encodee)

    Encode_button.place(x =  240, y = 520,height = 68)

    


    select_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\selcet.png")
    
    select_img = ImageTk.PhotoImage(select_img_load)

    select_button = tk.Button(master=Encode_tk,image = select_img, bd = 0,relief = tk.GROOVE, command = openfile)

    select_button.place(x = 160, y = 400)
    
    Encode_tk.mainloop()

def Decode():
    S_Screen.destroy()

    global Decode_tk

    Decode_tk = tk.Tk()

    Decode_tk.title("Decode")

    Decode_tk.geometry("700x700")

    bg_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\bg_en.jpg")

    bg_img = ImageTk.PhotoImage(bg_img_load)

    bg_label = tk.Label(master= Decode_tk, image = bg_img)

    bg_label.place(x = 0, y= 0)

    back_button_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\bb.png")

    back_button_img = ImageTk.PhotoImage(back_button_img_load)

    back_button = tk.Button(master= Decode_tk, image = back_button_img,bd = 0,command = back_decode)

    back_button.place(x = 0,y= 2)

    file_name_entry = tk.Entry(bd = 0.1)

    file_name_entry.place(x = 330, y = 194,height = 30,width = 242)

    message_text = tk.Text(bd = 0)

    message_text.place(x = 330 , y = 260,width = 240, height = 100)

    def openfile():
        global fileopen1

        fileopen1 = tk.StringVar()

        fileopen1 = tf.askopenfilename(initialdir = "/Desktop", title = "Select File", filetypes = (("jpeg file", "*jpg"), ("all files","*.*")))

        file_name_entry.insert(0,fileopen1)

    def Decodee():
        message = stg.reveal(fileopen1)

        message_text.insert("1.0", message)

    select_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\selcet1.png")
    
    select_img = ImageTk.PhotoImage(select_img_load)

    select_button = tk.Button(master=Decode_tk,image = select_img, bd = .3,command = openfile)

    select_button.place(x = 280, y = 130)

    Decode_button_img_load =  Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\decodeb.jpg")

    Decode_button_img = ImageTk.PhotoImage(Decode_button_img_load)
    
    Decode_button = tk.Button(master=Decode_tk, image = Decode_button_img, bd = 0,command = Decodee)

    Decode_button.place(x =  250, y = 520)

    Decode_tk.mainloop()


def First_Screen():
    global S_Screen
    S_Screen = tk.Tk()                  #creating tkinter instance.
    S_Screen.title("Steganographer By D")
    S_Screen.geometry("1200x800")

    S_Screen.maxsize(1200,800)
    S_Screen.minsize(1200,800)
    
    Logo_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\data-encryption.png")

    Logo_image = ImageTk.PhotoImage(Logo_load)

    Logo_label = tk.Label(master= S_Screen, image = Logo_image)

    Logo_label.place(x = 420, y = 80)

    encode_img = ImageTk.PhotoImage(file="C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\button.png")
    
    encode_b = tk.Button(master=S_Screen, image = encode_img , bd =0, activebackground = "#d8d8d8",relief = tk.GROOVE, command = Encode)
    
    encode_b.place(x = 230, y = 400)
    
    decode_img = ImageTk.PhotoImage(file="C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\button (1).png")
    
    decode_b = tk.Button(master=S_Screen, image = decode_img , bd =0, activebackground = "#d8d8d8",relief = tk.SOLID,command = Decode)
    
    decode_b.place(x = 670 , y= 400)

    S_Screen.mainloop()




window = tk.Tk()

window.title("Steganographer By D")

window.geometry("1200x800")
    
Background_image = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\bg.jpg")
    
rendered_image = ImageTk.PhotoImage(Background_image)

Background_Label = tk.Label(master=window, image = rendered_image)

greeting = tk.Label(master = window,text = "WEL-COME IN STEGANOGRPHER")

greeting.config(font = ("Courier", 44))

Close_button_image_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\click.png")

Close_button_image = ImageTk.PhotoImage(Close_button_image_load)

window_close_button = tk.Button(image = Close_button_image, bd = 0, command = close_open)
    
window_close_button.place(x = 460, y = 400)
    
greeting.place(x = 200, y = 250)
    
Background_Label.place(x = 0, y = -3)

window.mainloop()
