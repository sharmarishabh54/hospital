from tkinter import *
import sqlite3
import sys
import tkinter.messagebox


# create connection

conn = sqlite3.connect('database1.db')

# cursor to move 
c = conn.cursor()




# tkinter window
class Application:
    def __init__(self,master):
        self.master = master

    


        #labels
        self.heading=Label(master,text="Doctor's Details",font="times 40 ",fg='black',bg='darkseagreen')
        self.heading.place(x=10,y=5)
        self.dname = Label(master,text="Doctor's Name",font="times 18", fg='black',bg='darkseagreen')
        self.dname.place(x=10,y=100)

       
        self.dgender = Label(master,text="Gender",font="times 18", fg='black',bg='darkseagreen')
        self.dphone = Label(master,text="Phone no.",font="times 18", fg='black',bg='darkseagreen')
        self.dphone.place(x=10,y=180)

        self.daddress = Label(master,text="Address",font="times 18", fg='black',bg='darkseagreen')
        self.ddepartment = Label(master,text="Department",font="times 18", fg='black',bg='darkseagreen')

      
        self.dgender.place(x=10,y=140)
        self.daddress.place(x=10,y=220)
        self.ddepartment.place(x=10,y=260)

        

     

        #entries

        self.dname_ent= Entry(master,width=30)
        self.dname_ent.place(x=230,y=110)



        self.dgender_ent= Entry(master,width=30)
        self.dgender_ent.place(x=230,y=150)

        self.dphone_ent= Entry(master,width=30)
        self.dphone_ent.place(x=230,y=190)

        self.daddress_ent= Entry(master,width=30)
        self.daddress_ent.place(x=230,y=230)

        self.ddepartment_ent= Entry(master,width=30)
        self.ddepartment_ent.place(x=230,y=270)

        
        
        #button to perform a command

        self.submit= Button(master,text="Save",font="times 14",width=20,height=2,bg='tan',command=self.add1)
        self.submit.place(x=100,y=320)
        
        
     

    # make function working
    def add1(self):
            self.v1=self.dname_ent.get()
            
            self.v2=self.dgender_ent.get()
            self.v3=self.dphone_ent.get()
            self.v4=self.daddress_ent.get()
            self.v5=self.ddepartment_ent.get()
            if self.v1== '' or self.v2== '' or self.v3== '' or self.v4== '' or self.v5== '':
                tkinter.messagebox.showinfo("Warning","Please Fill All Enrties")
                
                
            else:
                # now add to database
                sql = "INSERT INTO 'doctor' (d_name , d_department , d_gender , d_phone , d_address) VALUES(?,?,?,?,?)"
                c.execute(sql,(self.v1,self.v5,self.v2,self.v3,self.v4))
                conn.commit()
                tkinter.messagebox.showinfo("Success"," Data for Dr. " +str(self.v1)+" has been created ")
                
                 


    
        



root=Tk()
b =Application(root)
root.geometry("500x500+0+0")
root.title('Sharda Hospital Management')
icon = PhotoImage(file='sharda.png')
root.tk.call('wm', 'iconphoto', root._w, icon)


#photo
photo = PhotoImage(file="Campus4.png")
pic = Label(root,image=photo)
pic.place(x=10,y=400)


root.resizable(False,False)
root.configure(bg='darkseagreen')


root.mainloop()


