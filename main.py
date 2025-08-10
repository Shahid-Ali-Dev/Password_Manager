
from tkinter import *
import json
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip

#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pa():
    inbox3.delete(0, END)
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_number =[(choice(numbers)) for _ in range(nr_numbers)]
    password_symbols =[(choice(symbols)) for _ in range(nr_symbols)]

    password_list = password_letter + password_number + password_symbols

    shuffle(password_list)

    final_pass = "".join(password_list)
    pyperclip.copy(final_pass)
    inbox3.insert(0,final_pass)

tk = Tk()
tk.title("Password Manager")
tk.config(pady=50,padx=50,bg="yellow")

def data():
    i1 = inbox1.get().title()
    i2 = inbox2.get()
    i3 = inbox3.get()

    new_data = {
        i1 :{"email": i2,
        "password": i3}
    }
    if i1 != "" and i2 != "" and i3 != "" :
        is_ok = messagebox.askyesno(title=inbox1.get(),message=f"You've provided: {i1} as Web name.\n"
                                                       f"Your password is: {i2}\nYour Email\\Username is:"
                                                       f" '{i3}'\nWould you like to save this information?")
        if is_ok:
            try:
                with open("data.json","r") as n:
                    da = json.load(n)
                    da.update(new_data)
            except:
                da = new_data

            with open("data.json", "w") as n:
                json.dump(da, n, indent=4)

            inbox1.delete(0,END)
            inbox3.delete(0, END)

    else:
        messagebox.showwarning(title="Unfilled Information", message="Please fill all the required information to save it.")

def se():
    try:
        with open("data.json","r") as n:
            d = json.load(n)
            em = d[inbox1.get().title()]["email"]
            p = d[inbox1.get().title()]["password"]
            messagebox.showinfo(title="Data.Json Folder",message=f"Here are the details for {inbox1.get().title()} website.\n"
                                                                 f"Your email is: {em}\nYour password is: {p}")

    except:
        messagebox.showwarning(title="Non-existent information",message="Sorry could not find the details of the provided website.")


image = PhotoImage(width= 200,height=200,file= "logo.png")
canvas = Canvas(highlightthickness=0,bg= "yellow")
canvas.create_image(150,150,image= image)
canvas.grid(row= 0,column = 1)

web = Label(text="Website :",bg="yellow")
web.grid(row=1,column=0)

email = Label(text= "Email\\Username :",bg="yellow")
email.grid(row=2, column=0,pady=5,padx=5)

password = Label(text= "Password :",bg="yellow")
password.grid(row=3, column=0)

password_row = Frame(bg="yellow")
password_row.grid(row=3, column=1)

frame = Frame(bg= "yellow")
frame.grid(row=1,column=1)

inbox1 = Entry(frame,width=22)
inbox1.grid(row=1,column=1)
inbox1.focus()

inbox2 = Entry(width= 40)
inbox2.insert(0,string="shahid3332210@gmail.com")
inbox2.grid(row=2,column=1)

inbox3 = Entry(password_row,width= 22)
inbox3.grid(row=3,column=1)

add_button = Button(text= "Add",width=34, bg="white",command=data)
add_button.grid(row=4,column=1,pady=5,padx=5)

generate = Button(password_row,text= "Generate password", width= 14, bg= "white",command=pa)
generate.grid(row= 3, column=2 ,padx=2)


searching = Button(frame, text= "Search", width=14,bg= "white",command=se)
searching.grid(row=1, column= 2,padx= 2)
tk.mainloop()