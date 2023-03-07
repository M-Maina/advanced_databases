import mysql.connector as mysql

#function to call the database 
def connect(db_name):
    try:
       return mysql.connect(
        host='localhost', 
        user='root',
        password='Tronic@123',
        database=db_name)
    except Error as e:
       print(e)

if __name__=='__main__':
   db = connect("projects")
   cursor = db.cursor()
   
   cursor.execute("SELECT * FROM projects")
   project_records = cursor.fetchall()
   print(project_records)
   db.close()