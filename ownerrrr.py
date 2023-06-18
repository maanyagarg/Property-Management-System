from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

class ownerClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("933x720+347+0")
        self.root.title("Owner")
        self.root.config(bg = "white")
        self.root.focus_force()

        # all variables
        self.owner_id = StringVar()
        self.name = StringVar()
        self.PhoneNo = StringVar()
        self.Address = StringVar()
        self.AadharNo = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.pincode = StringVar()
        self.searchBY = StringVar()
        self.searchtext = StringVar()

        style = ttk.Style();
        style.theme_use("clam")

        # search frame
        SearchFrame = LabelFrame(self.root, bg = "#CAD4FF", borderwidth=1)
        SearchFrame.place(x=60, y=630,width=824, height=65)
        # search through options 
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.searchBY, values = ("Select","owner_ID","Name","Phone No.", "City", "State"), state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "white")
        cmb_search.place(x=22, y = 18,width=172, height = 35)
        cmb_search.current(0)

        # text search
        txt_search = Entry(SearchFrame, textvariable=self.searchtext, font = ("Times New Roman", 17), bg = "white", relief = "solid", borderwidth=1, foreground="black")
        txt_search.place(x=254, y=18, height=35, width=345)

        # search button
        search_button = Button(SearchFrame,command=self.search, text="Search", font = ("Times New Roman", 17, "bold"), bg = "white", borderwidth=1, cursor= "hand2")
        search_button.place(x=645, y = 18, height = 35, width = 142)

        # content
        label_owner_id = Label(self.root, text = "ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=260)
        label_name = Label(self.root, text = "Name:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=300)
        label_PhoneNo = Label(self.root, text = "Phone No:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=340)
        label_AadharNo = Label(self.root, text = "Aadhar No:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=380)
        label_address = Label(self.root, text = "Address:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=420)
        label_city = Label(self.root, text = "City:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=460)
        label_state = Label(self.root, text = "State:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=500)
        label_pincode = Label(self.root, text = "Pincode:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=540)

        # entry
        entry_owner_id = Entry(self.root, textvariable=self.owner_id, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=260, width = 284, height = 30)
        entry_name = Entry(self.root, textvariable=self.name, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=300, width = 284, height = 30)
        entry_PhoneNo = Entry(self.root, textvariable=self.PhoneNo, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=285,y=340, width = 284, height = 30)
        entry_AadharNo = Entry(self.root, textvariable=self.AadharNo, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=285,y=380, width = 284, height = 30)
        entry_address = Entry(self.root, textvariable = self.Address, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=420, width = 284, height = 30)
        entry_city = Entry(self.root, textvariable=self.city, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=460, width = 284, height = 30)
        entry_state = Entry(self.root, textvariable=self.state, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=500, width = 284, height = 30)
        entry_pincode = Entry(self.root, textvariable=self.pincode, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=540, width = 284, height = 30)

        # buttons
        button_save = Button(self.root, text="Save",command=self.insert,font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 300, height = 35, width = 142)
        button_update = Button(self.root, text="Update",command = self.update, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 350, height = 35, width = 142)
        button_delete = Button(self.root, text="Delete", command=self.delete, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 400, height = 35, width = 142)
        button_clear = Button(self.root, text="Clear", command = self.clear,font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 450, height = 35, width = 142)

        # preview of database
        self.owner_data_Frame = Frame(self.root)
        self.owner_data_Frame.place(x=30, y = 200, width = 1220)
        self.owner_data_Frame.pack()

        
        self.OwnerTable = ttk.Treeview(self.owner_data_Frame, columns = ("owner_id", "name", "phone_no", "aadhaar_no", "address", "city", "state", "pincode"), selectmode=BROWSE)
        
        #scroll-bar
        scroll_y = Scrollbar(self.owner_data_Frame, orient=VERTICAL, command=self.OwnerTable.yview)
        scroll_x = Scrollbar(self.owner_data_Frame, orient=HORIZONTAL, command=self.OwnerTable.xview)
        scroll_x.pack(side=BOTTOM,fill = "x" )
        scroll_y.pack(side=RIGHT, fill = "y")

        self.OwnerTable.heading("owner_id", text = "ID")
        self.OwnerTable.heading("name", text = "Name")
        self.OwnerTable.heading("phone_no", text = "Phone No.")
        self.OwnerTable.heading("aadhaar_no", text = "Aadhaar No.")
        self.OwnerTable.heading("address", text = "Address")
        self.OwnerTable.heading("city", text = "City")
        self.OwnerTable.heading("state", text = "State")
        self.OwnerTable.heading("pincode", text = "Pincode")

        self.OwnerTable["show"] = "headings"

        self.OwnerTable.column("owner_id", width=50)
        self.OwnerTable.column("name", width=130)
        self.OwnerTable.column("phone_no", width=120)
        self.OwnerTable.column("aadhaar_no", width=120)
        self.OwnerTable.column("address", width=300)
        self.OwnerTable.column("city", width=100)
        self.OwnerTable.column("state", width=110)
        self.OwnerTable.column("pincode", width=100)

        self.OwnerTable.pack(fill = BOTH, expand= TRUE)
        self.OwnerTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        #event
        self.OwnerTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()
    # functions related to databases to 
    #save
    def insert(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.owner_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.AadharNo.get()==""):
                messagebox.showerror("ERROR", "Owner ID, Name, Phone No., Aadhaar No. is required", parent = self.root)
    
            else:
                print(self.owner_id.get())
                connection_cursor.execute("SELECT * FROM OWNER WHERE owner_id=?",(self.owner_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "This Owner ID is already assigned, try different ID", parent = self.root)
                else:

                    connection_cursor.execute("INSERT INTO OWNER (owner_id, name, phone_no, aadhaar_no, address, city, state, pincode) VALUES(?,?,?,?,?,?,?,?)",(
                        self.owner_id.get(),
                        self.name.get(),
                        self.PhoneNo.get(),
                        self.AadharNo.get(),
                        self.Address.get(),
                        self.city.get(),
                        self.state.get(),
                        self.pincode.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Owner added successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #update
    def update(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.owner_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.AadharNo.get()==""):
                messagebox.showerror("ERROR", "Owner ID, Name, Phone No., Aadhaar No. is required", parent = self.root)
    
            else:
                print(self.owner_id.get())
                connection_cursor.execute("SELECT * FROM OWNER WHERE owner_id=?",(self.owner_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid Owner ID", parent = self.root)
                else:
                    connection_cursor.execute("UPDATE OWNER SET name = ?, phone_no = ?, aadhaar_no = ?, address = ?, city = ?, state = ?, pincode = ? WHERE owner_id = ?",(
                        self.name.get(),
                        self.PhoneNo.get(),
                        self.AadharNo.get(),
                        self.Address.get(),
                        self.city.get(),
                        self.state.get(),
                        self.pincode.get(),
                        self.owner_id.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Owner updated successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #delete
    def delete(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.owner_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.AadharNo.get()==""):
                messagebox.showerror("ERROR", "Owner ID, Name, Phone No., Aadhaar No. is required", parent = self.root)
    
            else:
                print(self.owner_id.get())
                connection_cursor.execute("SELECT * FROM OWNER WHERE owner_id=?",(self.owner_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid Owner ID", parent = self.root)
                else:
                    permission = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if permission == YES:
                        connection_cursor.execute("DELETE FROM OWNER WHERE owner_id = ?", (self.owner_id.get()))
                        connection.commit()
                        messagebox.showinfo("Delete", "Owner deleted successfully", parent = self.root)
                        self.clear()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #clear
    def clear(self):
        self.owner_id.set(""),
        self.name.set(""),
        self.PhoneNo.set(""),
        self.AadharNo.set(""),
        self.Address.set(""),
        self.city.set(""),
        self.state.set(""),
        self.pincode.set(""),
        self.searchBY.set("Select"),
        self.searchtext.set("")
        self.show_data()

    def get_data(self, ev):
        focused_tuple = self.OwnerTable.focus()
        content_tuple = self.OwnerTable.item(focused_tuple)
        row = content_tuple['values']
        print(row)
        self.owner_id.set(row[0]),
        self.name.set(row[1]),
        self.PhoneNo.set(row[2]),
        self.AadharNo.set(row[3]),
        self.Address.set(row[4]),
        self.city.set(row[5]),
        self.state.set(row[6]),
        self.pincode.set(row[7])

    def show_data(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            connection_cursor.execute("Select * FROM OWNER")
            rows = connection_cursor.fetchall()

            self.OwnerTable.delete(*self.OwnerTable.get_children())
            for row in rows:
                self.OwnerTable.insert('', END, values = row)
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
                connection_cursor.execute("SELECT * FROM OWNER WHERE "+self.searchBY.get()+" LIKE '%" + self.searchtext.get()+ "%'")
                rows = connection_cursor.fetchall()
                if(len(rows)!=0):
                    self.OwnerTable.delete(*self.OwnerTable.get_children())
                    for row in rows:
                        self.OwnerTable.insert("",END, values = row)
                else:
                    messagebox.showerror("Error", "No record found!")
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")



if __name__ == "__main__":
    root = Tk()
    obj = ownerClass(root)
    root.mainloop()

