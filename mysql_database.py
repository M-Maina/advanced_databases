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
       
       
def add_new_project(cursor, project_title, project_description, task_description):
    project_data = (project_title, project_description)
    cursor.execute('''INSERT INTO projects(title, description)
                   VALUES(%S, %S)''', project_data)
    
    project_id = cursor.lastrowid
    tasks_data = []
    
    for description in tasks_descriptions:
        task_data = (project_id, description)
        tasks_data.append(task_data)
        
    cursor.executemany('''INSERT INTO tasks(project_id, description)
                       VALUES (%S %S)''', tasks_data)

if __name__=='__main__':
   db = connect("projects")
   cursor = db.cursor()
   
   tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
   add_new_project(cursor, "clean house", "Clean house by room", tasks)
   db.commit()
   
   cursor.execute("SELECT * FROM projects")
   project_records = cursor.fetchall()
   print(project_records)
   
   cursor.execute("SELECT * FROM tasks")
   tasks_records = cursor.fetchall()
   print(tasks_records)
   db.close()