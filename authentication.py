import tkinter as tk
import tkinter.font as tkFont
import config, alertMessage as alert

def mainFrame(root):
    frame = tk.Frame(root, background=config.colorBackground)
    
    def generateUI():
        global imgFrame
        imgFrame = tk.PhotoImage(file="assets/pages/page_authentication.png")
        frameBG = tk.Label(frame, image=imgFrame)
        frameBG.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
        
        entryUsername = tk.Entry(frame,
                                justify="left",
                                relief="raised",
                                background=config.colorWhite,
                                foreground=config.colorBlack,
                                font=tkFont.Font(family=config.fontDefault, size=13)
        )
        entryUsername.place(x=445, y=303, width=391, height=35)
        
        entryPasword = tk.Entry(frame,
                                show="*",
                                justify="left",
                                relief="raised",
                                background=config.colorWhite,
                                foreground=config.colorBlack,
                                font=tkFont.Font(family=config.fontDefault, size=13)
        )
        entryPasword.place(x=445, y=395, width=391, height=35)
        
        btnLogin = tk.Button(frame,
                            text="เข้าสู่ระบบ",
                            cursor="hand2",
                            justify="center",
                            relief="raised",
                            border=0,
                            borderwidth=0,
                            background=config.colorBackground,
                            foreground=config.colorWhite,
                            activebackground=config.colorLime,
                            activeforeground=config.colorBlack,
                            font=tkFont.Font(family=config.fontDefault, size=14)
        )
        btnLogin.place(x=519, y=497, width=243, height=37)
        
        labelForgotPassword = tk.Label(frame,
                                        text="ลืมรหัสผ่าน?",
                                        cursor="hand2",
                                        justify="center",
                                        foreground=config.colorFont,
                                        background=config.colorLightGary,
                                        font=tkFont.Font(family=config.fontDefault, size=12)
        )
        labelForgotPassword.place(x=519, y=559, width=243, height=23)

    generateUI()
    return frame

if __name__ == "__main__":
    import main
    main.mainWindow()