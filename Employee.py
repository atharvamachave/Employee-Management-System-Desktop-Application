from cProfile import label
from msilib import Table
from multiprocessing import parent_process
from os import stat
from re import search
from sqlite3 import Row
from tkinter import*
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.tix import COLUMN
from tokenize import String
from turtle import Vec2D, bgcolor
from PIL import Image,ImageTk
from cv2 import exp
from django.db import DatabaseError
from matplotlib.pyplot import grid, text
from numpy import tile
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1535x830+0+0")
        self.root.title("Employee Management System")


        #Variables :
        self.var_dept=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        self.var_id=StringVar()
        self.var_aadhar=StringVar()
        

        lbl_title = Label(self.root,text="Employee Management System",font=('times new roman',32,'italic'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1535,height=50)

        img_logo = Image.open('images/user.png')
        img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=0,y=0,width=50,height=50)

        #main frame
        Main_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=70,width=1505,height=760)

        #upper frame
        upper_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text="Employee Information...",font=('times new roman',12,'bold'),fg='blue')
        upper_frame.place(x=180,y=10,width=1150,height=370)

        # Label and Entry fields
        lbl_dept = Label(upper_frame,text='Department :',font=('Calibiri',12,'bold'),bg='white')
        lbl_dept.grid(row=0,column=0,padx=2,sticky=W)

        combo_dept = ttk.Combobox(upper_frame,textvariable=self.var_dept,font=('times new roman',12,'bold'),width=25,state="readonly")
        combo_dept['value']=('Select Department','Developer','Marketing','Finance','HR','Technology','Research & Development','Production','Customer services')
        combo_dept.current(0)
        combo_dept.grid(row=0,column=1,padx=2,pady=1,sticky=W)

        # Name label
        lbl_name=Label(upper_frame,font=('Calibiri',12,'bold'),text="Name :",bg="white")
        lbl_name.grid(row=0,column=2,sticky=W,padx=60,pady=15)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=25,font=('Calibiri',12,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=12)

        # Designation
        lbl_desc=Label(upper_frame,font=('Calibiri',12,'bold'),text="Designation :",bg="white")
        lbl_desc.grid(row=1,column=0,sticky=W,padx=2,pady=12)

        txt_desc=ttk.Entry(upper_frame,textvariable=self.var_designation,width=24,font=('Calibiri',12,'bold'))
        txt_desc.grid(row=1,column=1,sticky=W,padx=2,pady=12)
        

        # Email
        lbl_email=Label(upper_frame,font=('Calibiri',12,'bold'),text="Email :",bg="white")
        lbl_email.grid(row=1,column=2,sticky=W,padx=60,pady=12)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=25,font=('Calibiri',12,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=12)

        # Address

        lbl_address=Label(upper_frame,font=('Calibiri',12,'bold'),text="Address :",bg="white")
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=12)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=24,font=('Calibiri',12,'bold'))
        txt_address.grid(row=2,column=1,sticky=W,padx=2,pady=12)


        # Married

        lbl_marry = Label(upper_frame,text='Marital status :',font=('Calibiri',12,'bold'),bg='white')
        lbl_marry.grid(row=2,column=2,padx=60,pady=7,sticky=W)

        combo_marry = ttk.Combobox(upper_frame,textvariable=self.var_married,font=('times new roman',12,'bold'),width=26,state="readonly")
        combo_marry['value']=('Married','Unmarried','Widowed')
        combo_marry.current(1)
        combo_marry.grid(row=2,column=3,padx=2,pady=12,sticky=W)


        # DOB

        lbl_dob=Label(upper_frame,font=('Calibiri',12,'bold'),text="DOB :",bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=12)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=24,font=('Calibiri',12,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=12)


         # DOJ

        lbl_doj=Label(upper_frame,font=('Calibiri',12,'bold'),text="DOJ :",bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=60,pady=12)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=25,font=('Calibiri',12,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=12)


        # Gender
        
        lbl_gender = Label(upper_frame,text='Gender :',font=('Calibiri',12,'bold'),bg='white')
        lbl_gender.grid(row=4,column=0,padx=2,pady=12,sticky=W)

        combo_gender = ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('times new roman',12,'bold'),width=25,state="readonly")
        combo_gender['value']=('Male','Female','Others')
        combo_gender.current(1)
        combo_gender.grid(row=4,column=1,padx=2,pady=12,sticky=W)


        #Phone
        lbl_phone=Label(upper_frame,font=('Calibiri',12,'bold'),text="Phone No :",bg="white")
        lbl_phone.grid(row=4,column=2,sticky=W,padx=60,pady=12)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=25,font=('Calibiri',12,'bold'))
        txt_phone.grid(row=4,column=3,padx=2,pady=12)

        #Country
        lbl_country=Label(upper_frame,font=('Calibiri',12,'bold'),text="Country :",bg="white")
        lbl_country.grid(row=5,column=0,sticky=W,padx=2,pady=12)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=24,font=('Calibiri',12,'bold'))
        txt_country.grid(row=5,column=1,padx=2,pady=12)

        #Salary(Package)
        lbl_ctc=Label(upper_frame,font=('Calibiri',12,'bold'),text="Package :",bg="white")
        lbl_ctc.grid(row=5,column=2,sticky=W,padx=60,pady=12)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=25,font=('Calibiri',12,'bold'))
        txt_ctc.grid(row=5,column=3,padx=2,pady=12)

        #ID
        lbl_id=Label(upper_frame,font=('Calibiri',12,'bold'),text="Employee ID :",bg="white")
        lbl_id.grid(row=6,column=0,sticky=W,padx=2,pady=12)

        txt_id=ttk.Entry(upper_frame,textvariable=self.var_id,width=24,font=('Calibiri',12,'bold'))
        txt_id.grid(row=6,column=1,padx=2,pady=12)


        #Aadhar No:

        lbl_aadhar=Label(upper_frame,font=('Calibiri',12,'bold'),text="Aadhar No:",bg="white")
        lbl_aadhar.grid(row=6,column=2,sticky=W,padx=60,pady=12)

        txt_aadhar=ttk.Entry(upper_frame,textvariable=self.var_aadhar,width=25,font=('Calibiri',12,'bold'))
        txt_aadhar.grid(row=6,column=3,padx=2,pady=12)

       
       
        button_frame = Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=900,y=10,width=170,height=290)


        btn_add = Button(button_frame,text="Save",command=self.add_data,font=("arial",18,"bold"),width=10,bg='purple',fg='white')
        btn_add.grid(row=0,column=0,padx=2,pady=10)

        btn_update = Button(button_frame,text="Update",command=self.update_data,font=("arial",18,"bold"),width=10,bg='purple',fg='white')
        btn_update.grid(row=1,column=0,padx=2,pady=10)


        btn_delete = Button(button_frame,text="Delete",command=self.delet_data,font=("arial",18,"bold"),width=10,bg='purple',fg='white')
        btn_delete.grid(row=2,column=0,padx=2,pady=10)

        btn_clear = Button(button_frame,text="Clear",command=self.clear_data,font=("arial",18,"bold"),width=10,bg='purple',fg='white')
        btn_clear.grid(row=3,column=0,padx=2,pady=10)

        #lower frame
        lower_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text="Employee Retrived Information",font=('times new roman',12,'bold'),fg='green')
        lower_frame.place(x=10,y=380,width=1480,height=350)


        #Search Frame
        search_frame = LabelFrame(lower_frame,bd=2,relief=RIDGE,bg='white',text="Search Information",font=('times new roman',12,'bold'),fg='red')
        search_frame.place(x=3,y=0,width=1470,height=70)

        search_by=Label(search_frame,font=("arial",12,"bold"),text='Search By',fg='white',bg='green')
        search_by.grid(row=0,column=0,sticky=W,padx=5)


        #Search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_search['value']=('Pick Option','ID','Phone')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",12,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn__search=Button(search_frame,command=self.search_data,text="search",font=("arial",12,"bold"),width=14,bg='green',fg='white')
        btn__search.grid(row=0,column=3,padx=5)

        btn__search=Button(search_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),width=14,bg='green',fg='white')
        btn__search.grid(row=0,column=4,padx=5)

        slogan = Label(search_frame,text="A company’s most valuable asset is its employees.",font=("times new roman",20,"bold"),bg='white',fg='blue')
        slogan.place(x=850,y=0,width=600,height=30)


        # --------------Employee Table---------------

        table_frame = Frame(lower_frame,bd=3,relief=RIDGE,bg='grey')
        table_frame.place(x=0,y=60,width=1485,height=270)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=('dept','name','desc','email','add','marry','dob','doj','gen','phone','country','package','id','aadhar',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dept',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desc',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('add',text='Address')
        self.employee_table.heading('marry',text='Marital Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('gen',text='Gender')
        self.employee_table.heading('phone',text='Phone NO')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('package',text='Package')
        self.employee_table.heading('id',text='ID')
        self.employee_table.heading('aadhar',text='Aadhar No')

        self.employee_table['show']='headings'
        
        self.employee_table.column('dept',width=100)
        self.employee_table.column('desc',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('add',width=100)
        self.employee_table.column('marry',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('gen',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('package',width=100)
        self.employee_table.column('id',width=100)
        self.employee_table.column('aadhar',width=100)
        

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()


    #------------Function Declarations--------------*    

    def add_data(self):
        if self.var_dept.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','Please Filled All Fields')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='password',database='employee')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                                self.var_dept.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_designation.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_married.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_country.get(),
                                                                                                                self.var_salary.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_aadhar.get()

                                                                                                             ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Data inserted successfully...',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)
            
               
    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='password',database='employee')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content['values']
        self.var_dept.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_gender.set(data[8])
        self.var_phone.set(data[9])
        self.var_country.set(data[10])
        self.var_salary.set(data[11])
        self.var_id.set(data[12])
        self.var_aadhar.set(data[13])


    #Update

    def update_data(self):
        if self.var_dept.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','Please Filled All Fields')
        else:
            try:
                update = messagebox.askyesno('Update','Do you want To Update This Employee')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='password',database='employee')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Marital_Status=%s,DOB=%s,DOJ=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s,AadharNo=%s where ID=%s',(


                                                                                                                                                                                                                    self.var_dept.get(),
                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                    self.var_designation.get(),
                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_married.get(),
                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                    self.var_doj.get(),
                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                    self.var_country.get(),
                                                                                                                                                                                                                    self.var_salary.get(),
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    self.var_aadhar.get(),
                                                                                                                                                                                                                    self.var_id.get(),                        



                                                                                                                                                                                                                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee updated Successfully...',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)


    #Delete
    def delet_data(self):
        if self.var_id.get()=="":
            messagebox.showerror('Error',"All Fields Are Required")
        else:
            try:
                Delete = messagebox.askyesno('Delete','Do You Want To Delete this Employee',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='password',database='employee')
                    my_cursor=conn.cursor()
                    sql = 'delete from employee where ID=%s'
                    value=(self.var_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Deleted Successfully...',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)            


    # Clear
    def clear_data(self):
        self.var_dept.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")
        self.var_id.set("")
        self.var_aadhar.set("")


    #search

    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror('Error','Please Select Option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='password',database='employee')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows = my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                else:
                     messagebox.showinfo('Not Found','Employee Not Found...',parent=self.root)    


                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)            

    

                    





if __name__=="__main__":
    root = Tk()
    emp = Employee(root)
    root.mainloop()      
