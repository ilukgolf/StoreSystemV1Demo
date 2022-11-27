import mysql.connector
from mysql.connector import errorcode
import csv
import alertMessage as alert

_db = {}
def connectDatabase():
    with open('assets/backend/dbinfo.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            _db.setdefault(row[0], row[1])     
    try:
        conn = mysql.connector.connect(
            host = _db['mysqlServer'],
            user = _db['Username'],
            password = _db['Password'],
            database = _db['databaseTable']
        )
        return conn
    except mysql.connector.Error as err:
        alert.databaseError(err.errno, _db)
        return False

def checkConnection():
    if connectDatabase():
        return True
    else:
        return False

def queryDatabase(query):
    if checkConnection():
        conn = connectDatabase()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    else:
        return False
    
if __name__ == '__main__':
    import main
    main.mainWindow()