import tkinter as tk                #importing tkinter module
from PIL import ImageTk, Image      #importing PIL for image processing. 

def back():
    Encode_tk.destroy()
    First_Screen()

def Encode():
    S_Screen.destroy()

    global Encode_tk
    
    Encode_tk = tk.Tk()
    
    Encode_tk.title("Encode")
    
    Encode_tk.geometry("700x700")

    bg_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\bg_en.jpg") #image path

    bg_img = ImageTk.PhotoImage(bg_img_load) #rendering image

    bg_label = tk.Label(master= Encode_tk, image = bg_img) #background image Label

    bg_label.place(x = 0, y= 0) #placing the Bg

    back_button_img_load = Image.open("C:\\Users\\u\\Desktop\\py programmes\\Tkinter_Programmes\\Stegnographer\\bbl.png") #loading back button image

    back_button_img = ImageTk.PhotoImage(back_button_img_load) #rendering image

    back_button = tk.Button(master= Encode_tk, image = back_button_img,bd = 0,command = back) #button widgets

    back_button.place(x = 0,y= 2)

    file_name_entry = tk.Entry(bd = 0.1)

    file_name_entry.place(x = 330, y = 194,height = 30,width = 242)

    message_text = tk.Text(bd = 0)

    message_text.place(x = 330 , y = 260,width = 240, height = 180)

        #Working here


    


    


    Encode_tk.mainloop()

def close_open():
    window.destroy()
    First_Screen()

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
    
    decode_b = tk.Button(master=S_Screen, image = decode_img , bd =0, activebackground = "#d8d8d8",relief = tk.SOLID)
    
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
    
window_close_button.place(x = 505, y = 400)
    
greeting.place(x = 200, y = 250)
    
Background_Label.place(x = 0, y = -3)

window.mainloop()

