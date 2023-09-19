import random
from tkinter import *
from tkinter import messagebox
from random import shuffle,random,choice,randint
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_usarname_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:

        messagebox.showinfo(title="Ooops", message="Please make sure you haven't left any parts")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                       f"\nPassword: {password} \nWebsite: {website} \n İs it ok to save ? ")

        if is_ok:
            with open('data.txt',"a") as data_file:
                data_file.write(f"{website} I {email} I {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                email_usarname_entry.delete(0,END)






# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=75,pady=75,bg='white')


canvas = Canvas(width=200, height=200, bg='white',highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image= image)
canvas.grid(column=1,row=0)

website_label = Label(text='Website:',bg="white",highlightthickness=0)
website_label.grid(column=0,row=1)
email_usarname_laber = Label(text="Email/Usarname:",bg="white",highlightthickness=0)
email_usarname_laber.grid(column=0,row=2)
password_label = Label(text="Password:",bg="white",highlightthickness=0)
password_label.grid(column=0,row=3)

website_entry = Entry(width= 35,highlightthickness=0)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
email_usarname_entry = Entry(width= 35,highlightthickness=0)
email_usarname_entry.grid(column=1,row=2,columnspan=2)
password_entry = Entry(width= 17,highlightthickness=0)
password_entry.grid(column=1,row=3)


generate_password_button = Button(text="Generate Password",width=15,command= generate_password)
generate_password_button.grid(column=2,row=3)
add_button = Button(text="Add",width=30,command=save)
add_button.grid(column=1,row=4,columnspan=2)







window.mainloop()
