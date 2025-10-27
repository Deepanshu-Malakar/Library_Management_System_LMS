import mysql.connector
from datetime import datetime

# connect to your database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="library"
)
cur = mydb.cursor()

# -------------------------
# 📘 BOOK REPORTS
# -------------------------
def report_available_books():
    cur.execute("SELECT book_id, title, author, edition, category, available FROM books WHERE available > 0;")
    return cur.fetchall()

def report_most_issued_books(limit=5):
    cur.execute("""
        SELECT b.title, b.author, COUNT(*) AS issue_count
        FROM issue_books i
        JOIN books b ON i.book_id = b.book_id
        GROUP BY b.title, b.author
        ORDER BY issue_count DESC
        LIMIT %s
    """, (limit,))
    return cur.fetchall()

def report_books_by_category():
    cur.execute("SELECT category, COUNT(*) FROM books GROUP BY category;")
    return cur.fetchall()

def report_most_favourite_books(limit=5):
    cur.execute("""
        SELECT title, author, COUNT(*) AS fav_count
        FROM favourites
        GROUP BY title, author
        ORDER BY fav_count DESC
        LIMIT %s
    """, (limit,))
    return cur.fetchall()

# -------------------------
# 👩‍🎓 USER REPORTS
# -------------------------
def report_user_counts():
    cur.execute("""
        SELECT 'students' AS role, COUNT(*) FROM students
        UNION ALL
        SELECT 'faculty', COUNT(*) FROM faculty
        UNION ALL
        SELECT 'scholars', COUNT(*) FROM scholars
        UNION ALL
        SELECT 'librarian', COUNT(*) FROM librarian;
    """)
    return cur.fetchall()

def report_department_wise_users():
    cur.execute("""
        SELECT department, COUNT(*) FROM students GROUP BY department
        UNION ALL
        SELECT department, COUNT(*) FROM faculty GROUP BY department;
    """)
    return cur.fetchall()

def report_upcoming_birthdays():
    cur.execute("""
        SELECT student_id AS id, first_name, last_name, DOB, 'student' AS role FROM students WHERE MONTH(DOB)=MONTH(CURDATE())
        UNION
        SELECT faculty_id, first_name, last_name, DOB, 'faculty' FROM faculty WHERE MONTH(DOB)=MONTH(CURDATE())
        UNION
        SELECT scholar_id, first_name, last_name, DOB, 'scholar' FROM scholars WHERE MONTH(DOB)=MONTH(CURDATE())
        UNION
        SELECT lib_id, first_name, last_name, DOB, 'librarian' FROM librarian WHERE MONTH(DOB)=MONTH(CURDATE());
    """)
    return cur.fetchall()

# -------------------------
# 📦 ISSUE / RETURN REPORTS
# -------------------------
def report_active_issues():
    cur.execute("""
        SELECT i.user_id, b.title, b.author, i.issue_date, i.return_date
        FROM issue_books i
        JOIN books b ON i.book_id = b.book_id
        WHERE i.status='issued';
    """)
    return cur.fetchall()

def report_overdue_books():
    cur.execute("""
        SELECT i.user_id, b.title, i.issue_date, i.return_date
        FROM issue_books i
        JOIN books b ON i.book_id = b.book_id
        WHERE i.status='issued' AND i.return_date < CURDATE();
    """)
    return cur.fetchall()

def report_frequent_borrowers(limit=5):
    cur.execute("""
        SELECT user_id, COUNT(*) AS issue_count
        FROM issue_books
        GROUP BY user_id
        ORDER BY issue_count DESC
        LIMIT %s
    """, (limit,))
    return cur.fetchall()

# -------------------------
# 💬 DOUBTS / SOLUTIONS
# -------------------------
def report_unanswered_doubts():
    cur.execute("""
        SELECT d.doubt_id, d.user_id, d.doubt
        FROM doubts d
        LEFT JOIN solutions s ON d.doubt_id = s.doubt_id
        WHERE s.doubt_id IS NULL;
    """)
    return cur.fetchall()

def report_most_active_helpers(limit=5):
    cur.execute("""
        SELECT user_id, COUNT(*) AS solutions_posted
        FROM solutions
        GROUP BY user_id
        ORDER BY solutions_posted DESC
        LIMIT %s
    """, (limit,))
    return cur.fetchall()

# -------------------------
# 🔔 NOTIFICATIONS
# -------------------------
def report_recent_notifications(limit=10):
    cur.execute("""
        SELECT user_id, message, notification_datetime
        FROM notifications
        ORDER BY notification_datetime DESC
        LIMIT %s
    """, (limit,))
    return cur.fetchall()

# -------------------------
# 📊 SYSTEM SUMMARY
# -------------------------
def report_system_summary():
    cur.execute("SELECT COUNT(*) FROM books;")
    total_books = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM issue_books WHERE status='issued';")
    total_issued = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM reserve_books;")
    total_reserved = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM request_book;")
    total_requested = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM notifications;")
    total_notifications = cur.fetchone()[0]

    return {
        "total_books": total_books,
        "issued_books": total_issued,
        "reserved_books": total_reserved,
        "requested_books": total_requested,
        "notifications": total_notifications
    }

# -------------------------
# 🧭 MENU TESTING (Console Mode)
# -------------------------
if __name__ == "__main__":
    print("📊 Library Report Generator\n")

    print("1. Available Books")
    print("2. Most Issued Books")
    print("3. User Counts")
    print("4. Overdue Books")
    print("5. System Summary")
    print("6. Recent Notifications")

    choice = input("\nEnter choice: ")

    if choice == "1":
        print(report_available_books())
    elif choice == "2":
        print(report_most_issued_books())
    elif choice == "3":
        print(report_user_counts())
    elif choice == "4":
        print(report_overdue_books())
    elif choice == "5":
        print(report_system_summary())
    elif choice == "6":
        print(report_recent_notifications())
