import tkinter as tk
import tkinter.font as tkFont
import config, alertMessage as alert
import connectDB, passwordCheck, menu

def mainFrame(root):
    frame = tk.Frame(root, background=config.colorBackground)
    
    def generateUI():
        global imgFrame, entryUsername, entryPassword, btnLogin, username_entry, password_entry
        username_entry, password_entry = tk.StringVar(), tk.StringVar()
        imgFrame = tk.PhotoImage(file="assets/pages/page_authentication.png")
        frameBG = tk.Label(frame, image=imgFrame)
        frameBG.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
        
        entryUsername = tk.Entry(frame,
                                justify="left",
                                relief="raised",
                                background=config.colorWhite,
                                foreground=config.colorBlack,
                                textvariable=username_entry,
                                font=tkFont.Font(family=config.fontDefault, size=13)
        )
        entryUsername.place(x=445, y=303, width=391, height=35)
        
        entryPassword = tk.Entry(frame,
                                show="*",
                                justify="left",
                                relief="raised",
                                background=config.colorWhite,
                                foreground=config.colorBlack,
                                textvariable=password_entry,
                                font=tkFont.Font(family=config.fontDefault, size=13)
        )
        entryPassword.place(x=445, y=395, width=391, height=35)
        
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
                            font=tkFont.Font(family=config.fontDefault, size=14),
                            command=lambda: checkLogin(entryUsername.get(), entryPassword.get())
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

    def checkLogin(username, password):
        if len(username) == 0 and len(password) == 0:
            alert.login_error(1)
            entryUsername.focus_force()
        elif len(username) == 0:
            alert.login_error(2)
            entryUsername.focus_force()
        elif len(password) == 0:
            alert.login_error(3)
            entryPassword.focus_force()
        else:
            sql = "SELECT * FROM user WHERE username = '{}'".format(username)
            userData = connectDB.queryDatabase(sql)
            if len(userData) > 1:
                alert.login_error(0, len(userData))
                username_entry.set("")
                password_entry.set("")
                entryUsername.focus_force()
            elif len(userData) == 0:
                alert.login_error(4)
                entryUsername.focus_force()
                entryUsername.select_range(0, tk.END)
                entryUsername.icursor(tk.END)
                password_entry.set("")
            else:
                userInfo = {}
                for i in range(len(userData[0])):
                    if i == 0:
                        userInfo["emp_id"] = userData[0][i]
                    elif i == 1:
                        userInfo["username"] = userData[0][i]
                    elif i == 2:
                        userInfo["password"] = userData[0][i]
                    elif i == 3:
                        userInfo["status"] = userData[0][i]
                    elif i == 4:
                        userInfo["last_login"] = userData[0][i]
                loginStatus = passwordCheck.check(username, password, userInfo)
                if loginStatus == 1:
                    alert.login_success(userInfo['username'])
                    frame.destroy()
                    menu_frame = menu.mainFrame(root, userInfo)
                    menu_frame.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
                elif loginStatus == 2:
                    # TODO: Call function to change password
                    pass
                elif loginStatus == 3:
                    alert.login_error(5)
                    entryUsername.focus_force()
                    entryUsername.select_range(0, tk.END)
                    entryUsername.icursor(tk.END)
                    password_entry.set("")
                else:
                    alert.login_error(4)
                    entryUsername.focus_force()
                    entryUsername.select_range(0, tk.END)
                    entryUsername.icursor(tk.END)
                    password_entry.set("")
   
   
    generateUI()
    entryUsername.focus_force()
    entryUsername.bind("<Return>", lambda event: checkLogin(entryUsername.get(), entryPassword.get()))
    entryPassword.bind("<Return>", lambda event: checkLogin(entryUsername.get(), entryPassword.get()))
    btnLogin.bind("<Return>", lambda event: checkLogin(entryUsername.get(), entryPassword.get()))
    return frame

if __name__ == "__main__":
    import main
    main.mainWindow()