from tkinter import *
import sqlite3
import sys
import tkinter.messagebox


# create connection

conn = sqlite3.connect('database1.db')

# cursor to move 
c = conn.cursor()

# empty list
ids = []
id2= []

# tkinter window
class Application:
    def __init__(self,master):
        self.master = master

        # create the frames 
        self.left = Frame(master, width=800,height=720,bg='darkseagreen')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=400,height=720,bg='gold')
        self.right.pack(side=RIGHT)

        #labels
        self.heading=Label(master,text="Sharda Hospital",font="times 40 ",fg='black',bg='darkseagreen')
        self.heading.place(x=250,y=5)
        self.name = Label(master,text="Patient's name",font="times 18", fg='black',bg='darkseagreen')
        self.name.place(x=10,y=100)

        self.age = Label(master,text="Age",font="times 18", fg='black',bg='darkseagreen')
        self.gender = Label(master,text="Gender",font="times 18", fg='black',bg='darkseagreen')
        self.phone = Label(master,text="Phone No.",font="times 18", fg='black',bg='darkseagreen')
        self.phone.place(x=10,y=220)

        self.location = Label(master,text="Location",font="times 18", fg='black',bg='darkseagreen')
        self.time = Label(master,text="Appointment Time",font="times 18", fg='black',bg='darkseagreen')

        self.age.place(x=10,y=140)
        self.gender.place(x=10,y=180)
        self.location.place(x=10,y=260)
        self.time.place(x=10,y=300)

        self.log=Label(self.right,text="Appointment Logs",font='times,18',fg='black',bg='gold')
        self.log.place(x=100,y=2)

     

        #entries

        self.name_ent= Entry(master,width=30)
        self.name_ent.place(x=250,y=110)

        self.age_ent= Entry(master,width=30)
        self.age_ent.place(x=250,y=150)

        self.gender_ent= Entry(master,width=30)
        self.gender_ent.place(x=250,y=190)

        self.phone_ent= Entry(master,width=30)
        self.phone_ent.place(x=250,y=230)

        self.location_ent= Entry(master,width=30)
        self.location_ent.place(x=250,y=270)

        self.time_ent= Entry(master,width=30)
        self.time_ent.place(x=250,y=310)

        
        

        #button to perform a command

        self.submit= Button(master,text="Add Appointment",font="times 14",width=20,height=2,bg='tan',command=self.add1)
        self.submit.place(x=260,y=340)

        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        #odering the ids    
        self.new= sorted(ids)
        self.final_id=self.new[len(ids)-1]
        

        
        # display appointments
        self.box= Text(self.right,width=42,height=40)
        self.box.place(x=25,y=30)
        self.box.insert(END,"Total Appointments till now : " + str(self.final_id))
        
        
     

    # make function working
    def add1(self):
            self.v1=self.name_ent.get()
            self.v2=self.age_ent.get()
            self.v3=self.gender_ent.get()
            self.v4=self.phone_ent.get()
            self.v5=self.location_ent.get()
            self.v6=self.time_ent.get()
            if self.v1== '' or self.v2== '' or self.v3== '' or self.v4== '' or self.v5== '' or self.v6== '':
                tkinter.messagebox.showinfo("Warning","Please Fill All Enrties")
                
                
            else:
                # now add to database
                sql = "INSERT INTO 'appointments' (NAME, AGE, GENDER, PHONE, LOCATION, SCHEDULED_TIME) VALUES(?,?,?,?,?,?)"
                c.execute(sql,(self.v1,self.v2,self.v3,self.v4,self.v5,self.v6))
                conn.commit()
                tkinter.messagebox.showinfo("Success"," Appointment for " +str(self.v1)+" has been created ")
                
                self.box.insert(END,'\n Appointment Fixed For ' + str(self.v1) + ' at ' + str(self.v6))    


    
        



root=Tk()
b =Application(root)
root.geometry("1200x720+0+0")
root.title('Sharda Hospital Management')
icon = PhotoImage(file='sharda.png')
root.tk.call('wm', 'iconphoto', root._w, icon)


#photo
photo = PhotoImage(file="Campus4.png")
pic = Label(root,image=photo)
pic.place(x=180,y=600)


root.resizable(False,False)


root.mainloop()


