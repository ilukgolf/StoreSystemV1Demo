import tkinter as tk
import tkinter.font as tkFont
import config, alertMessage as alert

def mainFrame(root):
    frame = tk.Frame(root, background=config.colorBackground)
    
    def generateUI():
        global imgFrame
        imgFrame = tk.PhotoImage(file="assets/pages/page_employee.png")
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

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

        entryFirstnameTH = tk.Label(frame,
                                    text="",
                                    anchor="w",
                                    relief="flat",
                                    background=config.colorLightGary,
                                    foreground=config.colorBlack,
                                    font=tkFont.Font(family=config.fontDefault, size=15)
        )
        entryFirstnameTH.place(x=428, y=121, width=412, height=31)

    generateUI()
    return frame

if __name__ == "__main__":
    import main
    main.mainWindow()