import tkinter
from tkinter import messagebox
from tkinter import ttk
import sqlite3

def entry():

    Accepted = TermsCheckVariable.get()

    if Accepted == "YES":
        
    #Personal Info fetcher
        First = FirstNameEntry.get()
        Last = LastNameEntry.get()
        if First and Last:
            
            Title = TitleDrop.get()
            Age = AgeSpinner.get()
            Nationality = NationalityDrop.get()
            Register = RegisterCheckVariable.get()

            #Course and Semester info fetcher
            NumCourse = NumCourseSpinner.get()
            NumSemester = NumSemSpinner.get()
                
            con = sqlite3.connect('UserInfoGui#2.db')
            c = con.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS Information (first text, last text, title text, age integer,nationality text, registrationstatus text,completedsemesters integer, completedcourses integer) """)
            con.commit()

            c.execute("INSERT INTO Information VALUES(?,?,?,?,?,?,?,?)",
                          [First, Last, Title, Age, Nationality, Register,
                           NumCourse, NumSemester])

                #c.execute("INSERT INTO GuiInfo VALUES(:first,:last,:title,:age,:nationality,:completedcourses,:completedsemesters, :registrationstatus)")
            con.commit()

            c.execute("SELECT * FROM Information WHERE age >= 1 ")
            print(c.fetchall())

            con.commit()
            con.close()
                
        else:
            tkinter.messagebox.showwarning(title ="Error", message = "Enter First and Last Names")
    else:
        tkinter.messagebox.showwarning(title = "Error", message = "Please accept the Terms and Conditions to continue")
window = tkinter.Tk()
window.title("Information Collector")

frame = tkinter.Frame(window)
frame.pack()

####################  \/  THIS SECTION IS THE FRAMES AND WIDGETS  \/   ####################
#1st Label Frame
UserInfoFrame =tkinter.LabelFrame(frame, text = "User Information")
UserInfoFrame.grid(row = 0 , column = 0, padx = 20, pady = 10)

FirstNameLabel = tkinter.Label(UserInfoFrame, text = "First Name")
FirstNameLabel.grid(row = 0, column = 0, padx = 10, pady = 5)

LastNameLabel = tkinter.Label(UserInfoFrame, text = "Last Name")
LastNameLabel.grid(row = 0, column =1, padx = 10, pady = 5)

FirstNameEntry = tkinter.Entry(UserInfoFrame)
FirstNameEntry.grid(row = 1, column = 0, padx = 10, pady = 5)

LastNameEntry = tkinter.Entry(UserInfoFrame)
LastNameEntry.grid(row = 1, column = 1, padx = 10, pady = 5)

TitleLabel= tkinter.Label(UserInfoFrame, text = "Title")
TitleDrop = ttk.Combobox(UserInfoFrame, values = ["Mr.", "Mrs.", "Ms.", "Dr.","Prof.",])
TitleLabel.grid(row = 0, column = 2, padx = 10, pady = 5)
TitleDrop.grid(row = 1, column = 2, padx = 10, pady = 5)


AgeLabel = tkinter.Label (UserInfoFrame, text = "Age")
AgeSpinner = tkinter.Spinbox(UserInfoFrame, from_ = 1, to = 110)
AgeLabel.grid(row = 2, column = 0, padx = 10, pady = 5)
AgeSpinner.grid(row = 3, column = 0, padx = 10, pady = 5)


NationalityLabel = tkinter.Label(UserInfoFrame, text = "Nationality")
NationalityDrop = ttk.Combobox(UserInfoFrame, values = ["Asia", "Africa", "North America", "South America", "Antarctica", "Europe", "Australia"])
NationalityLabel.grid(row = 2, column = 1)
NationalityDrop.grid(row = 3, column = 1)


#2nd Label Frame
CoursesFrame = tkinter.LabelFrame(frame)
CoursesFrame.grid(row = 1, column = 0, sticky = "NEWS", padx = 20, pady = 10)

    #Make Check box a String Var to be able to .get()
RegisterCheckVariable = tkinter.StringVar(value = "Not Registered")

RegisterLabel = tkinter.Label(CoursesFrame, text = "Registration Status")
RegisteredChecker = tkinter.Checkbutton(CoursesFrame, text = "Registered", variable = RegisterCheckVariable, onvalue = "Registered", offvalue = "Not Registered")
RegisterLabel.grid(row = 0, column = 0, padx = 10, pady = 5)
RegisteredChecker.grid(row = 1, column = 0, padx = 10, pady = 5)

NumCourseLabel = tkinter.Label(CoursesFrame, text = "Completed Courses")
NumCourseSpinner = tkinter.Spinbox(CoursesFrame, from_ = 0, to = 10000)
NumCourseLabel.grid(row = 0, column = 1, padx = 10, pady = 5)
NumCourseSpinner.grid(row = 1, column = 1, padx = 10, pady = 5)


NumSemLabel = tkinter.Label(CoursesFrame, text = "Completed Semesters")
NumSemSpinner = tkinter.Spinbox(CoursesFrame, from_ = 0, to = 10000)
NumSemLabel.grid(row = 0, column = 2, padx = 10, pady = 5)
NumSemSpinner.grid(row = 1, column = 2, padx = 10, pady = 5)

#3rd Label Frame
TermsFrame = tkinter.LabelFrame(frame, text = "Terms and Conditions")
TermsFrame.grid(row=2, column = 0, sticky = "NEWS", padx = 20, pady = 20)

TermsCheckVariable = tkinter.StringVar(value = "Did not accept Terms and Conditions")

TermsCheck = tkinter.Checkbutton (TermsFrame, text = "I accept all of the Terms and Conditions", variable = TermsCheckVariable, onvalue = "YES", offvalue = "NO") 
TermsCheck.grid(row = 0, column = 0)


Enter = tkinter.Button(frame, text = "Enter", command= entry)
Enter.grid(row = 3, column = 0, sticky = "NEWS", padx = 20, pady =10)


                           
####################  /\  THIS SECTION IS THE FRAMES AND WIDGETS   /\  ####################





window.mainloop()
