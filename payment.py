from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

class paymentClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("933x720+347+0")
        self.root.title("Payment")
        self.root.config(bg = "white")
        self.root.focus_force()

        # all variables
        self.payment_id = StringVar()
        self.owner_id = StringVar()
        self.request_id = StringVar()
        self.tenant_id = StringVar()
        self.payment_date = StringVar()
        self.searchBY = StringVar()
        self.searchtext = StringVar()

        self.owner_id_list = []
        self.request_id_list = []
        self.tenant_id_list = []
        self.dropdown_values()

        style = ttk.Style();
        style.theme_use("clam")

        # search frame
        SearchFrame = LabelFrame(self.root, bg = "#CAD4FF", borderwidth=1)
        SearchFrame.place(x=60, y=630,width=824, height=65)
        # search through options 
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.searchBY, values = ("Select","payment_id","owner_id","tenant_id"), state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "white")
        cmb_search.place(x=22, y = 18,width=172, height = 35)
        cmb_search.current(0)

        # text search
        txt_search = Entry(SearchFrame, textvariable=self.searchtext, font = ("Times New Roman", 17), bg = "white", relief = "solid", borderwidth=1, foreground="black")
        txt_search.place(x=254, y=18, height=35, width=345)

        # search button
        search_button = Button(SearchFrame,command=self.search, text="Search", font = ("Times New Roman", 17, "bold"), bg = "white", borderwidth=1, cursor= "hand2")
        search_button.place(x=645, y = 18, height = 35, width = 142)

        # content
        label_payment_id = Label(self.root, text = "Payment ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=260)
        label_owner_id = Label(self.root, text = "Owner ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=320)
        label_request_id = Label(self.root, text = "Request ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=380)
        label_tenant_id = Label(self.root, text = "Tenant ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=440)
        label_payment_date = Label(self.root, text = "Payment Date:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=500)
       
        # entry
        entry_payment_id = Entry(self.root, textvariable=self.payment_id, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=260, width = 284, height = 30)
        dropdown_owner_id = ttk.Combobox(self.root,textvariable=self.owner_id, values = self.owner_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_owner_id.place(x=285,y=320, width = 284, height = 30)
        dropdown_request_id = ttk.Combobox(self.root,textvariable=self.request_id, values = self.request_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_request_id.place(x=285,y=380, width = 284, height = 30)
        dropdown_tenant_id = ttk.Combobox(self.root,textvariable=self.tenant_id, values = self.tenant_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_tenant_id.place(x=285,y=440, width = 284, height = 30)
        entry_payment_date = Entry(self.root, textvariable = self.payment_date, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=285,y=500, width = 284, height = 30)
        
        # buttons
        button_save = Button(self.root, text="Save",command=self.insert,font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 275, height = 35, width = 142)
        button_update = Button(self.root, text="Update",command=self.update, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 345, height = 35, width = 142)
        button_delete = Button(self.root, text="Delete",command=self.delete, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 415, height = 35, width = 142)
        button_clear = Button(self.root, text="Clear",command=self.clear, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=680, y = 485, height = 35, width = 142)

        # preview of database
        self.payment_data_Frame = Frame(self.root)
        self.payment_data_Frame.place(x=30, y = 200, width = 1220)
        self.payment_data_Frame.pack()

        
        self.paymentTable = ttk.Treeview(self.payment_data_Frame, columns = ("payment_id", "owner_id", "request_id", "tenant_id", "payment_date"), selectmode=BROWSE)
        
        #scroll-bar
        scroll_y = Scrollbar(self.payment_data_Frame, orient=VERTICAL, command=self.paymentTable.yview)
        scroll_x = Scrollbar(self.payment_data_Frame, orient=HORIZONTAL, command=self.paymentTable.xview)
        scroll_x.pack(side=BOTTOM,fill = "x" )
        scroll_y.pack(side=RIGHT, fill = "y")

        self.paymentTable.heading("payment_id", text = "Payment ID")
        self.paymentTable.heading("owner_id", text = "Owner ID")
        self.paymentTable.heading("request_id", text = "Request ID")
        self.paymentTable.heading("tenant_id", text = "Tenant ID")
        self.paymentTable.heading("payment_date", text = "Payment Date")
        

        self.paymentTable["show"] = "headings"

        self.paymentTable.column("payment_id", width=165)
        self.paymentTable.column("owner_id",  width=165)
        self.paymentTable.column("request_id", width=165)
        self.paymentTable.column("tenant_id", width=165)
        self.paymentTable.column("payment_date", width=240)


        self.paymentTable.pack(fill = BOTH, expand= TRUE)
        self.paymentTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        #event
        self.paymentTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

        # functions related to databases to 
    #save
    def insert(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.payment_id.get() == "" or self.owner_id.get() == "" or self.request_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "Payment ID, Owner ID, Request ID, Tenant ID is required", parent = self.root)
    
            else:
                print(self.payment_id.get())
                connection_cursor.execute("SELECT * FROM payment WHERE payment_id=?",(self.payment_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "This payment ID is already assigned, try different ID", parent = self.root)
                else:

                    connection_cursor.execute("INSERT INTO payment (payment_id, owner_id, request_id, tenant_id, payment_date) VALUES(?,?,?,?,?)",(
                        self.payment_id.get(),
                        self.owner_id.get(),
                        self.request_id.get(),
                        self.tenant_id.get(),
                        self.payment_date.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "payment added successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #update
    def update(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.payment_id.get() == "" or self.owner_id.get() == "" or self.request_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "Payment ID, Owner ID, Request ID, Tenant ID is required", parent = self.root)
    
            else:
                print(self.payment_id.get())
                connection_cursor.execute("SELECT * FROM payment WHERE payment_id=?",(self.payment_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid payment ID", parent = self.root)
                else:
                    connection_cursor.execute("UPDATE payment SET owner_id = ?, request_id = ?, tenant_id = ?, payment_date = ? WHERE payment_id = ?",(
                        self.owner_id.get(),
                        self.request_id.get(),
                        self.tenant_id.get(),
                        self.payment_date.get(),
                        self.payment_id.get()                    
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "payment updated successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #delete
    def delete(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.payment_id.get() == "" or self.owner_id.get() == "" or self.request_id.get() == "" or self.tenant_id.get()==""):
                messagebox.showerror("ERROR", "Payment ID, Owner ID, Request ID, Tenant ID is required", parent = self.root)
    
            else:
                print(self.payment_id.get())
                connection_cursor.execute("SELECT * FROM payment WHERE payment_id=?",(self.payment_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid payment ID", parent = self.root)
                else:
                    permission = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if permission == YES:
                        connection_cursor.execute("DELETE FROM payment WHERE payment_id = ?", (self.payment_id.get()))
                        connection.commit()
                        messagebox.showinfo("Delete", "payment deleted successfully", parent = self.root)
                        self.clear()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #clear
    def clear(self):
        self.payment_id.set(""),
        self.owner_id.set(""),
        self.request_id.set(""),
        self.tenant_id.set(""),
        self.payment_date.set(""),
        self.searchBY.set("Select"),
        self.searchtext.set("")
        self.show_data()

    def get_data(self, ev):
        focused_tuple = self.paymentTable.focus()
        content_tuple = self.paymentTable.item(focused_tuple)
        row = content_tuple['values']
        print(row)
        self.payment_id.set(row[0]),
        self.owner_id.set(row[1]),
        self.request_id.set(row[2]),
        self.tenant_id.set(row[3]),
        self.payment_date.set(row[4]),

    def show_data(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            connection_cursor.execute("Select * FROM payment")
            rows = connection_cursor.fetchall()

            self.paymentTable.delete(*self.paymentTable.get_children())
            for row in rows:
                self.paymentTable.insert('', END, values = row)
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
                connection_cursor.execute("SELECT * FROM payment WHERE "+self.searchBY.get()+" LIKE '%" + self.searchtext.get()+ "%'")
                rows = connection_cursor.fetchall()
                if(len(rows)!=0):
                    self.paymentTable.delete(*self.paymentTable.get_children())
                    for row in rows:
                        self.paymentTable.insert("",END, values = row)
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

        connection_cursor.execute("SELECT tenant_id FROM TENANT")
        connection.commit()
        tenants = connection_cursor.fetchall()
        print(tenants)
        for tenant in tenants:
            self.tenant_id_list.append(tenant[0])
        self.tenant_id_list.sort()

        connection_cursor.execute("SELECT request_id FROM REQUEST")
        connection.commit()
        requests = connection_cursor.fetchall()
        print(requests)
        for request in requests:
            self.request_id_list.append(request[0])
        self.request_id_list.sort()

if __name__ == "__main__":
    root = Tk()
    obj = paymentClass(root)
    root.mainloop()