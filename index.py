from customtkinter import CTk,CTkLabel,CTkFrame,CTkEntry,CTkComboBox,CTkRadioButton,CTkButton

window= CTk()
window.geometry("400x500")
window.title("Create a New Account")

#title label
title_label=CTkLabel(window,text="Create a new account", font=("Arial", 20, "bold"))
title_label.pack(pady=5)

# subtitle label
subtitle_label=CTkLabel(window,text="it`s quick and easy ", font=("Arial", 14, "bold"))
subtitle_label.pack(pady=5)

#first and lastname

first=CTkFrame(window)
first.pack(pady=10)
first_name=CTkEntry(first,placeholder_text="First name", width=150)
first_name.grid(row=0, column=0,padx=5)
last_name =CTkEntry(first,placeholder_text="Last name", width=150)
last_name.grid(row=0, column=1,padx=5)


#birthday label

bd_label=CTkLabel(window,text="Birthday")
bd_label.pack(pady=5)
first_bd=CTkFrame(window)
first_bd.pack(pady=5)

bd_month=CTkComboBox(first_bd ,values=[ "Jan","Feb","Mar","April","May","Jun","July","Aug","Sep","Oct","Nov","Dec"], width=80)
bd_month.grid(row=0, column=0, padx=5)
bd_day=CTkComboBox(first_bd,values=[str(i) for i in range(1,32)], width=50)
bd_day.grid(row=0, column=1, padx=5)
bd_year=CTkComboBox(first_bd, values=[str(i) for i in range(1900,2026)], width=80)
bd_year.grid(row=0, column=2,padx=5)


gd_label=CTkLabel(window,text="Gender")
gd_label.pack(pady=5)
first_gd=CTkFrame(window)
first_gd.pack(pady=5)

gd_female=CTkRadioButton(first_gd, text="Female" , value="Female")
gd_female.grid(row=0, column=0 , padx=10)
gd_male=CTkRadioButton(first_gd, text="Male" , value="Male")
gd_male.grid(row=0, column=1 , padx=10)
gd_custom=CTkRadioButton(first_gd, text="Custom" , value="Custom")
gd_custom.grid(row=0, column=2 , padx=10)


mb_num=CTkEntry(window,placeholder_text="Enter phone number or email", width= 300)
mb_num.pack(pady=10)

password=CTkEntry(window,placeholder_text="Enter password", width= 300, show=("*"))
password.pack(pady=10)

signup=CTkButton(window,text="Signup",fg_color="green",text_color="white", command=lambda: print("Account Created") )
signup.pack(pady=20)

link=CTkLabel(window,text="Already have Account",font=("arial",12,"italic"))
link.pack(pady=5)




window.mainloop()