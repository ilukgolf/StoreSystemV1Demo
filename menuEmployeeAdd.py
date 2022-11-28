import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import config, alertMessage as alert
import connectDB

def mainFrame(root, userInfo):
    frame = tk.Frame(root, background=config.colorBackground)
    
    def generateUI():
        global imgFrame, imgUser, entryNameTH, entryNameEN, entryThaiIdNumber, entryGender
        global entryAddress, entryPhoneNumber, entryEmail, entryHireDate, entryDathOfBirth
        imgFrame = tk.PhotoImage(file="assets/pages/page_employee_add.png")
        imgUser = tk.PhotoImage(file="assets/pages/unknownUser.png")
        frameBG = tk.Label(frame, image=imgFrame)
        frameBG.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
        
        btnReturn = tk.Button(frame,
                            text="กลับ",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorLightGary,
                            foreground=config.colorBlack,
                            activebackground=config.colorRed,
                            activeforeground=config.colorWhite,
                            font=tkFont.Font(family=config.fontDefault, size=14),
                            command=lambda: btnReturnClick()
        )
        btnReturn.place(x=26, y=14, width=66, height=45)

        entryNameTH = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryNameTH.place(x=413, y=119, width=416, height=35)

        entryNameEN = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorWhite,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryNameEN.place(x=413, y=174, width=416, height=35)

        entryThaiIdNumber = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryThaiIdNumber.place(x=413, y=229, width=416, height=35)

        entryDathOfBirth = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryDathOfBirth.place(x=413, y=284, width=416, height=35)

        entryGender = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryGender.place(x=413, y=339, width=416, height=35)

        entryPhoneNumber = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryPhoneNumber.place(x=413, y=394, width=416, height=35)

        entryEmail = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryEmail.place(x=413, y=449, width=416, height=35)

        entryAddress = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryAddress.place(x=413, y=504, width=416, height=90)

        entryHireDate = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryHireDate.place(x=413, y=614, width=416, height=35)
        
        labelUserImg = tk.Label(frame, image=imgUser)
        labelUserImg.place(x=902, y=162, width=283, height=326)
        
        btnAdd = tk.Button(frame,
                            text="บันทึก",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorDarkBlue,
                            foreground=config.colorWhite,
                            activebackground=config.colorLightBlue,
                            activeforeground=config.colorWhite,
                            font=tkFont.Font(family=config.fontDefault, size=14),
                            command=lambda: btnAddClick()
        )
        btnAdd.place(x=909, y=641, width=120, height=36)
        
        btnCancel = tk.Button(frame,
                            text="ยกเลิก",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorRed,
                            foreground=config.colorWhite,
                            activebackground=config.colorDarkBlue,
                            activeforeground=config.colorWhite,
                            font=tkFont.Font(family=config.fontDefault, size=14),
                            command=lambda: btnReturnClick()
        )
        btnCancel.place(x=1060, y=641, width=120, height=36)
        
        labelDepartment = tk.Label(frame,
                                    text="ทดสอบ",
                                    anchor="center",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorFont,
                                    font=tkFont.Font(family=config.fontDefault, size=12)
        )
        labelDepartment.place(x=902, y=528, width=283, height=29)
        
        labelEmployeeID = tk.Label(frame,
                                    text="ทดสอบ",
                                    anchor="center",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorFont,
                                    font=tkFont.Font(family=config.fontDefault, size=12)
        )
        labelEmployeeID.place(x=902, y=578, width=283, height=29)
        
        entryNameTH.configure(text="Jirawat Bunmaraksasakul")
        
    def btnAddClick():
        sql = "SELECT * FROM employees ORDER BY emp_id DESC LIMIT 1"
        data = connectDB.queryDatabase(sql)
        print(data)
        # if entryNameTH.get() == "" and entryNameEN.get() == "" and entryThaiIdNumber.get() == "" and entryDathOfBirth.get() == "" and entryGender.get() == "" and entryPhoneNumber.get() == "" and entryEmail.get() == "" and entryAddress.get() == "" and entryHireDate.get() == "":
        #     alert.addEmployee()
        # else:
        #     newUserInfo = {}
        #     newUserInfo["gender"] = entryGender.get()
        #     newUserInfo["emp_fname_th"] = entryNameTH.get().split(" ")[0]
        #     newUserInfo["emp_lname_th"] = entryNameTH.get().split(" ")[1]
        #     newUserInfo["emp_fname_en"] = entryNameEN.get().split(" ")[0]
        #     newUserInfo["emp_lname_en"] = entryNameEN.get().split(" ")[1]
        #     newUserInfo["emp_thai_id_number"] = entryThaiIdNumber.get()
        #     newUserInfo["emp_date_of_birth"] = entryDathOfBirth.get()
        #     newUserInfo["emp_phone_number"] = entryPhoneNumber.get()
        #     newUserInfo["emp_email"] = entryEmail.get()
        #     newUserInfo["emp_address"] = entryAddress.get()
        #     newUserInfo["emp_hire_date"] = entryHireDate.get()
            
            
            
        #     sql = "INSERT INTO employee (emp_fname_th, emp_lname_th, emp_fname_en, emp_lname_en, emp_thai_id_number, emp_date_of_birth, emp_phone_number, emp_email, emp_address,"
                            
    def btnReturnClick():
        import menu
        print("- Frame: menuEmployeeAdd")
        frame.destroy()
        menu_frame = menu.mainFrame(root, userInfo)
        menu_frame.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
        print("+ Frame: menu")

    generateUI()
    return frame

if __name__ == "__main__":
    import main
    main.mainWindow()