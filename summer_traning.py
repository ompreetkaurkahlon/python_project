
 
from tkinter import *
import mysql.connector
from tkinter import messagebox

root= Tk()
root.title("summer training project")
root.geometry("700x700")


cnn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="prince2003",
                database="collegeproject",
                port=3306
                    )
mycursor=cnn.cursor()

marks = 0
    
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()   



def start():
    clear_frame()
    lbl1=Label(root,text="Registration",bg="orange",fg="black",anchor="center",font=("Copperplate Gothic Light",20)).pack(pady=3,padx=3)

    btn1=Button(root,text="Click Here To Register",bg="orange",fg="black",font=("Copperplate Gothic Light",15),command=registration,anchor="center").pack(pady=3,padx=3)


    lbl2=Label(root,text="Login",bg="orange",fg="black",font=("Copperplate Gothic Light",20),anchor="center").pack(pady=3,padx=3)

    btn2=Button(root,text="Click Here For Login",bg="orange",fg="black",font=("Copperplate Gothic Light",15),command=login,anchor="center").pack(pady=3,padx=3)


    lbl3=Label(root,text="Selection Window",bg="orange",fg="black",font=("Copperplate Gothic Light",20),anchor="center").pack(pady=3,padx=3)

    btn3=Button(root,text="Click Here For Selection",bg="orange",fg="black",font=("Copperplate Gothic Light",15),command=selection_page,anchor="center").pack(pady=3,padx=3)

           
             
                
        
def login():
    
    def retrive():
        clear_frame()
        
        flag=0
        useremail= v1.get()
        userpwd= v2.get()
        cnn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="prince2003",
                database="collegeproject",
                port=3306
                    )
       
        mycursor=cnn.cursor()
        sql="select * from register"
        try:
            mycursor.execute(sql)
            results=mycursor.fetchall()
            for row in results:
                dbemail=row[3]
                dbpwd=row[4]
                if((useremail==dbemail)and (userpwd==dbpwd)):
                    flag=1
          
        except:
            print("error: unable to fetch all data")
            cnn.rollback()
        cnn.close()

        if(flag==1):
            
            print("login  success")
            btn=Button(root,text="next",command=selection_page,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
            
        else:
            print("login  not success")
            result = messagebox.askquestion("Error",
                           "Do you want to Re-Login")
            if result == "yes":
                {
                login()
                }
            else:
               {
               start()
               }
            
        

    v1=StringVar()
    v2=StringVar()

    clear_frame()
    lbl2=Label(root,text="log in here",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    lbl1=Label(root,text="enter your email",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    e1=Entry(root,textvariable=v1).pack(pady=3,padx=3)
    lbl3=Label(root,text="enter your password",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    e2=Entry(root,textvariable=v2).pack(pady=3,padx=3)





   
    


    btn1=Button(root,text="login",command=retrive,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    
   

def registration():
    clear_frame()

    
    def insert():
        cnn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="prince2003",
                database="collegeproject",
                port=3306
                    ) 
        
        cursor=cnn.cursor()
        sql="insert into register set id='%d',name='%s',department='%s',email='%s',password='%s'"%(v1.get(),v2.get(),v3.get(),v4.get(),v5.get())
        try:
            cursor.execute(sql)
            cnn.commit()
            print("data inserted")
        except:
            cnn.rollback()
            cnn.close()


      
    
    
    v1=IntVar()
    v2=StringVar()
    v3=StringVar()
    v4=StringVar()
    v5=StringVar()





    Lbl1=Label(root,text="Welcome for registration",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    Lbl2=Label(root,text="Enter your id",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    e1=Entry(root,textvariable=v1).pack(pady=3,padx=3)
    Lbl3=Label(root,text="Enter your name",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    e2=Entry(root,textvariable=v2).pack(pady=3,padx=3)
    Lbl4=Label(root,text="Enter your department",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    e3=Entry(root,textvariable=v3).pack(pady=3,padx=3)
    Lbl5=Label(root,text="Enter your email id",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    e4=Entry(root,textvariable=v4).pack(pady=3,padx=3)
    Lbl6=Label(root,text="Enter your password",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    e5=Entry(root,textvariable=v5).pack(pady=3,padx=3)





    
    
    
    
    
    

    btn1=Button(root,text="register",command=insert,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    btn=Button(root,text="next",command=login,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    



def selection_page():
    clear_frame()
    
    var=IntVar()
    def selection():
        cnn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="prince2003",
        database="mydb",
        port=3306
        )
        mycursor=cnn.cursor()
           
        sql="select * from register"
       
        try:
            mycursor.execute(sql)
            selection="You selected the option"+ str(var.get())
           
            print(selection)
        except:
            print("error: unable to fetch all data")
            cnn.rollback()
        cnn.close()
       
    lbl1=Label(root,text="selection  of the paper language",fg="black",bg="pink",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)


    r1=Button(root,text="C language",fg="black",bg="orange",command=clanguage,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    r2=Button(root,text="java language",fg="black",bg="orange",command=javalanguage,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    r3=Button(root,text=" Python language",fg="black",bg="orange",command=pythonlanguage,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)
    r4=Button(root,text="C++ language",fg="black",bg="orange",command=cpplanguage,font=('Copperplate Gothic Light',20),anchor="center").pack(pady=3,padx=3)

    


def clanguage():
    global marks
    clear_frame()
    
   
     
    
    def question1():
        global marks
        clear_frame()
       
        def result1():
            global marks
            ans1=str(var.get())
            true="2"
            if(true==ans1):
                 marks+=1
               
            else:
                 marks
               
    
    
        var=IntVar()
        clear_frame()
    
        lbl1=Label(root,text="1). Year when the c language was introduced to the world?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).1974",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).1972",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).1976",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).1973",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

    def question2():
        global marks
        clear_frame()
       
        def result2():
            global marks
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                 marks+=1
           
            else:
                 marks
            
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="2).Which of the following is not the data type of c language?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).ARRAY",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).POINTER",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text=" c).DICTIONARY",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).STRUCTURE",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        
    def question3():
        global marks
        clear_frame()
        
        def result3():
            global marks
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                 marks+=1
            else:
                 marks
                
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="3).HOW MANY SPACES TAB HAS IN C LANGUAGE?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).8",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).9",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text=" c).7",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).6",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        
    def question4():
        global marks
        clear_frame()
        
        def result4():
            global marks
            ans1=str(var.get())
            true="4"
        
            if(true==ans1):
                 marks+=1
         
            else:
                 marks
                 
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="4).Which of the following is not a valid C variable name?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). int number;",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). float rate;",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). int variable_count;",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). int $main;",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question5():
        global marks
        clear_frame()
        
        def result5():
    
            global marks
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                 marks+=1
                
            else:
                 marks
               
    
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="5). Which of the following is true for variable names in C?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). They can contain alphanumeric characters as well as special characters",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). It is not an error to declare a variable to be one of the keywords(like goto, static)",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). Variable names cannot start with a digit",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). Variable can be of any length",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question6():
        global marks
        clear_frame()
        
        def result6():
            global marks
            ans1=str(var.get())
            true="2"
            if(true==ans1):
                 marks+=1
                 
            else:
                 marks
                 
            
    
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="6). Which is valid C expression?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). int my_num = 100,000;",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). int my_num = 100000;",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). int my num = 1000;",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). int $my_num = 10000;",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
    
        btn=Button(root,text="submit",fg="black",bg="pink",command=result6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question7():
        global marks
        clear_frame()
        
        def result7():
            global marks
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                 marks+=1
                
            else:
                 marks
                
    
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="7). What is short int in C programming?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). The basic data type of C",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). Qualifier",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Short is the qualifier and int is the basic data type",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). All of the mentioned",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question8():
        global marks
        clear_frame()
        
        def result8():
            global marks
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                marks+=1
             
            else:
                 marks
                
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="8). Which keyword is used to prevent any changes in the variable within a C program?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). immutable",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). mutable",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). const",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). volatile",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question9():
        global marks
        clear_frame()
        
        def result9():
        
            global marks
            
            ans1=str(var.get())
            true="2"
            if(true==ans1):
                 marks+=1
                
            else:
                 marks
              
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="9). What is the result of logical or relational expression in C?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a) True or False",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) 0 or 1",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) 0 if an expression is false and any positive number if an expression is true",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) None of the mentioned",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question10():
        global marks
        clear_frame()
        
        def result10():
           
            global marks
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                 marks+=1
               
            else:
                marks
            show_result()
            
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="10). Which of the following typecasting is accepted by C language?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). Widening conversions",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). Narrowing conversions",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). Widening & Narrowing conversions",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). None of the mentioned",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
       
    btn=Button(root,text="start",fg="orange",bg="black",command=question1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

def show_result():
    clear_frame()
    result_label = Label(root, text=f"CONGRATULATIONS! You completed the quiz.\nYou scored {marks} out of {10}.", font=("Copperplate Gothic Light", 15))
    result_label.pack(padx=10, pady=10)    


    

def javalanguage():
    global marks
    clear_frame()
    
    def question1():
        global marks
        clear_frame()
        def result1():
            global marks
            
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                 marks+=1
            else:
                 marks
               
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="1. Arrays in java are-",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)       

        r1=Radiobutton(root,text="a) Object reference",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) object",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) primitive data type",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) none",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        

    def question2():
        global marks
        clear_frame()
        def result2():
            global marks
           
            
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                 marks+=1
              
            else:
                 marks
              
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="2).Which of the following option leads to the portability and security of Java?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a) Bytecode is executed by JVM ",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) The applet makes the Java code secure and portable",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) Use of exception handling",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) Dynamic binding between objects",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question3():
        global marks
        clear_frame()
       
        def result3():
            global marks
       
            ans1=str(var.get())
            true="2"
            if(true==ans1):
                 marks+=1
            else:
                 marks
                
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="3).  What makes the Java platform independent?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a) Advanced programming language",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) It uses bytecode for execution",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text=" c)  Class compilation",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d)All of these",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question4():
        global marks
        clear_frame()
        def result4():
            global marks
    
            ans1=str(var.get())
            true="3"
        
            if(true==ans1):
                 marks+=1
                 
            else:
                 marks
               
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="4). What are the types of memory allocated in memory in java?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).Heap memory",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). Stack memory",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Both A and B",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). None of these",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question5():
        global marks
        clear_frame()
    
        def result5():
            global marks
    
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                 marks+=1
                
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="5).  What is the entry point of a program in Java?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).main() method",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).The first line of code",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). Last line of code",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). main class",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question6():
        global marks
        clear_frame()
        def result6():
            global marks
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                marks+=1
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="6).  Which keyword in java is used for exception handling?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).exep",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). excepHand",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). throw",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).All of these",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
    
        btn=Button(root,text="submit",fg="black",bg="pink",command=result6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question7():
        global marks
        clear_frame()
        def result7():
            global marks
   
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="7). Which class in Java is used to take input from the user?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).Scanner",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). Input",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Applier",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). None of these",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question8():
        global marks
        clear_frame()
        def result8():
            global marks

            ans1=str(var.get())
            true="3"
            if(true==ans1):
                marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="8).Method used to take a string as input in Java?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).next()",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).nextLine()",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Both A. and B.",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).None of these",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
       
    def question9():
        global marks
        clear_frame()
        def result9():
            global marks
   
            ans1=str(var.get())
            true="2"
            if(true==ans1):
                marks+=1
               
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="9).Which of the following is the correct syntax to create a variable in Java?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    
 
        r1=Radiobutton(root,text="a) var name;",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) int name;",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) var name int;",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) All of these",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question10():
        global marks
        clear_frame()
    
        def result10():
            global marks
    
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                marks+=1
            else:
                marks
            show_result()
        var=IntVar()  
        lbl1=Label(root,text="10).Which of the following option leads to the portability and security of Java?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    
        r1=Radiobutton(root,text="a).Bytecode is executed by JVM",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).The applet makes the Java code secure and portable",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Use of exception handling",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).Dynamic binding between objects",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
      
    btn=Button(root,text="start",bg="black",fg="pink",command=question1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    
    

def cpplanguage():
    global marks
    
    clear_frame()
    def question1():
        global marks
        clear_frame()
        def result1():
            global marks
        
            ans1=str(var.get())
            true="3"
            if(true==ans1):
               marks+=1
           
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="1). What is C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a) C++ is an object oriented programming language",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) C++ is a procedural programming language",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) C++ supports both procedural and object oriented programming language",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) C++ is a functional programming language",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        
    def question2():
        global marks
        clear_frame()
        def result2():
            global marks
          
            ans1=str(var.get())
            true="2"
            if(true==ans1):
                marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="2). Which of the following is the correct syntax of including a user defined header files in C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a) #include [userdefined] ",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) #include “userdefined”",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) #include <userdefined.h>",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) #include <userdefined>",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question3():
        global marks
        clear_frame()
        def result3():
            global marks
       
            
            ans1=str(var.get())
            true="4"
            if(true==ans1):
               marks+=1
              
            else:
                 marks= 0
               
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="3). Which of the following is used for comments in C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a) /* comment */",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) // comment */",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text=" c)  // comment",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d)both // comment or /* comment */",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question4():
        global marks
        clear_frame()
        def result4():
            global marks
   
            ans1=str(var.get())
            true="1"
            
            if(true==ans1):
                marks+=1
             
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="4).Which of the following is a correct identifier in C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). VAR_1234",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). $var_name",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). 7VARNAME",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). 7var_name",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        
        btn=Button(root,text="submit",fg="black",bg="pink",command=result4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question5():
        global marks
        clear_frame()
     
        def result5():
            global marks
    
            ans1=str(var.get())
            true="4"
            if(true==ans1):
                marks+=1
            
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="5).  Which of the following is not a type of Constructor in C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). Default constructor",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). Parameterized constructor",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). Copy constructor",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). Friend constructor",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question6():
        global marks
        clear_frame()
    
        def result6():
            global marks
 
            ans1=str(var.get())
            true="3"
            if(true==ans1):
               marks+=1
               
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="6). Which of the following approach is used by C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).Left-right",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). Right-left",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). Bottom-up",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). Top-down",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
    
        btn=Button(root,text="submit",fg="black",bg="pink",command=result6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question7():
        global marks
        clear_frame()
    
        def result7():
            global marks
      
            ans1=str(var.get())
            true="4"
            if(true==ans1):
                marks+=1
                
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="7).  What is virtual inheritance in C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).C++ technique to enhance multiple inheritance",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b). C++ technique to ensure that a private member of the base class can be accessed somehow",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).C++ technique to avoid multiple inheritances of classes",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). C++ technique to avoid multiple copies of the base class into children/derived class",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question8():
        global marks
        clear_frame()
        def result8():
            global marks
       
            ans1=str(var.get())
            true="2"
            if(true==ans1):
               marks+=1

            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="8).What happens if the following C++ statement is compiled and executed?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        lbl2=Label(root,text="int *ptr = NULL;",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl3=Label(root,text="delete ptr;",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)

        r1=Radiobutton(root,text="a).The program is not semantically correct",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).The program is compiled and executed successfully",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).The program gives a compile-time error",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).The program compiled successfully but throws an error during run-time",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="black",bg="pink",command=question9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question9():
        global marks
        clear_frame()
       
        def result9():
            global marks
     
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                 marks+=1
             
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="9). What will be the output of the following C++ code?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        lbl2=Label(root,text="#include <iostream> ",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl3=Label(root,text="#include <string>",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl4=Label(root,text="using namespace std;  ",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl5=Label(root,text="int main(int argc, char const *argv[]) ",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl6=Label(root,text="{ ",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl7=Label(root,text="char s1[6] = Hello; ",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl8=Label(root,text="char s2[6] = World;",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl9=Label(root,text="char s3[12] = s1 + " " + s2;",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl10=Label(root,text="cout<<s3; ",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl11=Label(root,text="return 0;",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
        lbl12=Label(root,text="}",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=1,pady=1)
 
        r1=Radiobutton(root,text="a) Hello",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) World",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) Error",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) Hello World",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",bg="pink",fg="black",command=result9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",fg="pink",bg="black",command=question10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

    def question10():
        global marks
        clear_frame()
        
        def result10():
            global marks
 
            ans1=str(var.get())
            true="4"
            if(true==ans1):
                marks+=1
            else:
                marks
            show_result()
            
     
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="10).What is the difference between delete and delete[] in C++?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).delete is syntactically correct but delete[] is wrong and hence will give an error if used in any case",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).delete is used to delete normal objects whereas delete[] is used to pointer objects",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).delete is a keyword whereas delete[] is an identifier",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).delete is used to delete single object whereas delete[] is used to multiple(array/pointer of) objects",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        
   
    btn1=Button(root,text="start",fg="black",bg="pink",command=question1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    

def pythonlanguage():
    global marks
    
    clear_frame()
    def question1():
        global marks
        clear_frame()
        
        def result1():
            global marks
    
            ans1=str(var.get())
            true="3"
            if(true==ans1):
                marks+=1
              
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="1).Which type of Programming does Python support?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).Wick van Rossum",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).Rasmus Lerdorf",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Guido van Rossum",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).Niene Stom",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn1=Button(root,text="submit",fg="black",bg="pink",command=result1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn=Button(root,text="next",bg="black",fg="pink",command=question2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question2():
        global marks
        clear_frame()
        def result2():
            global marks
   
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="2).Which of the following is not the data type of c language?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).Python code is both compiled and interpreted",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).Python code is neither compiled nor interpreted",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text=" c).Python code is only compiled",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).Python code is only interpreted",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn1=Button(root,text="submit",fg="black",bg="pink",command=result2,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn1=Button(root,text="next",fg="black",bg="pink",command=question3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
       
    def question3():
        global marks
        clear_frame()
     
        def result3():
            global marks
       
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                 marks+=1
             
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="3).What will be the value of the following Python expression?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        lbl1=Label(root,text="4 + 3 % 5",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).7",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).2",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text=" c).4",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).1",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn1=Button(root,text="submit",fg="black",bg="pink",command=result3,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn1=Button(root,text="next",fg="black",bg="pink",command=question4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    
    def question4():
        global marks
        clear_frame()
        def result4():
            global marks
     
            ans1=str(var.get())
            true="1"
        
            if(true==ans1):
                 marks+=1
               
            else:
                 marks
    
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="4).Which of the following is used to define a block of code in Python language?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).Indentation",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).Key",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Brackets",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).All of the mentioned",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn1=Button(root,text="submit",fg="black",bg="pink",command=result4,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn1=Button(root,text="next",fg="black",bg="pink",command=question5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
       
    def question5():
        global marks
        clear_frame()
        def result5():
            global marks
            ans1=str(var.get())
            true="4"
            if(true==ans1):
                 marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="5).Which of the following functions can help us to find the version of python that we are currently working on?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).sys.version(1)",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).  sys.version(0)",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).  sys.version()",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).sys.version",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn1=Button(root,text="submit",fg="black",bg="pink",command=result5,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn1=Button(root,text="next",fg="black",bg="pink",command=question6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question6():
        global marks
        clear_frame()
        def result6():
            global marks
    
            ans1=str(var.get())
            true="4"
            if(true==ans1):
                 marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="6).What is the order of precedence in python?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).Exponential, Parentheses, Multiplication, Division, Addition, Subtraction",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).Exponential, Parentheses, Division, Multiplication, Addition, Subtraction",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).Parentheses, Exponential, Multiplication, Division, Subtraction, Addition",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).Parentheses, Exponential, Multiplication, Division, Addition, Subtraction",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
    
        btn1=Button(root,text="submit",fg="black",bg="pink",command=result6,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn1=Button(root,text="next",fg="black",bg="pink",command=question7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question7():
        global marks
        clear_frame()
     
        def result7():
            global marks
    
            ans1=str(var.get())
            true="1"
            if(true==ans1):
                marks+=1
               
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="7). What will be the output of the following Python code snippet if x=1?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        lbl1=Label(root,text="x<<2",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a). 4",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).2",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).1",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).8",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn1=Button(root,text="submit",fg="black",bg="pink",command=result7,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn2=Button(root,text="next",fg="black",bg="pink",command=question8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
      
    def question8():
        global marks
        clear_frame()
        def result8():
            global marks

            ans1=str(var.get())
            true="3"
            if(true==ans1):
                marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="8).Which of the following is true for variable names in Python?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).underscore and ampersand are the only two special characters allowed",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).unlimited length",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c).all private members must have leading and trailing underscores",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d).none of the mentioned",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)


        btn1=Button(root,text="submit",fg="black",bg="pink",command=result8,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn1=Button(root,text="next",fg="black",bg="pink",command=question9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question9():
        global marks
        clear_frame()
        def result9():
            global marks

            ans1=str(var.get())
            true="2"
            if(true==ans1):
                marks+=1
            else:
                 marks
        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="9). What is the result of logical or relational expression in C?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a) True or False",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b) 0 or 1",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c) 0 if an expression is false and any positive number if an expression is true",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d) None of the mentioned",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn1=Button(root,text="submit",fg="black",bg="pink",command=result9,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
        btn1=Button(root,text="next",fg="black",bg="pink",command=question10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
    def question10():
        global marks
        clear_frame()
        
        def result10():
            global marks     
   
            ans1=str(var.get())
            true="2"
            if(true==ans1):
               marks+=1
            else:
                marks
            show_result()
            

        var=IntVar()
        clear_frame()
        lbl1=Label(root,text="10).Which of the following functions is a built-in function in python?",anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)

        r1=Radiobutton(root,text="a).factorial()",variable=var,value=1,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r2=Radiobutton(root,text="b).print()",variable=var,value=2,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r3=Radiobutton(root,text="c). seed()",variable=var,value=3,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)
        r4=Radiobutton(root,text="d). sqrt()",variable=var,value=4,anchor="center",font=('Copperplate Gothic Light',10)).pack(padx=2,pady=2)

        btn=Button(root,text="submit",fg="black",bg="pink",command=result10,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
       
    
    btn1=Button(root,text="START",fg="black",bg="pink",command=question1,anchor="center",font=('Copperplate Gothic Light',15)).pack(padx=2,pady=2)
   

lbl=Label(root,text="STUDENT EXAM PORTAL",bg="black",fg="orange",font=('Copperplate Gothic Light',20),anchor="center").pack(pady=4,padx=4)
btn=Button(root,text="CLICK TO START",bg="blue",fg="black",font=('Copperplate Gothic Light',20),anchor="center",command=start).pack(pady=4,padx=4)


    


root.mainloop()
