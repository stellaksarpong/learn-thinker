# from customtkinter import CTk,CTkButton,CTkEntry,CTkLabel
# window = CTk()
# window.title("Netflix")
# window.geometry("500x600")
# window.resizable(False,False)
# window.iconbitmap('netflix.ico')
# #creating button
# btn_click = CTkButton(window,text="Click")
# btn_click.place(x=70,y=120)

# btn_test= CTkButton(window, text="Press")
# btn_test.pack()

# #entry
# txt_user= CTkEntry(window,placeholder_text="Username",placeholder_text_color="white")
# txt_user.pack()

# txt_pass= CTkEntry(window,placeholder_text="Password",placeholder_text_color="white",show="*")
# txt_pass.pack()
# #lable

# lb_title= CTkLabel(window, text="Username")
# lb_title.pack()


# window.mainloop()


from customtkinter import CTk,CTkButton,CTkEntry,CTkLabel
from tkinter.messagebox import showinfo, showerror
window=CTk()
window.geometry("600x500+400+200")
window.resizable(False,False)
window.title("OpenLabs Plateform")
window.iconbitmap("netflix.ico")

def do_something():
    username=txt_username.get()
    password=txt_password.get()
    if username == 'admin' and password == '1234':
       showinfo("Success", "Login succesesfully") 
    else:
        showerror("Error","Invalid credential, try again")
       
#title widget
lb_title = CTkLabel(window, text="OpenLabs Portal",font=("arial",30),text_color='#4dabf7')
lb_username= CTkLabel(window,text="Username",font=('arial',20),text_color="white")
lb_password= CTkLabel(window,text="Password",font=("arial",20),text_color="white")


#entry

txt_username= CTkEntry(window,placeholder_text="Enter username", height=34, width=200)
txt_password= CTkEntry(window,placeholder_text="Enter password",show="*", height=34,width=200)


#button
btn_click= CTkButton(window, text="Login",height=40,font=('arial',20), command=do_something)


#display widget on windows
lb_title.pack()
lb_username.place(x=90,y=100)
txt_username.place(x=200,y=100)
lb_password.place(x=90, y= 150)
txt_password.place(x=200,y=150)
btn_click.place(x=220, y=200)

#display window
window.mainloop()











