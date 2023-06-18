from tkinter import *
#import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox

class requestClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("933x720+347+0")
        self.root.title("MAINTENANCE_REQUEST")
        self.root.config(bg = "white")
        self.root.focus_force()

        # all variables
        self.request_id = StringVar()
        self.vendor_id = StringVar()
        self.property_id = StringVar()
        self.tenant_id = StringVar()
        self.description = StringVar()
        self.status = StringVar()
        self.required_date = StringVar()
        self.amount = StringVar()
        self.payment_status = StringVar()
        self.searchBY = StringVar()
        self.searchtext = StringVar()

        self.vendor_id_list = []
        self.property_id_list = []
        self.tenant_id_list = []
        self.dropdown_values()

        style = ttk.Style();
        style.theme_use("clam")

        # search frame
        SearchFrame = LabelFrame(self.root, bg = "#CAD4FF", borderwidth=1)
        SearchFrame.place(x=60, y=600,width=824, height=65)
        # search through options 
        cmb_search = ttk.Combobox(SearchFrame,textvariable = self.searchBY , values = ("Select","request_id","property_id","vendor_id","tenant_id","rent_amount"), state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "white")
        cmb_search.place(x=22, y = 18,width=172, height = 35)
        cmb_search.current(0)

        # text search
        txt_search = Entry(SearchFrame,textvariable = self.searchtext, font = ("Times New Roman", 17), bg = "white", relief = "solid", borderwidth=1, foreground="black")
        txt_search.place(x=254, y=18, height=35, width=345)

        # search button
        search_button = Button(SearchFrame, text="Search",command=self.search, font = ("Times New Roman", 17, "bold"), bg = "white", borderwidth=1, cursor= "hand2")
        search_button.place(x=645, y = 18, height = 35, width = 142)

        # content
        label_request_id = Label(self.root, text = "request_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=82,y=300)
        label_vendor_id = Label(self.root, text = "Vendor_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=82,y=340)
        label_property_id = Label(self.root, text = "Property_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=82,y=380)
        label_tenant_id = Label(self.root, text = "Tenant_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=82,y=420)
        label_description = Label(self.root, text = "Description:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=82,y=460)
        label_status = Label(self.root, text = "Status:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=82,y=500)
        label_required_date = Label(self.root, text = "Required_Date:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=82,y=540)
        label_amount = Label(self.root, text = "Amount:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=300)
        label_payment_status = Label(self.root, text = "Payment\nstatus:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=340)
       
        # entry
        entry_request_id = Entry(self.root, textvariable= self.request_id, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=235,y=300, width = 180, height = 30)
        dropdown_vendor_id = ttk.Combobox(self.root,textvariable=self.vendor_id, values = self.vendor_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_vendor_id.place(x=235,y=340, width = 180, height = 30)
        dropdown_property_id = ttk.Combobox(self.root,textvariable=self.property_id, values = self.property_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_property_id.place(x=235,y=380, width = 180, height = 30)
        dropdown_tenant_id = ttk.Combobox(self.root,textvariable=self.tenant_id, values = self.tenant_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_tenant_id.place(x=235,y=420, width = 180, height = 30)
        entry_description = Entry(self.root, textvariable=self.description, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=235,y=460, width = 180, height = 30)
        entry_status = Entry(self.root, textvariable=self.status, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=235,y=500, width = 180, height = 30)
        entry_required_date = Entry(self.root, textvariable=self.required_date, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=235,y=540, width = 180, height = 30)
        entry_amount = Entry(self.root, textvariable=self.amount, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=300, width = 180, height = 30)
        entry_payment_status = Entry(self.root, textvariable=self.payment_status, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=340, width = 180, height = 30)

        # buttons
        button_save = Button(self.root, text="Save",command=self.insert, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=492, y = 440, height = 35, width = 142)
        button_update = Button(self.root, text="Update",command=self.update, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=492, y = 510, height = 35, width = 142)
        button_delete = Button(self.root, text="Delete",command=self.delete, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=692, y = 440, height = 35, width = 142)
        button_clear = Button(self.root, text="Clear",command=self.clear, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=692, y = 510, height = 35, width = 142)

# preview of database
        self.request_data_Frame = Frame(self.root)
        self.request_data_Frame.place(x=30, y = 200, width = 1220)
        self.request_data_Frame.pack()
        scroll_y = Scrollbar(self.request_data_Frame, orient=VERTICAL)
        scroll_x = Scrollbar(self.request_data_Frame, orient=HORIZONTAL)
        self.requestTable = ttk.Treeview(self.request_data_Frame, columns = ("request_id", "vendor_id", "property_id", "tenant_id", "description", "status", "required_date", "amount", "payment_status"))

        scroll_x.pack(side=BOTTOM,fill = "x" )
        scroll_y.pack(side=RIGHT, fill = "y")
        scroll_x.config(command=self.requestTable.xview)
        scroll_x.config(command=self.requestTable.yview)

        self.requestTable.heading("request_id", text = "request_id")
        self.requestTable.heading("vendor_id", text = "vendor_id")
        self.requestTable.heading("property_id", text = "property_id")
        self.requestTable.heading("tenant_id", text = "tenant_id")
        self.requestTable.heading("description", text = "description")
        self.requestTable.heading("status", text = "status")
        self.requestTable.heading("required_date", text = "required_date")
        self.requestTable.heading("amount", text = "amount")
        self.requestTable.heading("payment_status", text = "payment_status")

        self.requestTable["show"] = "headings"

        self.requestTable.column("request_id", width=100)
        self.requestTable.column("vendor_id", width=100)
        self.requestTable.column("property_id", width=100)
        self.requestTable.column("tenant_id", width=100)
        self.requestTable.column("description", width=100)
        self.requestTable.column("status", width=100)
        self.requestTable.column("required_date", width=100)
        self.requestTable.column("amount", width=100)
        self.requestTable.column("payment_status", width=100)

        self.requestTable.pack(fill = BOTH, expand= TRUE)
        self.requestTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        #event
        self.requestTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

# functions related to databases to 
    #save
    def insert(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.request_id.get() == "" or self.vendor_id.get() == "" or self.property_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "request_id, vendor_id, property_id, tenant_id , amount is required", parent = self.root)
    
            else:
                print(self.request_id.get())
                connection_cursor.execute("SELECT * FROM request WHERE request_id=?",(self.request_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "This request ID is already assigned, try different ID", parent = self.root)
                else:

                    connection_cursor.execute("INSERT INTO request (request_id, vendor_id, property_id, tenant_id, description, status, required_date, amount, payment_status) VALUES(?,?,?,?,?,?,?,?,?)",(
                        self.request_id.get(),
                        self.vendor_id.get(),
                        self.property_id.get(),
                        self.tenant_id.get(),
                        self.description.get(),
                        self.status.get(),
                        self.required_date.get(),
                        self.amount.get(),
                        self.payment_status.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "request added successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #update
    def update(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.request_id.get() == "" or self.vendor_id.get() == "" or self.property_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "request ID, vendor ID, Property ID, Tenant ID is required", parent = self.root)
    
            else:
                print(self.request_id.get())
                connection_cursor.execute("SELECT * FROM request WHERE request_id=?",(self.request_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid request ID", parent = self.root)
                else:
                    connection_cursor.execute("UPDATE request SET vendor_id = ?, property_id = ?, tenant_id = ?, description = ?, status = ?, required_date = ?, amount = ?, payment_status = ? WHERE request_id = ?",(
                        self.vendor_id.get(),
                        self.property_id.get(),
                        self.tenant_id.get(),
                        self.description.get(),
                        self.status.get(),
                        self.required_date.get(),
                        self.amount.get(),
                        self.payment_status.get(),
                        self.request_id.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "request updated successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")        

    #delete
    def delete(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.request_id.get() == "" or self.vendor_id.get() == "" or self.property_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "request ID, vendor ID, Property ID, Tenant ID is required", parent = self.root)
    
            else:
                print(self.request_id.get())
                connection_cursor.execute("SELECT * FROM request WHERE request_id=?",(self.request_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid request ID", parent = self.root)
                else:
                    permission = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if permission == YES:
                        connection_cursor.execute("DELETE FROM request WHERE request_id = ?", (self.request_id.get()))
                        connection.commit()
                        messagebox.showinfo("Delete", "request deleted successfully", parent = self.root)
                        self.clear()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #clear
    def clear(self):
        self.request_id.set(""),
        self.vendor_id.set(""),
        self.property_id.set(""),
        self.tenant_id.set(""),
        self.description.set(""),
        self.status.set(""),
        self.required_date.set(""),
        self.amount.set(""),
        self.payment_status.set(""),
        self.searchBY.set("Select"),
        self.searchtext.set("")
        self.show_data()

    def get_data(self, ev):
        focused_tuple = self.requestTable.focus()
        content_tuple = self.requestTable.item(focused_tuple)
        row = content_tuple['values']
        print(row)
        self.request_id.set(row[0]),
        self.vendor_id.set(row[1]),
        self.property_id.set(row[2]),
        self.tenant_id.set(row[3]),
        self.description.set(row[4]),
        self.status.set(row[5]),
        self.required_date.set(row[6]),
        self.amount.set(row[7]),
        self.payment_status.set(row[8])

        

    def show_data(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            connection_cursor.execute("Select * FROM request")
            rows = connection_cursor.fetchall()

            self.requestTable.delete(*self.requestTable.get_children())
            for row in rows:
                self.requestTable.insert('', END, values = row)
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
                connection_cursor.execute("SELECT * FROM request WHERE "+self.searchBY.get()+" LIKE '%" + self.searchtext.get()+ "%'")
                rows = connection_cursor.fetchall()
                if(len(rows)!=0):
                    self.requestTable.delete(*self.requestTable.get_children())
                    for row in rows:
                        self.requestTable.insert("",END, values = row)
                else:
                    messagebox.showerror("Error", "No record found!")
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}") 

    def dropdown_values(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        connection_cursor.execute("SELECT vendor_id FROM VENDOR")
        connection.commit()
        vendors = connection_cursor.fetchall()
        print(vendors)
        for vendor in vendors:
            self.vendor_id_list.append(vendor[0])
        self.vendor_id_list.sort()

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

if __name__ == "__main__":
    root = Tk()
    obj = requestClass(root)
    root.mainloop()