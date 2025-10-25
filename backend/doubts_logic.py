import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

def get_doubt_id():
    mydb.commit()
    cur.execute("select * from doubts")
    doubt_id = len(cur.fetchall())+1
    return doubt_id

def insert_doubt(user_id,doubt):
    doubt_id = get_doubt_id()
    cur.execute("insert into doubts values(%s,%s,%s)",(doubt_id,user_id,doubt))
    mydb.commit()

def get_username_role(user_id):
    cur.execute("select role from users where user_id = %s",(user_id,))
    role = cur.fetchall()[0][0]
    if role.lower() == 'student':
        cur.execute("select first_name from students where student_id = %s",(user_id,))
        name = cur.fetchall()[0][0]
        return (name,role)
    elif role.lower() == 'scholar':
        cur.execute("select first_name from scholars where scholar_id = %s",(user_id,))

def answer_doubt(user_id,doubt_id,solution):
    cur.execute("insert into solutions values(%s,%s,%s)",(doubt_id,user_id,solution))
    mydb.commit()

def get_all_doubts():
    cur.execute("select doubt_id,user_id,doubt from doubts")
    doubts = cur.fetchall()
    return doubts

def get_my_doubts(user_id):
    mydb.commit()
    cur.execute("select doubt_id,user_id,doubt from doubts where user_id = %s",(user_id,))
    doubts = cur.fetchall()
    return doubts

def get_solved_by_me(user_id):
    mydb.commit()
    cur.execute("select d.doubt_id,d.user_id,d.doubt from doubts d,solutions s where s.user_id = %s and d.doubt_id = s.doubt_id",(user_id,))
    doubts = cur.fetchall()
    return doubts


def get_solutions(doubt_id):
    cur.execute("select user_id,solution from solutions where doubt_id = %s",(doubt_id,))
    solver_ids = cur.fetchall()
    solvers = []
    for solver_id,solution in solver_ids:
        name,role = get_username_role(solver_id)
        solvers.append((solver_id,name,role,solution))
    return solvers

