from tkinter import messagebox as msg

def databaseError(errno, _db):
    msg.showerror('Database Error', 'MySQL Error Code: {:<35}\n\n{}'.format(errno, mySQL_error_code(errno, _db)))
    
def mySQL_error_code(errno, _db):
    if errno == 2005:
        return str("Unknown MySQL server host '{0}'".format(_db['mysqlServer']))
    elif errno == 1045:
        return str("Access denied for user '{0}'@'{1}'".format(_db['Username'], _db['mysqlServer']))
    elif errno == 1049:
        return str("Unknown database '{0}'".format(_db['databaseTable']))
    elif errno == 2003:
        return str("Can't connect to MySQL server on '{0}'".format(_db['mysqlServer']))

if __name__ == "__main__":
    import main
    main.mainWindow()