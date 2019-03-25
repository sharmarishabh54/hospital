from tkinter import *
import tkinter.messagebox
import sqlite3


conn = sqlite3.connect('database1.db')
c = conn.cursor()

class application:
    def __init__(self,master):
        self.master = master

        # heading label
        self.heading = Label(master, text="Update Appointments",fg='darkslategray',font='times 40',bg='darkseagreen')
        self.heading.place(x=350,y=30)

       # search criteria

        self.name=Label(master,text=" ENTER PATIENT'S NAME",font='times 18',bg='darkseagreen')
        self.name.place(x=10,y=150)

        #entry for name
        self.name_ent = Entry(master,width=50)
        self.name_ent.place(x=340,y=155)
        # search button
        self.search = Button(master,text="Search",font='times 13',width=12,height=1,bg='lightblue',command=self.search_db)
        self.search.place(x=340,y=200)


    def search_db(self):
        self.input = self.name_ent.get()
        # execute sql

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res=c.execute(sql,(self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age=self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.phone = self.row[5]
            self.time = self.row[6]
            
        # update form
        self.uname = Label(self.master,text="Patient's Name",font='times 18',bg='darkseagreen')
        self.uname.place(x=10,y=250)
        
        self.uage = Label(self.master,text="Age",font='times 18',bg='darkseagreen')
        self.uage.place(x=10,y=300)
        
        self.ugender = Label(self.master,text="Gender",font='times 18',bg='darkseagreen')
        self.ugender.place(x=10,y=350)
        
        self.ulocation = Label(self.master,text="Location",font='times 18',bg='darkseagreen')
        self.ulocation.place(x=10,y=400)
        
        self.uphone = Label(self.master,text="Phone no.",font='times 18',bg='darkseagreen')
        self.uphone.place(x=10,y=450)
        
        self.utime = Label(self.master,text="Appointment Time",font='times 18',bg='darkseagreen')
        self.utime.place(x=10,y=500)

        # ENTRIES FOR EACH LABEL
        self.ent1 = Entry(self.master,width=30)
        self.ent1.place(x=220,y=255)
        self.ent1.insert(END,str(self.name1))
        

        self.ent2 = Entry(self.master,width=30)
        self.ent2.place(x=220,y=305)
        self.ent2.insert(END,str(self.age))

        self.ent3 = Entry(self.master,width=30)
        self.ent3.place(x=220,y=355)
        self.ent3.insert(END,str(self.gender))

        self.ent4 = Entry(self.master,width=30)
        self.ent4.place(x=220,y=405)
        self.ent4.insert(END,str(self.location))

        self.ent5 = Entry(self.master,width=30)
        self.ent5.place(x=220,y=455)
        self.ent5.insert(END,str(self.phone))

        self.ent6 = Entry(self.master,width=30)
        self.ent6.place(x=220,y=505)
        self.ent6.insert(END,str(self.time))


        #button to execute update
        self.update = Button(self.master,text="Update",width=20,height=2,bg='springgreen',command=self.update_db)
        self.update.place(x=220,y=555)

        #button to delete
        self.delete = Button(self.master,text="Delete",width=20,height=2,bg='red',command=self.delete_db)
        self.delete.place(x=400,y=555)

        

    def update_db(self):
        #declaring the varialbe to updtae
        self.v1= self.ent1.get()
        self.v2= self.ent2.get()
        self.v3= self.ent3.get()
        self.v4= self.ent4.get()
        self.v5= self.ent5.get()
        self.v6= self.ent6.get()

        query = "UPDATE appointments SET NAME=?, AGE=?, GENDER=?, LOCATION=?, PHONE=?, SCHEDULED_TIME=? WHERE NAME LIKE ?"
        c.execute(query,(self.v1,self.v2,self.v3,self.v4,self.v5,self.v6,self.name_ent.get(),))
        conn.commit()

        tkinter.messagebox.showinfo("UPDATED","Successfully Updated")

    def delete_db(self):

        sql2="DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2,(self.name_ent.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("DELETED","Successfully Deleted")

        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
        


        

# creating the object
root= Tk()
b= application(root)

# icon
icon = PhotoImage(file='sharda.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

#photo

photo = PhotoImage(file="Campus4.png")
pic = Label(root,image=photo)
pic.place(x=300,y=600)





root.geometry("1200x720+0+0")
root.resizable(False,False)
root.title('Sharda Hospital Management')
root.configure(bg='darkseagreen')
root.mainloop()
