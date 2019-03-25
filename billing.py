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
        self.heading=Label(master,text="Billing Details",font="times 40 ",fg='black',bg='darkseagreen')
        self.heading.place(x=10,y=5)
        self.billno = Label(master,text="Bill no.",font="times 18", fg='black',bg='darkseagreen')
        self.billno.place(x=10,y=100)

        self.roomtype = Label(master,text="Room Type",font="times 18", fg='black',bg='darkseagreen')
        self.roomtype.place(x=10,y=140)

       
        self.roomcharge = Label(master,text="Room Charges",font="times 18", fg='black',bg='darkseagreen')
        self.document = Label(master,text="Documentation Charges",font="times 18", fg='black',bg='darkseagreen')
        self.document.place(x=10,y=220)

        self.date = Label(master,text="Date",font="times 18", fg='black',bg='darkseagreen')
        self.date.place(x=10,y=260)


        

        self.total = Label(master,text="Total Amount",font="times 18", fg='black',bg='darkseagreen')


      
        self.roomcharge.place(x=10,y=180)
        self.total.place(x=10,y=300)
      

        

     

        #entries

        self.billno_ent= Entry(master,width=30)
        self.billno_ent.place(x=250,y=110)



        self.roomtype_ent= Entry(master,width=30)
        self.roomtype_ent.place(x=250,y=150)

        self.roomcharge_ent= Entry(master,width=30)
        self.roomcharge_ent.place(x=250,y=190)

        self.document_ent= Entry(master,width=30)
        self.document_ent.place(x=250,y=230)

        self.date_ent= Entry(master,width=30)
        self.date_ent.place(x=250,y=270)

        self.total_ent= Entry(master,width=30)
        self.total_ent.place(x=250,y=310)

        
        
        #button to perform a command

        self.submit= Button(master,text="Generate bill",font="times 14",width=20,height=2,bg='tan',command=self.add1)
        self.submit.place(x=100,y=340)


        # display bill
        self.box=Text(master,width=50,height=27)
        self.box.place(x=500,y=20)
        
     

    # make function working
    def add1(self):
            self.v1=self.billno_ent.get()
            
            self.v2=self.roomtype_ent.get()
            self.v3=self.roomcharge_ent.get()
            self.v4=self.document_ent.get()
            self.v5=self.date_ent.get()
            
            self.v6=self.total_ent.get()

            

                                       
            if self.v1== '' or self.v2== '' or self.v3== '' or self.v4== '' or self.v5== '' or self.v6== '':
                tkinter.messagebox.showinfo("Warning","Please Fill All Enrties")
                
                
            else:
                # now add to database
                sql = "INSERT INTO 'billing' (bill_no , room_charge , document_charge  , total_amount , room_type , date ) VALUES(?,?,?,?,?,?)"
                c.execute(sql,(self.v1,self.v3,self.v4,self.v6,self.v2,self.v5))
                conn.commit()
              
                tkinter.messagebox.showinfo("Success"," Bill generated successfully ")
                self.box.insert(END,'\n date = ' + str(self.v5) + '\n\n Bill no. =' + str(self.v1) + '\n\n Room Type = ' + str(self.v2) + '\n\n Room Charges =' + str(self.v3) + '\n\n Documentation Charges = ' + str(self.v4) + '\n\n Total charges = ' + str(self.v5))
                
                
                 


    
        



root=Tk()
b =Application(root)
root.geometry("920x500+0+0")
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
