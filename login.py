from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os
import smtplib 
import credentials
import time

class login_page:
    def __init__ (self, root):
        #initial declaration of gemeotry etc.
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("LOGIN | Property Management System | Developed by Manav and Manya")
        self.root.config(bg="#AEBBF2")

        style = ttk.Style()
        style.theme_use("clam")

        #white rectangle
        self.canvas = Canvas(self.root, width=502, height = 510, borderwidth=0, highlightthickness=0)
        self.canvas.place(x=384, y=105)
        self.canvas.create_rectangle(0,0,502,510,fill="white")
        
        #image
        self.image = Image.open("image.png")
        self.resized_image = self.image.resize((250, 135))

        self.image_open = ImageTk.PhotoImage(self.resized_image)
        self.image_label = Label(self.root, image=self.image_open, borderwidth=0, highlightthickness=0)
        self.image_label.place(x=510, y = 40)

        #main
        self.admin_id = StringVar()
        self.password = StringVar()
        self.otp = StringVar()
        self.new_password = StringVar()
        self.confirm_new_password = StringVar()
        self.get_otp = StringVar()

        admin_id_label = Label(self.canvas, text="Admin_ID", font = ("Times New Roman", 20), background="white", foreground="black").place(x = 30, y = 80)
        password_label = Label(self.canvas, text="Password", font = ("Times New Roman", 20), background="white", foreground="black").place(x = 30, y = 160)

        admin_id_entry = Entry(self.canvas, textvariable= self.admin_id, font = ("Times New Roman", 20),background="#E6E6E6" ,relief = "ridge", borderwidth=0.2, foreground="black").place(x=30,y=113, width = 440, height = 33)
        password_entry = Entry(self.canvas, textvariable= self.password, font = ("Times New Roman", 20),background="#E6E6E6", relief = "ridge", borderwidth=0.2, foreground="black").place(x=30,y=193, width = 440, height = 33)

        button_login = Button(self.canvas, text="Login", command = self.login_button ,font = ("Times New Roman",20, "bold"), bg = "#AEBBF2", borderwidth=0, cursor= "hand2").place(x=30, y = 250, height = 44, width = 442)
        button_forgot_password = Button(self.root, text = "Forget Password?", command=self.forget_password_button, font= ("Times New Roman", 19), background="white", foreground="black", cursor="hand2",borderwidth=0).place(x=550, y = 430)

        footer = Label(self.root, text = "A desktop based application for Property Management. Made by: Manav Mittal and Manya Garg", font = ("Times New Roman",20), background="white", foreground="black").place(x=0,y=680,width=1280, height = 40)

    def login_button(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if(self.admin_id.get()=="" or self.password.get() == ""):
                messagebox.showerror("Error", "All fields are required", parent = self.root)
            else:
                connection_cursor.execute("SELECT password FROM ADMIN where admin_id = ?", (
                    self.admin_id.get(),
                ))

                password = connection_cursor.fetchmany()
                print(password)
                # print(password[0])
                if(password == []):
                    messagebox.showerror("ERROR", "No such admin\nINVALID ADMIN_ID/PASSWORD", parent = self.root)
                elif(password[0][0]!=self.password.get()):
                    messagebox.showerror("ERROR", "Incorrect Password", parent = self.root)
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")

        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    def forget_password_button(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.admin_id.get() == ""):
                messagebox.showerror("Error", "Admin ID. is required to change the password", parent = self.root)
            else:
                connection_cursor.execute("SELECT email FROM ADMIN where admin_id = ?", (
                    self.admin_id.get(),
                ))

                admin_gmail = connection_cursor.fetchall()
                print(admin_gmail)
                if(admin_gmail == []):
                    messagebox.showerror("Error", "No such Admin_ID present\nTRY AGAIN", parent = self.root)
                else:
                    print(admin_gmail[0][0])
                    check = self.send_mail(admin_gmail[0][0])
                    if (check == "F"):
                        messagebox.showerror("Error", "Connection Error\nTry Again Later", parent = self.root)
                    else:
                        self.forget_password_window = Toplevel(self.root)
                        self.forget_password_window.title("RESET PASSWORD")
                        self.forget_password_window.geometry("502x510+384+105")
                        self.forget_password_window['background'] = "#AEBBF2"
                        self.forget_password_window.focus_force()

                        #designing of the reset password window
                        otp_label = Label(self.forget_password_window, text="Enter the OTP sent to your registered email :", font=("Times New Roman", 19), background="#AEBBF2", foreground="black").place(x=20, y=30)
                        otp_entry = Entry(self.forget_password_window, textvariable=self.get_otp, font = ("Times New Roman", 20), relief = "ridge", borderwidth=0, foreground="black", background="white").place(x= 20, y = 63, width = 286, height = 40)
                        self.otp_submit_button = Button (self.forget_password_window, text = "Submit",command = self.submit_function, font = ("Times New Roman",20, "bold"), bg = "white", borderwidth=0, cursor= "hand2")
                        self.otp_submit_button.place(x= 335, y = 63, width = 132, height= 40)
                        new_password_label = Label(self.forget_password_window, text="New Password :", font=("Times New Roman", 21), background="#AEBBF2", foreground="black").place(x=20, y=150)
                        new_password_entry = Entry(self.forget_password_window, textvariable=self.new_password, font = ("Times New Roman", 20), relief = "ridge", borderwidth=0, foreground="black", background="white").place(x= 20, y = 183, width = 460, height = 40)
                        confirm_new_password_label = Label(self.forget_password_window, text="Confirm New Password :", font=("Times New Roman", 21), background="#AEBBF2", foreground="black").place(x=20, y=240)
                        confirm_new_password_entry = Entry(self.forget_password_window, textvariable=self.confirm_new_password, font = ("Times New Roman", 20), relief = "ridge", borderwidth=0, foreground="black", background="white").place(x= 20, y = 277, width = 460, height = 40)
                        self.update_button = Button(self.forget_password_window,state = DISABLED, command = self.update_password, text = "Update",font = ("Times New Roman",20, "bold"), bg = "white", borderwidth=0, cursor= "hand2")
                        self.update_button.place(x= 20, y = 340, width = 460, height= 45)

        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    def submit_function(self):
        if(int(self.otp) == int(self.get_otp.get())):
            self.update_button.config(state=NORMAL)
            self.otp_submit_button.config(state=DISABLED)
        else:
            messagebox.showerror("Error", "Invalid OTP\nTry Again!", parent = self.forget_password_window)


    def update_password(self):
        if(self.new_password.get()== "" or self.confirm_new_password == ""):
            messagebox.showerror("Error", "New Password is required\nTry Again!", parent = self.forget_password_window)
        elif(self.new_password.get()!= self.confirm_new_password.get()):
            messagebox.showerror("Error", "New Password and Confirm Password must be same", parent = self.forget_password_window)
        else:
            connection = sqlite3.connect("Property_Management.db")
            connection_cursor = connection.cursor()
            try:
                connection_cursor.execute("UPDATE ADMIN SET password = ? WHERE admin_id = ?",(
                    self.new_password.get(),
                    self.admin_id.get()
                ))
                connection.commit()
                row = connection_cursor.fetchone()
                print(row)
                messagebox.showinfo("Success","Password Updated Sucessfully", parent = self.forget_password_window)
                self.forget_password_window.destroy()

            except Exception as exc:
                messagebox.showerror("Error", f"Error due to: {str(exc)}")

    def send_mail(self, to):
        print(to)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email = credentials.email
        password = credentials.password

        s.login(email, password)
        
        self.otp = int(time.strftime("%M%H%S")) + int(time.strftime("%M"))
        print(self.otp)

        subject = "Mittal-Properties : Reset Password One Time Password (OTP)"
        message = f"Respected Sir/Ma'am\n\nYour OTP for Reset Password is {str(self.otp)}.\n\nWith Regards,\nMittal Properties Development Team"
        message = "Subject:{}\n\n{}".format(subject, message)
        print(message)
        s.sendmail(email, to, message)
        check = s.ehlo()

        if check[0] == 250:
            return "S"
        else:
            return "F"


# dashboard wali file mai add karlena
# def logout(self):
#     self.root.destroy()
#     os.system(python login.py)

root=Tk()
obj=login_page(root)
root.mainloop()