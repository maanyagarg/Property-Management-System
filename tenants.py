from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

class tenantClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("933x720+347+0")
        self.root.title("Tenant")
        self.root.config(bg = "white")
        self.root.focus_force()

        # all variables
        self.tenant_id = StringVar()
        self.name = StringVar()
        self.PhoneNo = StringVar()
        self.AadharNo = StringVar()
        self.email = StringVar()
        self.searchBY = StringVar()
        self.searchtext = StringVar()

        style = ttk.Style();
        style.theme_use("clam")

        # search frame
        SearchFrame = LabelFrame(self.root, bg = "#CAD4FF", borderwidth=1)
        SearchFrame.place(x=60, y=630,width=824, height=65)
        # search through options 
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.searchBY, values = ("Select","tenant_id","name","Phone_No"), state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "white")
        cmb_search.place(x=22, y = 18,width=172, height = 35)
        cmb_search.current(0)

        # text search
        txt_search = Entry(SearchFrame, textvariable=self.searchtext, font = ("Times New Roman", 17), bg = "white", relief = "solid", borderwidth=1, foreground="black")
        txt_search.place(x=254, y=18, height=35, width=345)

        # search button
        search_button = Button(SearchFrame,command=self.search, text="Search", font = ("Times New Roman", 17, "bold"), bg = "white", borderwidth=1, cursor= "hand2")
        search_button.place(x=645, y = 18, height = 35, width = 142)

        # content
        label_tenant_id = Label(self.root, text = "Tenant ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=260)
        label_name = Label(self.root, text = "Name:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=320)
        label_PhoneNo = Label(self.root, text = "Phone No:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=380)
        label_AadharNo = Label(self.root, text = "Aadhar No:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=440)
        label_email = Label(self.root, text = "Email:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=500)
       
        # entry
        entry_tenant_id = Entry(self.root, textvariable=self.tenant_id, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=260, width = 284, height = 30)
        entry_name = Entry(self.root, textvariable=self.name, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=320, width = 284, height = 30)
        entry_PhoneNo = Entry(self.root, textvariable=self.PhoneNo, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=285,y=380, width = 284, height = 30)
        entry_AadharNo = Entry(self.root, textvariable=self.AadharNo, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=285,y=440, width = 284, height = 30)
        entry_email = Entry(self.root, textvariable = self.email, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=500, width = 284, height = 30)
        
        # buttons
        button_save = Button(self.root, text="Save",command=self.insert,font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 275, height = 35, width = 142)
        button_update = Button(self.root, text="Update",command=self.update, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 345, height = 35, width = 142)
        button_delete = Button(self.root, text="Delete",command=self.delete, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 415, height = 35, width = 142)
        button_clear = Button(self.root, text="Clear",command=self.clear, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 485, height = 35, width = 142)

        # preview of database
        self.tenant_data_Frame = Frame(self.root)
        self.tenant_data_Frame.place(x=30, y = 200, width = 1220)
        self.tenant_data_Frame.pack()

        
        self.tenantTable = ttk.Treeview(self.tenant_data_Frame, columns = ("tenant_id", "name", "phone_no", "aadhaar_no", "email"), selectmode=BROWSE)
        
        #scroll-bar
        scroll_y = Scrollbar(self.tenant_data_Frame, orient=VERTICAL, command=self.tenantTable.yview)
        scroll_x = Scrollbar(self.tenant_data_Frame, orient=HORIZONTAL, command=self.tenantTable.xview)
        scroll_x.pack(side=BOTTOM,fill = "x" )
        scroll_y.pack(side=RIGHT, fill = "y")

        self.tenantTable.heading("tenant_id", text = "Tenant ID")
        self.tenantTable.heading("name", text = "Name")
        self.tenantTable.heading("phone_no", text = "Phone_No")
        self.tenantTable.heading("aadhaar_no", text = "Aadhaar_No")
        self.tenantTable.heading("email", text = "Email")
        

        self.tenantTable["show"] = "headings"

        self.tenantTable.column("tenant_id", width=100)
        self.tenantTable.column("name", width=160)
        self.tenantTable.column("phone_no", width=160)
        self.tenantTable.column("aadhaar_no", width=160)
        self.tenantTable.column("email", width=300)
        

        self.tenantTable.pack(fill = BOTH, expand= TRUE)
        self.tenantTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        #event
        self.tenantTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

    # functions related to databases to 
    #save
    def insert(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.tenant_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.AadharNo.get()==""):
                messagebox.showerror("ERROR", "Tenant ID, Name, Phone No., Aadhaar No. is required", parent = self.root)
    
            else:
                print(self.tenant_id.get())
                connection_cursor.execute("SELECT * FROM tenant WHERE tenant_id=?",(self.tenant_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "This tenant ID is already assigned, try different ID", parent = self.root)
                else:

                    connection_cursor.execute("INSERT INTO tenant (tenant_id, name, phone_no, aadhaar_no, email) VALUES(?,?,?,?,?)",(
                        self.tenant_id.get(),
                        self.name.get(),
                        self.PhoneNo.get(),
                        self.AadharNo.get(),
                        self.email.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "tenant added successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #update
    def update(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.tenant_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.AadharNo.get()==""):
                messagebox.showerror("ERROR", "tenant ID, Name, Phone No., Aadhaar No. is required", parent = self.root)
    
            else:
                print(self.tenant_id.get())
                connection_cursor.execute("SELECT * FROM tenant WHERE tenant_id=?",(self.tenant_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid tenant ID", parent = self.root)
                else:
                    connection_cursor.execute("UPDATE tenant SET name = ?, phone_no = ?, aadhaar_no = ?, email = ? WHERE tenant_id = ?",(
                        self.name.get(),
                        self.PhoneNo.get(),
                        self.AadharNo.get(),
                        self.email.get(),
                        self.tenant_id.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "tenant updated successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #delete
    def delete(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.tenant_id.get() == "" or self.name.get() == "" or self.PhoneNo.get() == "" or self.AadharNo.get()==""):
                messagebox.showerror("ERROR", "tenant ID, Name, Phone No., Aadhaar No. is required", parent = self.root)
    
            else:
                print(self.tenant_id.get())
                connection_cursor.execute("SELECT * FROM tenant WHERE tenant_id=?",(self.tenant_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid tenant ID", parent = self.root)
                else:
                    permission = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if permission == YES:
                        connection_cursor.execute("DELETE FROM tenant WHERE tenant_id = ?", (self.tenant_id.get()))
                        connection.commit()
                        messagebox.showinfo("Delete", "tenant deleted successfully", parent = self.root)
                        self.clear()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #clear
    def clear(self):
        self.tenant_id.set(""),
        self.name.set(""),
        self.PhoneNo.set(""),
        self.AadharNo.set(""),
        self.email.set(""),
        self.searchBY.set("Select"),
        self.searchtext.set("")
        self.show_data()

    def get_data(self, ev):
        focused_tuple = self.tenantTable.focus()
        content_tuple = self.tenantTable.item(focused_tuple)
        row = content_tuple['values']
        print(row)
        self.tenant_id.set(row[0]),
        self.name.set(row[1]),
        self.PhoneNo.set(row[2]),
        self.AadharNo.set(row[3]),
        self.email.set(row[4]),

    def show_data(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            connection_cursor.execute("Select * FROM tenant")
            rows = connection_cursor.fetchall()

            self.tenantTable.delete(*self.tenantTable.get_children())
            for row in rows:
                self.tenantTable.insert('', END, values = row)
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
                connection_cursor.execute("SELECT * FROM tenant WHERE "+self.searchBY.get()+" LIKE '%" + self.searchtext.get()+ "%'")
                rows = connection_cursor.fetchall()
                if(len(rows)!=0):
                    self.tenantTable.delete(*self.tenantTable.get_children())
                    for row in rows:
                        self.tenantTable.insert("",END, values = row)
                else:
                    messagebox.showerror("Error", "No record found!")
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

if __name__ == "__main__":
    root = Tk()
    obj = tenantClass(root)
    root.mainloop()

