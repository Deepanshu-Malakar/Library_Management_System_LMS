from backend import mysql_tables
cur = mysql_tables.mydb.cursor()
mydb = mysql_tables.mydb

"""CREATE TABLE IF NOT EXISTS notifications(
    user_id VARCHAR(30),
    message TEXT,
    notification_datetime DATETIME DEFAULT NOW()
);
"""

def send_notification(user_id, message):
    cur.execute("""
        INSERT INTO notifications (user_id, message)
        VALUES (%s, %s)
    """, (user_id, message))
    mydb.commit()


def get_latest_notifications(user_id):
    cur.execute("""
        SELECT message, notification_datetime
        FROM notifications
        WHERE user_id = %s
        ORDER BY notification_datetime DESC
        LIMIT 4
    """, (user_id,))
    return cur.fetchall()
