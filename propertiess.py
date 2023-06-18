from tkinter import *
#import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox

class propertyClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("933x720+347+0")
        self.root.title("PROPERTY")
        self.root.config(bg = "white")
        self.root.focus_force()

         # all variables
        self.property_id = StringVar()
        self.owner_id = StringVar()
        self.bhk = StringVar()
        self.washrooms = StringVar()
        self.status = StringVar()
        self.Address = StringVar()
        self.city = StringVar()
        self.state = StringVar()
        self.pincode = StringVar()
        self.other_details = StringVar()
        self.searchBY = StringVar()
        self.searchtext = StringVar()
        self.owner_id_list = []
        self.owner_search()


        style = ttk.Style();
        style.theme_use("clam")

        # search frame
        SearchFrame = LabelFrame(self.root, bg = "#CAD4FF", borderwidth=1)
        SearchFrame.place(x=60, y=600,width=824, height=65)
        # search through options 
        cmb_search = ttk.Combobox(SearchFrame,textvariable = self.searchBY , values = ("Select","property_id","owner_id","bhk","status"), state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "white")
        cmb_search.place(x=22, y = 18,width=172, height = 35)
        cmb_search.current(0)

        # text search
        txt_search = Entry(SearchFrame,textvariable = self.searchtext, font = ("Times New Roman", 17), bg = "white", relief = "solid", borderwidth=1, foreground="black")
        txt_search.place(x=254, y=18, height=35, width=345)

        # search button
        search_button = Button(SearchFrame, text="Search",command=self.search, font = ("Times New Roman", 17, "bold"), bg = "white", borderwidth=1, cursor= "hand2")
        search_button.place(x=645, y = 18, height = 35, width = 142)

         # content
        label_property_id = Label(self.root, text = "Propery_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=300)
        label_owner_id = Label(self.root, text = "Owner_ID:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=340)
        label_bhk = Label(self.root, text = "BHK:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=380)
        label_washrooms = Label(self.root, text = "Washrooms:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=420)
        label_status = Label(self.root, text = "Status:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=460)
        label_address = Label(self.root, text = "Address:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=500)
        label_city = Label(self.root, text = "City:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=92,y=540)
        label_state = Label(self.root, text = "State:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=300)
        label_pincode = Label(self.root, text = "Pincode:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=340)
        label_other_detail = Label(self.root, text = "Other_Details:", font = ("Times New Roman", 17), background="white", foreground="black").place(x=492,y=380)

        # entry
        entry_property_id = Entry(self.root, textvariable= self.property_id, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=235,y=300, width = 180, height = 30)
        dropdown_owner_id = ttk.Combobox(self.root,textvariable=self.owner_id, values = self.owner_id_list, state="readonly", justify=CENTER, font = ("Times New Roman", 17), background= "#CAD4FF", foreground="black")
        dropdown_owner_id.place(x=235,y=340, width = 180, height = 30)
        entry_bhk = Entry(self.root, textvariable=self.bhk, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=235,y=380, width = 180, height = 30)
        entry_washrooms = Entry(self.root, textvariable=self.washrooms, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=235,y=420, width = 180, height = 30)
        entry_status = Entry(self.root, textvariable=self.status, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=235,y=460, width = 180, height = 30)
        entry_address = Entry(self.root, textvariable=self.Address, font = ("Times New Roman", 17), bg = "#CAD4FF",relief = "solid", borderwidth=1, foreground="black").place(x=235,y=500, width = 180, height = 30)
        entry_city = Entry(self.root, textvariable=self.city, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=235,y=540, width = 180, height = 30)
        entry_state = Entry(self.root, textvariable=self.state, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=300, width = 180, height = 30)
        entry_pincode = Entry(self.root, textvariable=self.pincode, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=340, width = 180, height = 30)
        entry_other_details = Entry(self.root, textvariable=self.other_details, font = ("Times New Roman", 17), bg = "#CAD4FF", relief = "solid", borderwidth=1, foreground="black").place(x=635,y=380, width = 180, height = 30)

         # buttons
        button_save = Button(self.root, text="Save",command=self.insert, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=492, y = 460, height = 35, width = 142)
        button_update = Button(self.root, text="Update",command=self.update, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=492, y = 510, height = 35, width = 142)
        button_delete = Button(self.root, text="Delete",command=self.delete, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=692, y = 460, height = 35, width = 142)
        button_clear = Button(self.root, text="Clear",command=self.clear, font = ("Times New Roman", 17, "bold"), bg = "#CAD4FF", borderwidth=1, cursor= "hand2").place(x=692, y = 510, height = 35, width = 142)


        # preview of database
        self.property_data_Frame = Frame(self.root)
        self.property_data_Frame.place(x=30, y = 200, width = 1220)
        self.property_data_Frame.pack()
        scroll_y = Scrollbar(self.property_data_Frame, orient=VERTICAL)
        scroll_x = Scrollbar(self.property_data_Frame, orient=HORIZONTAL)
        self.propertyTable = ttk.Treeview(self.property_data_Frame, columns = ("property_id", "owner_id", "bhk", "washrooms", "status", "address", "city", "state", "pincode","other_details"))

        scroll_x.pack(side=BOTTOM,fill = "x" )
        scroll_y.pack(side=RIGHT, fill = "y")
        scroll_x.config(command=self.propertyTable.xview)
        scroll_x.config(command=self.propertyTable.yview)

        self.propertyTable.heading("property_id", text = "property_id")
        self.propertyTable.heading("owner_id", text = "owner_id")
        self.propertyTable.heading("bhk", text = "BHK")
        self.propertyTable.heading("washrooms", text = "Washrooms")
        self.propertyTable.heading("status", text = "Status")
        self.propertyTable.heading("address", text = "Address")
        self.propertyTable.heading("city", text = "City")
        self.propertyTable.heading("state", text = "State")
        self.propertyTable.heading("pincode", text = "Pincode")
        self.propertyTable.heading("other_details", text = "other_details")

        self.propertyTable["show"] = "headings"

        self.propertyTable.column("property_id", width=50)
        self.propertyTable.column("owner_id", width=50)
        self.propertyTable.column("bhk", width=50)
        self.propertyTable.column("washrooms", width=80)
        self.propertyTable.column("status", width=100)
        self.propertyTable.column("address", width=300)
        self.propertyTable.column("city", width=100)
        self.propertyTable.column("state", width=110)
        self.propertyTable.column("pincode", width=100)
        self.propertyTable.column("other_details", width=500)

        self.propertyTable.pack(fill = BOTH, expand= TRUE)
        self.propertyTable.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        #event
        self.propertyTable.bind("<ButtonRelease-1>", self.get_data)

        self.show_data()

    # functions related to databases to 
    #save
    def insert(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.property_id.get() == "" or self.owner_id.get() == "" or self.bhk.get() == "" or self.status.get()==""):
                messagebox.showerror("ERROR", "Property ID,Owner ID, BHK, Washrooms, Status is required", parent = self.root)
    
            else:
                print(self.property_id.get())
                connection_cursor.execute("SELECT * FROM PROPERTY WHERE property_id=?",(self.property_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "This Property ID is already assigned, try different ID", parent = self.root)
                else:

                    connection_cursor.execute("INSERT INTO PROPERTY (property_id, owner_id, bhk, washrooms, status, Address, city, state, pincode, other_details) VALUES(?,?,?,?,?,?,?,?,?,?)",(
                        self.property_id.get(),
                        self.owner_id.get(),
                        self.bhk.get(),
                        self.washrooms.get(),
                        self.status.get(),
                        self.Address.get(),
                        self.city.get(),
                        self.state.get(),
                        self.pincode.get(),
                        self.other_details.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Property added successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #update
    def update(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.property_id.get() == "" or self.owner_id.get() == "" or self.bhk.get() == "" or self.status.get()==""):
                messagebox.showerror("ERROR", "Property ID, Owner ID, BHK, Washrooms, Status is required", parent = self.root)
    
            else:
                print(self.property_id.get())
                connection_cursor.execute("SELECT * FROM PROPERTY WHERE property_id=?",(self.property_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid Property ID", parent = self.root)
                else:
                    connection_cursor.execute("UPDATE PROPERTY SET owner_id = ?, bhk = ?, washrooms = ?, status = ?, address = ?, city = ?, state = ?, pincode = ?, other_details = ? WHERE property_id = ?",(
                        self.owner_id.get(),
                        self.bhk.get(),
                        self.washrooms.get(),
                        self.status.get(),
                        self.Address.get(),
                        self.city.get(),
                        self.state.get(),
                        self.pincode.get(),
                        self.other_details.get(),
                        self.property_id.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Property updated successfully", parent = self.root)
                    self.show_data()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")        

    #delete
    def delete(self): 
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            if (self.property_id.get() == "" or self.owner_id.get() == "" or self.bhk.get() == "" or self.status.get()==""):
                messagebox.showerror("ERROR", "Property ID, Owner ID, BHK, Washrooms, Status is required", parent = self.root)
    
            else:
                print(self.property_id.get())
                connection_cursor.execute("SELECT * FROM PROPERTY WHERE property_id=?",(self.property_id.get()),)
                row = connection_cursor.fetchone()
                print(row)
                if (row==NONE):
                    messagebox.showerror("Error", "Invalid Property ID", parent = self.root)
                else:
                    permission = messagebox.askyesno("Confirm", "Do you really want to delete?", parent = self.root)
                    if permission == YES:
                        connection_cursor.execute("DELETE FROM PROPERTY WHERE property_id = ?", (self.property_id.get()))
                        connection.commit()
                        messagebox.showinfo("Delete", "Property deleted successfully", parent = self.root)
                        self.clear()
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")

    #clear
    def clear(self):
        self.property_id.set("")
        self.owner_id.set(""),
        self.bhk.set(""),
        self.washrooms.set(""),
        self.status.set(""),
        self.Address.set(""),
        self.city.set(""),
        self.state.set(""),
        self.pincode.set(""),
        self.other_details.set(""),
        self.searchBY.set("Select"),
        self.searchtext.set("")
        self.show_data()

    def get_data(self, ev):
        focused_tuple = self.propertyTable.focus()
        content_tuple = self.propertyTable.item(focused_tuple)
        row = content_tuple['values']
        print(row)
        self.property_id.set(row[0]),
        self.owner_id.set(row[1]),
        self.bhk.set(row[2]),
        self.washrooms.set(row[3]),
        self.status.set(row[4]),
        self.Address.set(row[5]),
        self.city.set(row[6]),
        self.state.set(row[7]),
        self.pincode.set(row[8]),
        self.other_details.set(row[9]),
        

    def show_data(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()

        try:
            connection_cursor.execute("Select * FROM PROPERTY")
            rows = connection_cursor.fetchall()

            self.propertyTable.delete(*self.propertyTable.get_children())
            for row in rows:
                self.propertyTable.insert('', END, values = row)
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
                connection_cursor.execute("SELECT * FROM PROPERTY WHERE "+self.searchBY.get()+" LIKE '%" + self.searchtext.get()+ "%'")
                rows = connection_cursor.fetchall()
                if(len(rows)!=0):
                    self.propertyTable.delete(*self.propertyTable.get_children())
                    for row in rows:
                        self.propertyTable.insert("",END, values = row)
                else:
                    messagebox.showerror("Error", "No record found!")
        except Exception as exc:
            messagebox.showerror("Error", f"Error due to: {str(exc)}")    

    # owner - dropdown utility function
    def owner_search(self):
        connection = sqlite3.connect("Property_Management.db")
        connection_cursor = connection.cursor()
        connection_cursor.execute("SELECT owner_id FROM OWNER")
        rows = connection_cursor.fetchall()
        print(rows)
        for row in rows:
            self.owner_id_list.append(row[0])
        self.owner_id_list.sort()
        print(self.owner_id_list)

if __name__ == "__main__":
    root = Tk()
    obj = propertyClass(root)
    root.mainloop()
