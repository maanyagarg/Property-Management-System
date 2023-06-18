from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

class vendorClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("933x720+347+0")
        self.root.title("Vendor")
        self.root.config(bg = "white")
        self.root.focus_force()

        # all variables
        self.vendor_id = StringVar()
        self.name = StringVar()
        self.PhoneNo = StringVar()
        self.work = StringVar()
        self.Address = StringVar()
        self.email = StringVar()
        self.searchBY = StringVar()
        self.searchtext = StringVar()

        style = ttk.Style();
        style.theme_use("clam")

        # search frame
        SearchFrame = LabelFrame(self.root, bg = "#CAD4FF", borderwidth=1)
        SearchFrame.place(x=60, y=630,width=824, height=65)
        # search through options 
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.searchBY, values = ("Select","vendor_id","Name","Phone_No","work"), state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "white")
        cmb_search.place(x=22, y = 18,width=172, height = 35)
        cmb_search.current(0)

        # text search
        txt_search = Entry(SearchFrame, textvariable=self.searchtext, font = ("Times New Roman", 17), bg = "white", relief = "solid", borderwidth=1, foreground="black")
        txt_search.place(x=254, y=18, height=35, width=345)

        # search button
        search_button = Button(SearchFrame,command=self.search, text="Search", font = ("Times New Roman", 17, "bold"), bg = "white", borderwidth=1, cursor= "hand2")
        search_button.place(x=645, y = 18, height = 35, width = 142)

        # content
        label_vendor_id = Label(self.root, text = "Vendor ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=260)
        label_name = Label(self.root, text = "Name:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=320)
        label_PhoneNo = Label(self.root, text = "Phone No:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=380)
        label_work = Label(self.root, text = "Work:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=440)
        label_address = Label(self.root, text = "Address:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=500)
        label_email = Label(self.root, text = "email:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=560)
       

        # entry
        entry_vendor_id = Entry(self.root, textvariable=self.vendor_id, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=260, width = 284, height = 30)
        entry_name = Entry(self.root, textvariable=self.name, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=320, width = 284, height = 30)
        entry_PhoneNo = Entry(self.root, textvariable=self.PhoneNo, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=285,y=380, width = 284, height = 30)
        entry_work = Entry(self.root, textvariable=self.work, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=285,y=440, width = 284, height = 30)
        entry_address = Entry(self.root, textvariable = self.Address, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=500, width = 284, height = 30)
        entry_email = Entry(self.root, textvariable=self.email, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=560, width = 284, height = 30)
       

        # buttons
        button_save = Button(self.root, text="Save",command=self.insert,font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 300, height = 35, width = 142)
        button_update = Button(self.root, text="Update",command = self.update, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 360, height = 35, width = 142)
        button_delete = Button(self.root, text="Delete", command=self.delete, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 420, height = 35, width = 142)
        button_clear = Button(self.root, text="Clear", command = self.clear,font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 480, height = 35, width = 142)

        # preview of database
        self.vendor_data_Frame = Frame(self.root)
        self.vendor_data_Frame.place(x=30, y = 200, width = 1220)
        self.vendor_data_Frame.pack()

        
        self.vendorTable = ttk.Treeview(self.vendor_data_Frame, columns = ("vendor_id", "name", "phone_no", "work", "address", "email"), selectmode=BROWSE)
        
        #scroll-bar
        scroll_y = Scrollbar(self.vendor_data_Frame, orient=VERTICAL, command=self.vendorTable.yview)
        scroll_x = Scrollbar(self.vendor_data_Frame, orient=HORIZONTAL, command=self.vendorTable.xview)
        scroll_x.pack(side=BOTTOM,fill = "x" )
        scroll_y.pack(side=RIGHT, fill = "y")

        self.vendorTable.heading("vendor_id", text = "VENDOR ID")
        self.vendorTable.heading("name", text = "Name")
        self.vendorTable.heading("phone_no", text = "Phone No.")
        self.vendorTable.heading("work", text = "Aadhaar No.")
        self.vendorTable.heading("address", text = "Address")
        self.vendorTable.heading("email", text = "Email")

        self.vendorTable["show"] = "headings"

        self.vendorTable.column("vendor_id", width=100)
        self.vendorTable.column("name", width=130)
        self.vendorTable.column("phone_no", width=130)
        self.vendorTable.column("work", width=130)
        self.vendorTable.column("address", width=220)
        self.vendorTable.column("email", width=220)

        self.vendorTable.pack(fill = BOTH, expand= TRUE)
        self.vendorTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        #event
        self.vendorTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

        # functions related to databases to 
    #save
    def insert(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.vendor_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.work.get()==""):
                messagebox.showerror("ERROR", "vendor ID, Name, Phone No., work is required", parent = self.root)
    
            else:
                print(self.vendor_id.get())
                connection_cursor.execute("SELECT * FROM vendor WHERE vendor_id=?",(self.vendor_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "This vendor ID is already assigned, try different ID", parent = self.root)
                else:

                    connection_cursor.execute("INSERT INTO vendor (vendor_id, name, phone_no, work, address, email) VALUES(?,?,?,?,?,?)",(
                        self.vendor_id.get(),
                        self.name.get(),
                        self.PhoneNo.get(),
                        self.work.get(),
                        self.Address.get(),
                        self.email.get(),
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "vendor added successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #update
    def update(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.vendor_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.work.get()==""):
                messagebox.showerror("ERROR", "vendor ID, Name, Phone No., work is required", parent = self.root)
    
            else:
                print(self.vendor_id.get())
                connection_cursor.execute("SELECT * FROM vendor WHERE vendor_id=?",(self.vendor_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid vendor ID", parent = self.root)
                else:
                    connection_cursor.execute("UPDATE vendor SET name = ?, phone_no = ?, work = ?, address = ?, email = ? WHERE vendor_id = ?",(
                        self.name.get(),
                        self.PhoneNo.get(),
                        self.work.get(),
                        self.Address.get(),
                        self.email.get(),
                        self.vendor_id.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "vendor updated successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #delete
    def delete(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.vendor_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.work.get()==""):
                messagebox.showerror("ERROR", "vendor ID, Name, Phone No., work is required", parent = self.root)
    
            else:
                print(self.vendor_id.get())
                connection_cursor.execute("SELECT * FROM vendor WHERE vendor_id=?",(self.vendor_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid vendor ID", parent = self.root)
                else:
                    permission = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if permission == YES:
                        connection_cursor.execute("DELETE FROM vendor WHERE vendor_id = ?", (self.vendor_id.get()))
                        connection.commit()
                        messagebox.showinfo("Delete", "vendor deleted successfully", parent = self.root)
                        self.clear()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #clear
    def clear(self):
        self.vendor_id.set(""),
        self.name.set(""),
        self.PhoneNo.set(""),
        self.work.set(""),
        self.Address.set(""),
        self.email.set(""),
        self.searchBY.set("Select"),
        self.searchtext.set("")
        self.show_data()

    def get_data(self, ev):
        focused_tuple = self.vendorTable.focus()
        content_tuple = self.vendorTable.item(focused_tuple)
        row = content_tuple['values']
        print(row)
        self.vendor_id.set(row[0]),
        self.name.set(row[1]),
        self.PhoneNo.set(row[2]),
        self.work.set(row[3]),
        self.Address.set(row[4]),
        self.email.set(row[5])

    def show_data(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            connection_cursor.execute("Select * FROM vendor")
            rows = connection_cursor.fetchall()

            self.vendorTable.delete(*self.vendorTable.get_children())
            for row in rows:
                self.vendorTable.insert('', END, values = row)
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    def search(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.searchBY.get() == "Select"):
                messagebox.showerror("ERROR", "Select Search by option", parent = self.root)
            elif (self.searchtext.get()==""):
                messagebox.showerror("ERROR", "Select Input should be required", parent = self.root)
            else:
                connection_cursor.execute("SELECT * FROM vendor WHERE "+self.searchBY.get()+" LIKE '%" + self.searchtext.get()+ "%'")
                rows = connection_cursor.fetchall()
                if(len(rows)!=0):
                    self.vendorTable.delete(*self.vendorTable.get_children())
                    for row in rows:
                        self.vendorTable.insert("",END, values = row)
                else:
                    messagebox.showerror("Error", "No record found!")
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")



if __name__ == "__main__":
    root = Tk()
    obj = vendorClass(root)
    root.mainloop()