import tkinter as tk
import tkinter.font as tkFont
import config, alertMessage as alert

def mainFrame(root, userInfo):
    frame = tk.Frame(root, background=config.colorBackground)
    
    def generateUI():
        global imgFrame
        imgFrame = tk.PhotoImage(file="assets/pages/page_menu.png")
        frameBG = tk.Label(frame, image=imgFrame)
        frameBG.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)

        btnQuit = tk.Button(frame,
                            text="ออก",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorRed,
                            foreground=config.colorWhite,
                            activebackground=config.colorWhite,
                            activeforeground=config.colorBlack,
                            font=tkFont.Font(family=config.fontDefault, size=14),
                            command=lambda: btnQuitClick()
        )
        btnQuit.place(x=26, y=14, width=66, height=45)
        
        labelForgotEmployee = tk.Label(frame,
                                        text="พนักงาน",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=14)
        )
        labelForgotEmployee.place(x=179, y=26, width=106, height=27)
    
        labelForgotCustomer = tk.Label(frame,
                                        text="ลูกค้า",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=14)
        )
        labelForgotCustomer.place(x=308, y=26, width=106, height=27)
    
        labelForgotProduct = tk.Label(frame,
                                        text="สินค้า",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=14)
        )
        labelForgotProduct.place(x=437, y=26, width=106, height=27)
    
        labelForgotAgent = tk.Label(frame,
                                        text="ตัวแทน",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=14)
        )
        labelForgotAgent.place(x=566, y=26, width=106, height=27)
        
        labelForgotUserAccount = tk.Label(frame,
                                        text=userInfo['username'],
                                        anchor="center",
                                        foreground=config.colorWhite,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=14)
        )
        labelForgotUserAccount.place(x=1094, y=27, width=162, height=23)
        
        labelForgotfunctionUsed = tk.Label(frame,
                                        text="ชื่อฟังชัน\nที่กำลังใช้งาน",
                                        anchor="center",
                                        foreground=config.colorBlack,
                                        background=config.colorLightGary,
                                        font=tkFont.Font(family=config.fontDefault, size=24)
        )
        labelForgotfunctionUsed.place(x=53, y=99, width=209, height=97)

        entryfd = tk.Entry(frame,
                                justify="center",
                                relief="raised",
                                background=config.colorWhite,
                                foreground=config.colorBlack,
                                font=tkFont.Font(family=config.fontDefault, size=13)
        )
        entryfd.place(x=900, y=108, width=338, height=35)

        btnSearch = tk.Button(frame,
                            text="ค้นหา",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorDarkBlue,
                            foreground=config.colorWhite,
                            activebackground=config.colorLightBlue,
                            activeforeground=config.colorWhite,
                            font=tkFont.Font(family=config.fontDefault, size=13)
        )
        btnSearch.place(x=1148, y=162, width=90, height=36)
        
        btnAdd = tk.Button(frame,
                            text="เพิ่ม",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorDarkBlue,
                            foreground=config.colorWhite,
                            activebackground=config.colorLightBlue,
                            activeforeground=config.colorWhite,
                            font=tkFont.Font(family=config.fontDefault, size=13),
                            command=lambda: btnAddClick()
        )
        btnAdd.place(x=1045, y=162, width=90, height=36)
        
    def btnQuitClick():
        import authentication
        print("- Frame: menu")
        frame.destroy()
        auth_frame = authentication.mainFrame(root)
        auth_frame.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
        print("+ Frame: Authentication")
        
    def btnAddClick():
        import menuEmployeeAdd
        print("- Frame: menu")
        emp_frame = menuEmployeeAdd.mainFrame(root, userInfo)
        emp_frame.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
        print("+ Frame: menuEmployeeAdd")
        
    generateUI()
    return frame

if __name__ == "__main__":
    import main
    main.mainWindow()