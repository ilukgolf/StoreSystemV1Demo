import tkinter as tk
import tkinter.font as tkFont
import config, alertMessage as alert

def mainFrame(root):
    frame = tk.Frame(root, background=config.colorBackground)
    
    def generateUI():
        global imgFrame
        imgFrame = tk.PhotoImage(file="assets/pages/page_menu.png")
        frameBG = tk.Label(frame, image=imgFrame)
        frameBG.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)

        btnBack = tk.Button(frame,
                            text="กลับ",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorLightGary,
                            foreground=config.colorBlack,
                            activebackground=config.colorLime,
                            activeforeground=config.colorBlack,
                            font=tkFont.Font(family=config.fontDefault, size=24)
        )
        btnBack.place(x=26, y=14, width=66, height=45)
        
        labelForgotEmployee = tk.Label(frame,
                                        text="พนักงาน",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=16)
        )
        labelForgotEmployee.place(x=179, y=26, width=106, height=27)
    
        labelForgotCustomer = tk.Label(frame,
                                        text="ลูกค้า",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=16)
        )
        labelForgotCustomer.place(x=308, y=26, width=106, height=27)
    
        labelForgotProduct = tk.Label(frame,
                                        text="สินค้า",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=16)
        )
        labelForgotProduct.place(x=437, y=26, width=106, height=27)
    
        labelForgotAgent = tk.Label(frame,
                                        text="ตัวแทนจัดจำหน่าย",
                                        cursor="hand2",
                                        anchor="center",
                                        foreground=config.colorYellow,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=16)
        )
        labelForgotAgent.place(x=566, y=26, width=106, height=27)
        
        labelForgotUserAccount = tk.Label(frame,
                                        text="ชื่อบัญชีผู้ใช้งาน",
                                        anchor="center",
                                        foreground=config.colorWhite,
                                        background=config.colorBackground,
                                        font=tkFont.Font(family=config.fontDefault, size=16)
        )
        labelForgotUserAccount.place(x=1094, y=27, width=162, height=21)
        
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

        btnName = tk.Button(frame,
                            text=" ",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background="#2D394E",
                            foreground=config.colorWhite,
                            activebackground=config.colorLime,
                            activeforeground=config.colorBlack,
                            font=tkFont.Font(family=config.fontDefault, size=10)
        )
        btnName.place(x=1148, y=162, width=90, height=36)
        
        btnName2 = tk.Button(frame,
                            text=" ",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background="#2D394E",
                            foreground=config.colorWhite,
                            activebackground=config.colorLime,
                            activeforeground=config.colorBlack,
                            font=tkFont.Font(family=config.fontDefault, size=10)
        )
        btnName2.place(x=1045, y=162, width=90, height=36)

    generateUI()
    return frame

if __name__ == "__main__":
    import main
    main.mainWindow()