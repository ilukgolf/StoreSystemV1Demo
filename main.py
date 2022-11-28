import tkinter as tk
import config, alertMessage as alert
import tkinter.font as tkFont

def mainWindow():
    
    def generateWindow():
        root = tk.Tk()
        windowXpos = int(root.winfo_screenwidth() / 2 - config.windowsWidth / 2)
        windowYpos = int(root.winfo_screenheight() / 2 - config.windowsHeight / 2)
        root.title(config.windowsTitle)
        root.geometry(f"{config.windowsWidth}x{config.windowsHeight}+{windowXpos}+{windowYpos}")
        root.resizable(config.windowsResizeable, config.windowsResizeable)
        root.iconbitmap(config.windowsLogo)
        root.configure(background=config.colorBackground)        
        return root
    
    def checkSqlConnection():
        import connectDB
        if connectDB.checkConnection():
            authenticationFunction()
        else:
            root.destroy()
        
    def authenticationFunction():   # TODO: EDIT TO authentication (now use to generate ui)
        import authentication as functionFrame
        frame = functionFrame.mainFrame(root)
        frame.place(x=0, y=0, width=config.windowsWidth, height=config.windowsHeight)
        print("+ Frame: Authentication")
        
    root = generateWindow()
    root.option_add("*Font", tkFont.Font(family=config.fontDefault, size=12))
    root.option_add("*OptionMenu", tkFont.Font(family=config.fontDefault, size=12))
    # checkSqlConnection()
    authenticationFunction()
    root.mainloop()
    
if __name__ == "__main__":
    mainWindow()