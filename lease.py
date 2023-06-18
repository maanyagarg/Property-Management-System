from tkinter import *
#import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox

class leaseClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("933x720+347+0")
        self.root.title("LEASE")
        self.root.config(bg = "white")
        self.root.focus_force()

         # all variables
        self.lease_id = StringVar()
        self.owner_id = StringVar()
        self.property_id = StringVar()
        self.tenant_id = StringVar()
        self.start_date = StringVar()
        self.end_date = StringVar()
        self.security = StringVar()
        self.lease_amount = StringVar()
        self.rent_amount = StringVar()
        self.due_date = StringVar()
        self.searchBY = StringVar()
        self.searchtext = StringVar()

        self.owner_id_list = []
        self.property_id_list = []
        self.tenant_id_list = []
        self.dropdown_values()
        self.prop()
        style = ttk.Style();
        style.theme_use("clam")

        # search frame
        SearchFrame = LabelFrame(self.root, bg = "#CAD4FF", borderwidth=1)
        SearchFrame.place(x=60, y=600,width=824, height=65)
        # search through options 
        cmb_search = ttk.Combobox(SearchFrame,textvariable = self.searchBY , values = ("Select","lease_id","property_id","owner_id","tenant_id","rent_amount"), state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "white")
        cmb_search.place(x=22, y = 18,width=172, height = 35)
        cmb_search.current(0)

        # text search
        txt_search = Entry(SearchFrame,textvariable = self.searchtext, font = ("Times New Roman", 17), bg = "white", relief = "solid", borderwidth=1, foreground="black")
        txt_search.place(x=254, y=18, height=35, width=345)

        # search button
        search_button = Button(SearchFrame, text="Search",command=self.search, font = ("Times New Roman", 17, "bold"), bg = "white", borderwidth=1, cursor= "hand2")
        search_button.place(x=645, y = 18, height = 35, width = 142)

        # content
        label_lease_id = Label(self.root, text = "Lease_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=300)
        label_owner_id = Label(self.root, text = "Owner_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=340)
        label_property_id = Label(self.root, text = "Property_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=380)
        label_tenant_id = Label(self.root, text = "Tenant_id:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=420)
        label_start_date = Label(self.root, text = "Start_date:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=460)
        label_end_date = Label(self.root, text = "End_date:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=500)
        label_security = Label(self.root, text = "Security:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=540)
        label_lease_amount = Label(self.root, text = "Lease_amount", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=300)
        label_rent_amount = Label(self.root, text = "Rent_amount:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=340)
        label_due_date = Label(self.root, text = "Due_date:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=380)

        # entry
        entry_lease_id = Entry(self.root, textvariable= self.lease_id, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=235,y=300, width = 180, height = 30)
        dropdown_owner_id = ttk.Combobox(self.root,textvariable=self.owner_id, values = self.owner_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_owner_id.place(x=235,y=340, width = 180, height = 30)
        self.prop()
        dropdown_property_id = ttk.Combobox(self.root,textvariable=self.property_id, values = self.property_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_property_id.place(x=235,y=380, width = 180, height = 30)
        dropdown_tenant_id = ttk.Combobox(self.root,textvariable=self.tenant_id, values = self.tenant_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_tenant_id.place(x=235,y=420, width = 180, height = 30)
        entry_start_date = Entry(self.root, textvariable=self.start_date, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=235,y=460, width = 180, height = 30)
        entry_end_date = Entry(self.root, textvariable=self.end_date, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=235,y=500, width = 180, height = 30)
        entry_security = Entry(self.root, textvariable=self.security, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=235,y=540, width = 180, height = 30)
        entry_lease_amount = Entry(self.root, textvariable=self.lease_amount, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=300, width = 180, height = 30)
        entry_rent_amount = Entry(self.root, textvariable=self.rent_amount, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=340, width = 180, height = 30)
        entry_due_date = Entry(self.root, textvariable=self.due_date, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=380, width = 180, height = 30)

         # buttons
        button_save = Button(self.root, text="Save",command=self.insert, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=492, y = 460, height = 35, width = 142)
        button_update = Button(self.root, text="Update",command=self.update, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=492, y = 510, height = 35, width = 142)
        button_delete = Button(self.root, text="Delete",command=self.delete, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=692, y = 460, height = 35, width = 142)
        button_clear = Button(self.root, text="Clear",command=self.clear, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=692, y = 510, height = 35, width = 142)

# preview of database
        self.lease_data_Frame = Frame(self.root)
        self.lease_data_Frame.place(x=30, y = 200, width = 1220)
        self.lease_data_Frame.pack()
        scroll_y = Scrollbar(self.lease_data_Frame, orient=VERTICAL)
        scroll_x = Scrollbar(self.lease_data_Frame, orient=HORIZONTAL)
        self.leaseTable = ttk.Treeview(self.lease_data_Frame, columns = ("lease_id", "owner_id", "property_id", "tenant_id", "start_date", "end_date", "security", "lease_amount", "rent_amount", "due_date"))

        scroll_x.pack(side=BOTTOM,fill = "x" )
        scroll_y.pack(side=RIGHT, fill = "y")
        scroll_x.config(command=self.leaseTable.xview)
        scroll_x.config(command=self.leaseTable.yview)

        self.leaseTable.heading("lease_id", text = "lease_id")
        self.leaseTable.heading("owner_id", text = "owner_id")
        self.leaseTable.heading("property_id", text = "property_id")
        self.leaseTable.heading("tenant_id", text = "tenant_id")
        self.leaseTable.heading("start_date", text = "start_date")
        self.leaseTable.heading("end_date", text = "end_date")
        self.leaseTable.heading("security", text = "security")
        self.leaseTable.heading("lease_amount", text = "lease_amount")
        self.leaseTable.heading("rent_amount", text = "rent_amount")
        self.leaseTable.heading("due_date", text = "due_date")

        self.leaseTable["show"] = "headings"

        self.leaseTable.column("lease_id", width=80)
        self.leaseTable.column("owner_id", width=80)
        self.leaseTable.column("property_id", width=80)
        self.leaseTable.column("tenant_id", width=80)
        self.leaseTable.column("start_date", width=100)
        self.leaseTable.column("end_date", width=100)
        self.leaseTable.column("security", width=80)
        self.leaseTable.column("lease_amount", width=100)
        self.leaseTable.column("rent_amount", width=100)
        self.leaseTable.column("due_date", width=100)

        self.leaseTable.pack(fill = BOTH, expand= TRUE)
        self.leaseTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        #event
        self.leaseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()



    # functions related to databases to 
    #save
    def insert(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.lease_id.get() == "" or self.owner_id.get() == "" or self.property_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "lease_id, Owner_id, property_id, tenant_id , Security is required", parent = self.root)
    
            else:
                print(self.lease_id.get())
                connection_cursor.execute("SELECT * FROM lease WHERE lease_id=?",(self.lease_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "This lease ID is already assigned, try different ID", parent = self.root)
                else:

                    connection_cursor.execute("INSERT INTO lease (lease_id, owner_id, property_id, tenant_id, start_date, end_date, security, lease_amount, rent_amount, due_date) VALUES(?,?,?,?,?,?,?,?,?,?)",(
                        self.lease_id.get(),
                        self.owner_id.get(),
                        self.property_id.get(),
                        self.tenant_id.get(),
                        self.start_date.get(),
                        self.end_date.get(),
                        self.security.get(),
                        self.lease_amount.get(),
                        self.rent_amount.get(),
                        self.due_date.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "lease added successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #update
    def update(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.lease_id.get() == "" or self.owner_id.get() == "" or self.property_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "Lease ID, Owner ID, Property ID, Tenant ID is required", parent = self.root)
    
            else:
                print(self.lease_id.get())
                connection_cursor.execute("SELECT * FROM lease WHERE lease_id=?",(self.lease_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid lease ID", parent = self.root)
                else:
                    connection_cursor.execute("UPDATE lease SET owner_id = ?, property_id = ?, lease_id = ?, start_date = ?, end_date = ?, security = ?, lease_amount = ?, rent_amount = ?, due_date = ? WHERE lease_id = ?",(
                        self.owner_id.get(),
                        self.property_id.get(),
                        self.tenant_id.get(),
                        self.start_date.get(),
                        self.end_date.get(),
                        self.security.get(),
                        self.lease_amount.get(),
                        self.rent_amount.get(),
                        self.due_date.get(),
                        self.lease_id.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "lease updated successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")        

    #delete
    def delete(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.lease_id.get() == "" or self.owner_id.get() == "" or self.property_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "Lease ID, Owner ID, Property ID, Tenant ID is required", parent = self.root)
    
            else:
                print(self.lease_id.get())
                connection_cursor.execute("SELECT * FROM lease WHERE lease_id=?",(self.lease_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid lease ID", parent = self.root)
                else:
                    permission = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if permission == YES:
                        connection_cursor.execute("DELETE FROM lease WHERE lease_id = ?", (self.lease_id.get()))
                        connection.commit()
                        messagebox.showinfo("Delete", "lease deleted successfully", parent = self.root)
                        self.clear()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #clear
    def clear(self):
        self.lease_id.set(""),
        self.owner_id.set(""),
        self.property_id.set(""),
        self.tenant_id.set(""),
        self.start_date.set(""),
        self.end_date.set(""),
        self.security.set(""),
        self.lease_amount.set(""),
        self.rent_amount.set(""),
        self.due_date.set(""),
        self.searchBY.set("Select"),
        self.searchtext.set("")
        self.show_data()

    def get_data(self, ev):
        focused_tuple = self.leaseTable.focus()
        content_tuple = self.leaseTable.item(focused_tuple)
        row = content_tuple['values']
        print(row)
        self.lease_id.set(row[0]),
        self.owner_id.set(row[1]),
        self.property_id.set(row[2]),
        self.tenant_id.set(row[3]),
        self.start_date.set(row[4]),
        self.end_date.set(row[5]),
        self.security.set(row[6]),
        self.lease_amount.set(row[7]),
        self.rent_amount.set(row[8]),
        self.due_date.set(row[9]),
        

    def show_data(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            connection_cursor.execute("Select * FROM lease")
            rows = connection_cursor.fetchall()

            self.leaseTable.delete(*self.leaseTable.get_children())
            for row in rows:
                self.leaseTable.insert('', END, values = row)
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
                connection_cursor.execute("SELECT * FROM LEASE WHERE "+self.searchBY.get()+" LIKE '%" + self.searchtext.get()+ "%'")
                rows = connection_cursor.fetchall()
                if(len(rows)!=0):
                    self.leaseTable.delete(*self.leaseTable.get_children())
                    for row in rows:
                        self.leaseTable.insert("",END, values = row)
                else:
                    messagebox.showerror("Error", "No record found!")
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}") 


    def dropdown_values(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        connection_cursor.execute("SELECT owner_id FROM OWNER")
        connection.commit()
        owners = connection_cursor.fetchall()
        print(owners)
        for owner in owners:
            self.owner_id_list.append(owner[0])
        self.owner_id_list.sort()

        connection_cursor.execute("SELECT property_id FROM PROPERTY")
        connection.commit()
        properties = connection_cursor.fetchall()
        print(properties)
        for property in properties:
            self.property_id_list.append(property[0])
        self.property_id_list.sort()

        connection_cursor.execute("SELECT tenant_id FROM TENANT")
        connection.commit()
        tenants = connection_cursor.fetchall()
        print(tenants)
        for tenant in tenants:
            self.tenant_id_list.append(tenant[0])
        self.tenant_id_list.sort()

    def prop(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        connection_cursor.execute("SELECT property_id FROM PROPERTY where owner_id = ?", (self.owner_id.get(),))
        connection.commit()
        properties = connection_cursor.fetchall()
        print(properties)
        for property in properties:
            self.property_id_list.append(property[0])
        self.property_id_list.sort()

if __name__ == "__main__":
    root = Tk()
    obj = leaseClass(root)
    root.mainloop()
