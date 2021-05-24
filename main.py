from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1400x700+0+0")

        #-----------------VARIABLES-----------------------------------
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var= StringVar()
        self.laterdatefine_var = StringVar()
        self.dateoverdue_var = StringVar()



        lbtitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="black", bd=20, relief=RIDGE,
                        font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbtitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1270, height=350)

        # ----------------------DATA FRAME LEFT---------------------------
        DataFrameLeft = LabelFrame(frame, text="Library Membership information", bg="powder blue", fg="black", bd=12,
                                   relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameLeft.place(x=0, y=5, width=760, height=320)

        lblMember = Label(DataFrameLeft, bg="powder blue",text="Member Type :", font=("arial", 11, "bold"),
                          padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, textvariable = self.member_var,font=("arial", 11, "bold"), width=27,state = "readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_NO = Label(DataFrameLeft, bg="powder blue",text="USN No. :", font=("arial", 11, "bold"),
                          padx=2, pady=6)
        lblPRN_NO.grid(row=1, column=0, sticky=W)

        txtPRN_NO = Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable = self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle = Label(DataFrameLeft, font =("arial",11,"bold"),text="Mail ID :",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle = Entry(DataFrameLeft,font=("arial",11,"bold"),textvariable =self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstname = Label(DataFrameLeft, font=("arial", 11, "bold"), text="FirstName :", padx=2, pady=6,
                             bg="powder blue")
        lblFirstname.grid(row=3, column=0, sticky=W)
        txtFirstname = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.firstname_var,width=29)
        txtFirstname.grid(row=3, column=1)

        lblLastname = Label(DataFrameLeft, font=("arial", 11, "bold"),text="LastName :", padx=2, pady=6,
                             bg="powder blue")
        lblLastname.grid(row=4, column=0, sticky=W)
        txtLastname = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.lastname_var,width=29)
        txtLastname.grid(row=4, column=1)

        lbladdress1 = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Address :", padx=2, pady=6,
                            bg="powder blue")
        lbladdress1.grid(row=5, column=0, sticky=W)
        txtaddress1 = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.address,width=29)
        txtaddress1.grid(row=5, column=1)


        lblpostcode = Label(DataFrameLeft, font=("arial", 11, "bold"),text="Post Code :", padx=2, pady=6,
                            bg="powder blue")
        lblpostcode.grid(row=6, column=0, sticky=W)
        txtpostcode = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.postcode_var, width=29)
        txtpostcode.grid(row=6, column=1)

        lblMobile = Label(DataFrameLeft, font=("arial", 11, "bold"),text="Mobile no :", padx=2, pady=6,
                            bg="powder blue")
        lblMobile.grid(row=7, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.mobile_var,width=29)
        txtMobile.grid(row=7, column=1)

        lblBookid = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Book ID :", padx=2, pady=6,
                          bg="powder blue")
        lblBookid.grid(row=0, column=2, sticky=W)
        txtBookid = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.bookid_var,width=29)
        txtBookid.grid(row=0, column=3)

        lblBooktitle = Label(DataFrameLeft, font=("arial", 11, "bold"),text="Book Title :", padx=2, pady=6,
                          bg="powder blue")
        lblBooktitle.grid(row=1, column=2, sticky=W)
        txtBooktitle = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.booktitle_var,width=29)
        txtBooktitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, font=("arial", 11, "bold"),text="Author :", padx=2, pady=6,
                             bg="powder blue")
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial", 11, "bold"),textvariable=self.author_var, width=29)
        txtAuthor.grid(row=2, column=3)

        lblDateborrowed = Label(DataFrameLeft, font=("arial", 11, "bold"),text="Date Borrowed :", padx=2, pady=6,
                          bg="powder blue")
        lblDateborrowed.grid(row=3, column=2, sticky=W)
        txtDateborrowed = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable = self.dateborrowed_var,width=29)
        txtDateborrowed.grid(row=3, column=3)

        lblDatedue = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Date Due :", padx=2, pady=6,
                                bg="powder blue")
        lblDatedue.grid(row=4, column=2, sticky=W)
        txtDatedue = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable= self.datedue_var,width=29)
        txtDatedue.grid(row=4, column=3)

        lblDaysonBook = Label(DataFrameLeft, font=("arial", 11, "bold"), text="Days On Book :", padx=2, pady=6,
                           bg="powder blue")
        lblDaysonBook.grid(row=5, column=2, sticky=W)
        txtDaysonBook = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable= self.daysonbook_var,width=29)
        txtDaysonBook.grid(row=5, column=3)

        lbllatereturn = Label(DataFrameLeft, font=("arial", 11, "bold"), padx=2, pady=6,text="Late Fine :",bg="powder blue")
        lbllatereturn.grid(row=6, column=2, sticky=W)
        txtlatereturn = Entry(DataFrameLeft, font=("arial", 11, "bold"),textvariable = self.laterdatefine_var, width=29)
        txtlatereturn.grid(row=6, column=3)

        lbldateoverdue = Label(DataFrameLeft, font=("arial", 11, "bold"),text="Date Over Due :", padx=2, pady=6,
                              bg="powder blue")
        lbldateoverdue.grid(row=7, column=2, sticky=W)
        txtdateoverdue = Entry(DataFrameLeft, font=("arial", 11, "bold"), textvariable= self.dateoverdue_var,width=29)
        txtdateoverdue.grid(row=7, column=3)




        #-------------------------Data Frame Right-------------------------------------------





        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="black", bd=12,
                                    relief=RIDGE, font=("times new roman", 15, "bold"))
        DataFrameRight.place(x=766, y=5, width=460, height=320)

        self.txtBox = Text(DataFrameRight,font=("arial",11,"bold"),width = 35,height = 15,padx=2,pady=5)
        self.txtBox.grid(row = 0,column =2)
        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")
        listBooks = ['Python','Advance java','Data Structures','Algorithms','Let us C','Learn C++','Database Management System','Computer Networks','Operating Systems','Learn SQL','Web Development','Unix System','Machine Learning','Artificial Intelligence','MongoDB','Green Computing','Android Development','Learn Kotlin','Discrete Mathematics','Graph Theory','Digital Marketing']

        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x == "Python"):
                self.bookid_var.set("BKIDPYTHON001")
                self.booktitle_var.set("Head First Python")
                self.author_var.set("Paul barry")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")
            if (x == "Advance java"):
                self.bookid_var.set("BKIDADJAVA002")
                self.booktitle_var.set("Effective JAVA")
                self.author_var.set("Joshua Bloch")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")
            if (x == "Data Structures"):
                self.bookid_var.set("BKIDDS003")
                self.booktitle_var.set("Data Structures made easy")
                self.author_var.set("Narasimha Karumanchi")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")
            if (x == "Algorithms"):
                self.bookid_var.set("BKIDALGO004")
                self.booktitle_var.set("Introduction to Algorithms")
                self.author_var.set("C.L.R.S")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")
            if (x == "Let us C"):
                self.bookid_var.set("BKIDLETUSC005")
                self.booktitle_var.set("Let us C")
                self.author_var.set("Yashavant Kanetkar")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Learn C++"):
                self.bookid_var.set("BKIDLEARNC++006")
                self.booktitle_var.set("Thinking in C++")
                self.author_var.set("Bruce Eckel")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Database Management System"):
                self.bookid_var.set("BKIDDBMS007")
                self.booktitle_var.set("Fundamentals Of DBMS")
                self.author_var.set("Ramez Elmasri")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Computer Networks"):
                self.bookid_var.set("BKIDCNET008")
                self.booktitle_var.set("Computer Networks")
                self.author_var.set("Tanenbaum,Wetherall")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Operating Systems"):
                self.bookid_var.set("BKIDOS009")
                self.booktitle_var.set("Operating System Concepts")
                self.author_var.set("Avi Silberschatz")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Learn SQL"):
                self.bookid_var.set("BKIDSQL0010")
                self.booktitle_var.set("SQL Cookbook")
                self.author_var.set("Anthony Molinaro")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Web Development"):
                self.bookid_var.set("BKIDWEBDEV0011")
                self.booktitle_var.set("Web Dev for beginners")
                self.author_var.set("Whitebelt Mastery")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Unix System"):
                self.bookid_var.set("BKIDUNIXSYS0012")
                self.booktitle_var.set("Learning the UNIX OS")
                self.author_var.set("Peek,Todino,Strang")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Machine Learning"):
                self.bookid_var.set("BKIDML0013")
                self.booktitle_var.set("Hands on ML")
                self.author_var.set("Aurelien Geron")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Artificial Intelligence"):
                self.bookid_var.set("BKIDAI0014")
                self.booktitle_var.set("AI a modern approach")
                self.author_var.set("Peter Norvig")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "MongoDB"):
                self.bookid_var.set("BKIDMONGO0015")
                self.booktitle_var.set("MongoDB in action")
                self.author_var.set("Kyle Banker")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Green Computing"):
                self.bookid_var.set("BKIDGC0016")
                self.booktitle_var.set("The Green Computing book")
                self.author_var.set("Wu-chun Feng")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Android Development"):
                self.bookid_var.set("BKIDANDEV0017")
                self.booktitle_var.set("Android Development")
                self.author_var.set("Philips,Stewart,Marsicano")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Learn Kotlin"):
                self.bookid_var.set("BKIDKOTLIN0018")
                self.booktitle_var.set("Kotlin in Action")
                self.author_var.set("Svetlana Isakova")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Discrete Mathematics"):
                self.bookid_var.set("BKIDDM0019")
                self.booktitle_var.set("Discrete Mathematics")
                self.author_var.set("Kenneth H.Rosen")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Graph Theory"):
                self.bookid_var.set("BKIDGT0020")
                self.booktitle_var.set("Graph theory with applications")
                self.author_var.set("John Adrian Bondy")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")

            if (x == "Digital Marketing"):
                self.bookid_var.set("BKIDDMA0021")
                self.booktitle_var.set("Digital Marketing for dummies")
                self.author_var.set("Ryan deiss")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.laterdatefine_var.set("Rs 50")
                self.dateoverdue_var.set("NO")






        listBox =Listbox(DataFrameRight, font=("arial", 11 ,"bold"), width = 15, height=15)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)




        # ---------------BUTTONS FRAME-----------------------------

        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=480, width=1270, height=50)

        btnAddData = Button(framebutton, command = self.add_data,text="Add Data",font =("arial",11,"bold"),width=20,bg="red",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData = Button(framebutton, command = self.showData,text="Show Data", font=("arial", 11, "bold"), width=25, bg="red", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(framebutton, command=self.update,text="Update", font=("arial", 11, "bold"), width=25, bg="red", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(framebutton, command = self.delete,text="Delete", font=("arial", 11, "bold"), width=20, bg="red", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(framebutton, command = self.reset,text="Reset", font=("arial", 11, "bold"), width=20, bg="red", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(framebutton, command = self.isExit,text="Exit", font=("arial", 11, "bold"), width=17, bg="red", fg="white")
        btnAddData.grid(row=0, column=5)

        # ---------------INFORMATION FRAME-----------------------------

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=530, width=1270, height=190)


        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=1,width=1210,height=100)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame,column=("membertype","Usnno.","Mailid","FirstName","LastName","Address","Postid","Mobile","Bookid","Booktitle","Author","Dateborrowed","Datedue","Days","LateFine","Dateoverdue"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("Usnno.", text="USN No.")
        self.library_table.heading("Mailid", text="Mail ID")
        self.library_table.heading("FirstName", text="First Name")
        self.library_table.heading("LastName", text="Last Name")
        self.library_table.heading("Address", text="Address")
        self.library_table.heading("Postid", text="Post ID")
        self.library_table.heading("Mobile", text="Mobile")
        self.library_table.heading("Bookid", text="Book ID")
        self.library_table.heading("Booktitle", text="Book title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("Dateborrowed", text="Borrow date")
        self.library_table.heading("Datedue", text="Due date")
        self.library_table.heading("Days", text="DaysOnBook")
        self.library_table.heading("LateFine", text="LateFine")
        self.library_table.heading("Dateoverdue", text="Dateoverdue")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("Usnno.", width=100)
        self.library_table.column("Mailid", width=100)
        self.library_table.column("FirstName", width=100)
        self.library_table.column("LastName", width=100)
        self.library_table.column("Address", width=100)
        self.library_table.column("Postid", width=100)
        self.library_table.column("Mobile", width=100)
        self.library_table.column("Bookid", width=100)
        self.library_table.column("Booktitle", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("Dateborrowed", width=100)
        self.library_table.column("Datedue", width=100)
        self.library_table.column("Days", width=100)
        self.library_table.column("LateFine", width=100)
        self.library_table.column("Dateoverdue", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="ananya",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                           self.member_var.get(),
                                                                                                           self.prn_var.get(),
                                                                                                           self.id_var.get(),
                                                                                                           self.firstname_var.get(),
                                                                                                           self.lastname_var.get(),
                                                                                                           self.address.get(),
                                                                                                           self.postcode_var.get(),
                                                                                                           self.mobile_var.get(),
                                                                                                           self.booktitle_var.get(),
                                                                                                           self.bookid_var.get(),
                                                                                                           self.author_var.get(),
                                                                                                           self.dateborrowed_var.get(),
                                                                                                           self.datedue_var.get(),
                                                                                                           self.daysonbook_var.get(),
                                                                                                           self.laterdatefine_var.get(),
                                                                                                           self.datedue_var.get()
                                                                                                         ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","member has been inserted successfully")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ananya", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address=%s,Postid=%s,Mobile=%s,Booktitle=%s,Bookid=%s,Author=%s,Databorrowed=%s,datedue=%s,daysofbook=%s,latereturnfine=%s,dateoverdue=%s where PRN_NO=%s",(
                                                                                                  self.member_var.get(),
                                                                                                  self.id_var.get(),
                                                                                                  self.firstname_var.get(),
                                                                                                  self.lastname_var.get(),
                                                                                                  self.address.get(),
                                                                                                  self.postcode_var.get(),
                                                                                                  self.mobile_var.get(),
                                                                                                  self.booktitle_var.get(),
                                                                                                  self.bookid_var.get(),
                                                                                                  self.author_var.get(),
                                                                                                  self.dateborrowed_var.get(),
                                                                                                  self.datedue_var.get(),
                                                                                                  self.daysonbook_var.get(),
                                                                                                  self.laterdatefine_var.get(),
                                                                                                  self.dateoverdue_var.get(),
                                                                                                  self.prn_var.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success","Member has been Updated")





    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",username="root",password="ananya",database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address.set(row[5]),
        self.postcode_var.set(row[6]),
        self.mobile_var.set(row[7]),
        self.bookid_var.set(row[8]),
        self.booktitle_var.set(row[9]),
        self.author_var.set(row[10]),
        self.dateborrowed_var.set(row[11]),
        self.datedue_var.set(row[12]),
        self.daysonbook_var.set(row[13]),
        self.laterdatefine_var.set(row[14]),
        self.dateoverdue_var.set(row[15])

    def showData(self):
        self.txtBox.insert(END,"Member Type :\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END, "USN No. :\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "Mail ID :\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name :\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Last Name :\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address :\t" + self.address.get() + "\n")
        self.txtBox.insert(END, "Post ID :\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile :\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID :\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book title :\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author :\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END, "Borrow date :\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Due date :\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook :\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "Late Fine :\t" + self.laterdatefine_var.get() + "\n")
        self.txtBox.insert(END, "Dateoverdue :\t" + self.dateoverdue_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.laterdatefine_var.set("")
        self.dateoverdue_var.set("")
        self.txtBox.delete("1.0",END)

    def isExit(self):
        isExit = tkinter.messagebox.askyesno("Library Management System","Do you want to exit ?")
        if isExit > 0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="ananya",database="mydata")
            my_cursor=conn.cursor()
            query = "delete from library where PRN_NO=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been deleted")





















if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagement(root)
    root.mainloop()