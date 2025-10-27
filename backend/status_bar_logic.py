import mysql.connector
mydb = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password = "1234")
cur = mydb.cursor()
cur.execute("use library")

def issued_books(user_id):
    cur.execute("select count(*) from issue_books where user_id = %s and status != 'Returned'",(user_id,))
    result = cur.fetchall()
    if len(result) == 0:
        return 0
    else:
        return result[0][0]
    
def total_issued_books():
    cur.execute("select count(*) from issue_books where status != 'Returned'")
    result = cur.fetchall()
    if len(result) == 0:
        return 0
    else:
        return result[0][0]

def reserved_books(user_id):
    cur.execute("select count(*) from reserve_books where user_id = %s",(user_id,))
    result = cur.fetchall()
    if len(result) == 0:
        return 0
    else:
        return result[0][0] 

def total_reserved_books():
    cur.execute("select count(*) from reserve_books")
    result = cur.fetchall()
    if len(result) == 0:
        return 0
    else:
        return result[0][0]   

def due_books(user_id):
    cur.execute("select count(*) from issue_books where user_id = %s and status = 'Due'",(user_id,))
    result = cur.fetchall()
    if len(result) == 0:
        return 0
    else:
        return result[0][0]  
    
def total_due_books():
    cur.execute("select count(*) from issue_books where status = 'Due'")
    result = cur.fetchall()
    if len(result) == 0:
        return 0
    else:
        return result[0][0] 
    
def pending_fine(user_id):
    query = """
        SELECT 
            SUM(GREATEST(DATEDIFF(CURDATE(), return_date), 0) * 5) AS total_fine
        FROM issue_books
        WHERE status = 'Due' AND user_id = %s;
    """
    cur.execute(query, (user_id,))
    result = cur.fetchone()
    if result[0] is None:
        return 0
    return result[0] 

def total_pending_fine():
    query = """
        SELECT 
            SUM(GREATEST(DATEDIFF(CURDATE(), return_date), 0) * 5) AS total_fine
        FROM issue_books
        WHERE status = 'Due';
    """
    cur.execute(query)
    result = cur.fetchone()
    if result[0] is None:
        return 0
    return result[0] 