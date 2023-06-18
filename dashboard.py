from tkinter import *
from PIL import Image, ImageTk
from ownerrrr import ownerClass
from propertiess import propertyClass
from tenants import tenantClass
from lease import leaseClass
from vendor import vendorClass
from maintenanceRequest import requestClass
from payment import paymentClass
import os

class PMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Property Management System | Developed by Manav and Manya" )
        #self.root.config(bg="white")

        #___title___
        title=Label(self.root,text="Mittal Properties Portal",font=("times new roman",40,"bold")).place(x=520,y=267,width=562,height=66)

        #_____leftmenuu
        leftmenu=Frame(self.root,bd=3,relief=RIDGE,bg="#24293E")
        leftmenu.place(x=0,y=0,width=347,height=721)

        #iconnnnnnn
        #self.icon_title=PhotoImage(file="Pictures\\1.jpeg")
        #title=Label(self.root,image=self.icon_title)
        #my_img = ImageTk.PhotoImage(Image.open("1.jpeg"))
        #my_label = Label(image=my_img)
        #my_label.pack()
        self.menulogo = Image.open("2.jpeg")
        self.menulogo = self.menulogo.resize((347,150),Image.ANTIALIAS)
        self.menulogo = ImageTk.PhotoImage(self.menulogo) 

        lbl_menulogo=Label(leftmenu,image=self.menulogo,bd=0)
        lbl_menulogo.pack(side=TOP,fill=X)

        #menu k columns
        lbl_menu=Label(leftmenu,font=("times new roman",10),bg="#24293E").pack(side=TOP,fill=X)
        btn_owner=Button(leftmenu,text="Owner",command=self.owner,font=("times new roman",20),bg="#788AD4",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_properties=Button(leftmenu,text="Properties",command=self.property,font=("times new roman",20),bg="#788AD4",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_tenants=Button(leftmenu,text="Tenants",command=self.tenant,font=("times new roman",20),bg="#788AD4",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_lease=Button(leftmenu,text="Lease",command=self.lease,font=("times new roman",20),bg="#788AD4",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_vendors=Button(leftmenu,text="Vendors",command=self.vendor,font=("times new roman",20),bg="#788AD4",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_requests=Button(leftmenu,text="Maintenance requests",command=self.request,font=("times new roman",20),bg="#788AD4",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_payment=Button(leftmenu,text="Payment",command=self.payment,font=("times new roman",20),bg="#788AD4",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #time and date
        #self.lbl_clock=Label(self.root,text="DD-MM-YYYY \n HH:MM:SS",font=("times new roman",15),bg="#24293E",fg="#F4F5FC")
        #self.lbl_clock.place(x=100,y=620)

        #logout button--------------
        topmenu=Frame(self.root,bd=0,relief=RIDGE)
        topmenu.place(x=347,y=20,width=933,height=100)

        self.toplogo = Image.open("log.png")
        self.toplogo = self.toplogo.resize((45,33),Image.ANTIALIAS)
        self.toplogo = ImageTk.PhotoImage(self.toplogo) 

        btn_toplogo=Button(topmenu,image=self.toplogo,command=self.logout,bd=0,cursor="hand2",borderwidth=0)
        btn_toplogo.pack(anchor="e",padx=40)


        #title k neeche
        title=Label(self.root,text="Welcome to our property management company, where we are committed to providing exceptional service and\nmaximizing the value of your real estate investments. Let us take care of your properties and ensure your peace of mind.",font=("times new roman",12)).place(x=368,y=330,width=862,height=78)

        #footer
        footer=Label(self.root,text="Contact No.: 83721920192\nEmail Address.: mittalproperties@gmail.com ",font=("times new roman",10),bg="#788AD4",anchor="e",padx=20).place(x=347,y=629,width=933,height=71)
        
        
        #===================end of dashboard========================

    def owner(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ownerClass(self.new_win)

    def property(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=propertyClass(self.new_win)

    def tenant(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=tenantClass(self.new_win)

    def lease(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=leaseClass(self.new_win)

    def vendor(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=vendorClass(self.new_win)

    def request(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=requestClass(self.new_win)

    def payment(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=paymentClass(self.new_win)        

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


root=Tk()
obj=PMS(root)
root.mainloop()