import tkinter as tk
import tkinter.font as tkFont
import config, alertMessage as alert

def mainFrame(root):
    frame = tk.Frame(root, background=config.colorBackground)
    
    def generateUI():
        global imgFrame, imgUser
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
                            font=tkFont.Font(family=config.fontDefault, size=14)
        )
        btnReturn.place(x=26, y=14, width=66, height=45)

        entryNameTH = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryNameTH.place(x=428, y=121, width=412, height=31)

        entryNameEN = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorWhite,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryNameEN.place(x=428, y=174, width=412, height=31)

        entryThaiIdNumber = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryThaiIdNumber.place(x=428, y=229, width=412, height=31)

        entryDathOfBirth = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryDathOfBirth.place(x=428, y=284, width=412, height=31)

        entryGender = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryGender.place(x=428, y=339, width=412, height=31)

        entryPhomeNumber = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryPhomeNumber.place(x=428, y=394, width=412, height=31)

        entryEmail = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryEmail.place(x=428, y=449, width=412, height=31)

        entryAddress = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryAddress.place(x=428, y=504, width=412, height=90)

        entryHireDate = tk.Entry(frame,
                                    justify="left",
                                    relief="raised",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryHireDate.place(x=428, y=614, width=412, height=31)
        
        labelUserImg = tk.Label(frame, image=imgUser)
        labelUserImg.place(x=902, y=162, width=283, height=326)
        
        btnEdit = tk.Button(frame,
                            text="แก้ไข",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorDarkBlue,
                            foreground=config.colorWhite,
                            activebackground=config.colorLightBlue,
                            activeforeground=config.colorWhite,
                            font=tkFont.Font(family=config.fontDefault, size=14)
        )
        btnEdit.place(x=909, y=641, width=120, height=36)
        
        btnDelete = tk.Button(frame,
                            text="ลบ",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorRed,
                            foreground=config.colorWhite,
                            activebackground=config.colorDarkBlue,
                            activeforeground=config.colorWhite,
                            font=tkFont.Font(family=config.fontDefault, size=14)
        )
        btnDelete.place(x=1060, y=641, width=120, height=36)
        
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
                            

    generateUI()
    return frame

if __name__ == "__main__":
    import main
    main.mainWindow()