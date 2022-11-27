from tkinter import messagebox as msg

def databaseError(errno, _db):
    msg.showerror('ฐานข้อมูลผิดพลาด', 'MySQL Error Code: {:<35}\n\n{}'.format(errno, mySQL_error_code(errno, _db)))
    
def mySQL_error_code(errno, _db):
    if errno == 2005:
        return str("Unknown MySQL server host '{0}'".format(_db['mysqlServer']))
    elif errno == 1045:
        return str("Access denied for user '{0}'@'{1}'".format(_db['Username'], _db['mysqlServer']))
    elif errno == 1049:
        return str("Unknown database '{0}'".format(_db['databaseTable']))
    elif errno == 2003:
        return str("Can't connect to MySQL server on '{0}'".format(_db['mysqlServer']))

def login_success(user):
    msg.showinfo("เข้าสู่ระบบสำเร็จ", "ยินดีต้อนรับคุณ %s เข้าสู่ระบบ" % (user))
    
def login_error(code, user = None):
    if code == 0:
        msg.showerror("เกิดข้อผิดพลาด", "พบข้อมูลผู้ใช้จำนวน %s รายการซ้ำภายในระบบ\nกรุณาติดต่อผู้ดูแลระบบ" % (user))
    elif code == 1:
        msg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "{:<35}".format("กรุณากรอกชื่อผู้ใช้ และรหัสผ่านให้ครบถ้วน"))
    elif code == 2:
        msg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "{:<35}".format("กรุณากรอกชื่อผู้ใช้"))
    elif code == 3:
        msg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "{:<35}".format("กรุณากรอกรหัสผ่าน"))
    elif code == 4:
        msg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "{:<35}".format("ชื่อผู้ใช้งาน หรือรหัสผ่านไม่ถูกต้อง"))
    elif code == 5:
        msg.showwarning("เข้าสู่ระบบไม่สำเร็จ", "{:<35}".format("บัญชีถูกระงับการใช้งาน กรุณาติดต่อผู้ดูแลระบบ"))
    else:
        msg.showerror("เกิดข้อผิดพลาด", "{:<35}".format("เกิดข้อผิดพลาดที่ไม่รู้จัก กรุณาติดต่อผู้ดูแลระบบ"))

if __name__ == "__main__":
    import main
    main.mainWindow()