"""
Banking Management System (Complete) — Python + MySQL + Tkinter
Single-file final project for DBMS course submission.

Features:
 - Prompts for MySQL connection (host/port/user/password/database)
 - Creates DB and normalized tables automatically
 - Optional sample data insertion
 - Tkinter GUI:
    - Login (Customer/Admin)
    - Customer dashboard: view balance, deposit, withdraw, transfer, transactions
    - Admin dashboard: view/create customers & accounts, normalization demo, DCL demo
 - Proper transaction control (COMMIT/ROLLBACK) and SELECT ... FOR UPDATE locking
 - Demonstrates DDL, DML, DQL, TCL, DCL, normalization, lossless decomposition

Dependencies:
  pip install mysql-connector-python

Usage:
  python banking_full_app.py
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import sys
import traceback

# -------------------------
# DB helper - will prompt user for credentials at runtime
# -------------------------
class DBConfig:
    host = 'localhost'
    port = 3306
    user = 'root'
    password = ''
    database = 'banking_db'

def prompt_db_credentials():
    root = tk.Tk()
    root.withdraw()  # hide main window
    messagebox.showinfo("Database Setup", "Provide MySQL connection details in the next dialogs.\nIf MySQL is on the same machine, host=localhost and port=3306 are typical.")
    DBConfig.host = simpledialog.askstring("MySQL Host", "Host (default 'localhost'):", initialvalue='localhost') or 'localhost'
    DBConfig.port = int(simpledialog.askstring("MySQL Port", "Port (default 3306):", initialvalue='3306') or 3306)
    DBConfig.user = simpledialog.askstring("MySQL Username", "Username (e.g., root):", initialvalue='root') or 'root'
    DBConfig.password = simpledialog.askstring("MySQL Password", "Password (leave blank if none):", show='*') or ''
    DBConfig.database = simpledialog.askstring("Database Name", "Database name to create/use (default 'banking_db'):", initialvalue='banking_db') or 'banking_db'
    root.destroy()

def get_connection(use_db=True):
    cfg = {
        'host': DBConfig.host,
        'port': DBConfig.port,
        'user': DBConfig.user,
        'password': DBConfig.password,
    }
    if use_db:
        cfg['database'] = DBConfig.database
    return mysql.connector.connect(**cfg)

# -------------------------
# Database initialization: create DB + tables + optional sample data
# -------------------------
CREATE_TABLES_SQL = {
    'Branch': (
        "CREATE TABLE IF NOT EXISTS Branch ("
        " BranchID INT PRIMARY KEY,"
        " BranchName VARCHAR(100) NOT NULL,"
        " Location VARCHAR(100)"
        ") ENGINE=InnoDB"
    ),
    'Customer': (
        "CREATE TABLE IF NOT EXISTS Customer ("
        " CustomerID INT PRIMARY KEY,"
        " Name VARCHAR(100) NOT NULL,"
        " Address VARCHAR(200),"
        " Phone VARCHAR(20),"
        " BranchID INT,"
        " Username VARCHAR(50) UNIQUE,"  # for login
        " Password VARCHAR(100),"        # demo plain text
        " FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)"
        ") ENGINE=InnoDB"
    ),
    'Account': (
        "CREATE TABLE IF NOT EXISTS Account ("
        " AccountNo INT PRIMARY KEY,"
        " CustomerID INT,"
        " BranchID INT,"
        " Balance DECIMAL(15,2) DEFAULT 0.00,"
        " AccountType VARCHAR(20),"
        " FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),"
        " FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)"
        ") ENGINE=InnoDB"
    ),
    'Loan': (
        "CREATE TABLE IF NOT EXISTS Loan ("
        " LoanID INT PRIMARY KEY,"
        " CustomerID INT,"
        " BranchID INT,"
        " LoanAmount DECIMAL(15,2),"
        " Status VARCHAR(20),"
        " FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),"
        " FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)"
        ") ENGINE=InnoDB"
    ),
    'Transaction': (
        "CREATE TABLE IF NOT EXISTS Transaction ("
        " TransactionID INT PRIMARY KEY,"
        " AccountNo INT,"
        " TransactionType VARCHAR(20),"
        " Amount DECIMAL(15,2),"
        " TDate DATETIME,"
        " FOREIGN KEY (AccountNo) REFERENCES Account(AccountNo)"
        ") ENGINE=InnoDB"
    ),
    'Employee': (
        "CREATE TABLE IF NOT EXISTS Employee ("
        " EmployeeID INT PRIMARY KEY,"
        " Name VARCHAR(100),"
        " BranchID INT,"
        " Username VARCHAR(50) UNIQUE,"
        " Password VARCHAR(100),"
        " Role VARCHAR(50),"
        " Salary DECIMAL(12,2),"
        " FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)"
        ") ENGINE=InnoDB"
    ),
}

SAMPLE_DATA = {
    'branches': [
        (101, 'Main Branch', 'New Delhi'),
        (102, 'Suburb Branch', 'Noida'),
    ],
    'customers': [
        (1, 'Amit Sharma', 'Delhi', '9876500001', 101, 'amit', 'a'),  # username/password for demo
        (2, 'Rohit Verma', 'Noida', '9876500002', 102, 'rohit', 'r'),
        (3, 'Sita Patel', 'Delhi', '9876500003', 101, 'sita', 's'),
    ],
    'accounts': [
        (5001, 1, 101, 25000.00, 'Savings'),
        (5002, 2, 102, 40000.00, 'Savings'),
        (5003, 1, 101, 15000.00, 'Current'),
        (5004, 3, 101, 30000.00, 'Savings'),
    ],
    'loans': [
        (7001, 2, 102, 200000.00, 'Pending'),
        (7002, 3, 101, 50000.00, 'Paid'),
    ],
    'employees': [
        (9001, 'Ramesh', 101, 'admin', 'adminpw', 'Manager', 80000.00),
        (9002, 'Suresh', 102, 'teller', 'tellerpw', 'Teller', 30000.00),
    ],
    'transactions': [
        (10001, 5001, 'Deposit', 5000.00, '2025-09-01 10:00:00'),
        (10002, 5002, 'Deposit', 10000.00, '2025-09-02 11:00:00'),
        (10003, 5001, 'Withdraw', 2000.00, '2025-09-03 09:30:00'),
    ]
}

def initialize_database(create_sample=False):
    # Create database if not exists
    try:
        cnx = get_connection(use_db=False)
    except Exception as e:
        messagebox.showerror("DB Connection", f"Unable to connect to MySQL: {e}")
        return False
    cursor = cnx.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DBConfig.database} DEFAULT CHARACTER SET 'utf8mb4'")
    except Exception as e:
        messagebox.showerror("DB Error", f"Failed to create database: {e}")
        cursor.close()
        cnx.close()
        return False
    cursor.close()
    cnx.close()

    # Create tables
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        for name, ddl in CREATE_TABLES_SQL.items():
            cursor.execute(ddl)
        cnx.commit()
    except Exception as e:
        messagebox.showerror("DB Error", f"Failed creating tables: {e}")
        traceback.print_exc()
        return False
    finally:
        cursor.close()
        cnx.close()

    if create_sample:
        try:
            cnx = get_connection()
            cursor = cnx.cursor()
            # Clear old sample (safe for demo)
            for t in ('Transaction','Loan','Account','Employee','Customer','Branch'):
                cursor.execute(f"DELETE FROM {t}")
            # Insert sample
            cursor.executemany("INSERT INTO Branch (BranchID, BranchName, Location) VALUES (%s,%s,%s)", SAMPLE_DATA['branches'])
            cursor.executemany("INSERT INTO Customer (CustomerID, Name, Address, Phone, BranchID, Username, Password) VALUES (%s,%s,%s,%s,%s,%s,%s)", SAMPLE_DATA['customers'])
            cursor.executemany("INSERT INTO Employee (EmployeeID, Name, BranchID, Username, Password, Role, Salary) VALUES (%s,%s,%s,%s,%s,%s,%s)", SAMPLE_DATA['employees'])
            cursor.executemany("INSERT INTO Account (AccountNo, CustomerID, BranchID, Balance, AccountType) VALUES (%s,%s,%s,%s,%s)", SAMPLE_DATA['accounts'])
            cursor.executemany("INSERT INTO Loan (LoanID, CustomerID, BranchID, LoanAmount, Status) VALUES (%s,%s,%s,%s,%s)", SAMPLE_DATA['loans'])
            cursor.executemany("INSERT INTO Transaction (TransactionID, AccountNo, TransactionType, Amount, TDate) VALUES (%s,%s,%s,%s,%s)", SAMPLE_DATA['transactions'])
            cnx.commit()
        except Exception as e:
            messagebox.showerror("DB Error", f"Failed inserting sample data: {e}")
            traceback.print_exc()
            return False
        finally:
            cursor.close()
            cnx.close()
    return True

# -------------------------
# Business logic: account ops & queries
# -------------------------
def get_customer_by_username(username):
    try:
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Customer WHERE Username=%s", (username,))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()
        return row
    except Exception:
        return None

def get_employee_by_username(username):
    try:
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Employee WHERE Username=%s", (username,))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()
        return row
    except Exception:
        return None

def get_accounts_for_customer(customer_id):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT AccountNo, AccountType, Balance FROM Account WHERE CustomerID=%s", (customer_id,))
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    return rows

def get_total_balance(customer_id):
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT IFNULL(SUM(Balance),0) FROM Account WHERE CustomerID=%s", (customer_id,))
    s = cursor.fetchone()[0]
    cursor.close()
    cnx.close()
    return float(s)

def insert_transaction_record(txn_id, account_no, ttype, amount):
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO Transaction (TransactionID, AccountNo, TransactionType, Amount, TDate) VALUES (%s,%s,%s,%s,NOW())", (txn_id, account_no, ttype, amount))
    cnx.commit()
    cursor.close()
    cnx.close()

def deposit(account_no, amount):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        cnx.start_transaction()
        cursor.execute("UPDATE Account SET Balance = Balance + %s WHERE AccountNo = %s", (amount, account_no))
        cursor.execute("SELECT Balance FROM Account WHERE AccountNo=%s", (account_no,))
        new_bal = cursor.fetchone()[0]
        cursor.execute("INSERT INTO Transaction (TransactionID, AccountNo, TransactionType, Amount, TDate) VALUES (%s,%s,%s,%s,NOW())", (90000+int(account_no), account_no, 'Deposit', amount))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True, new_bal
    except Exception as e:
        try:
            cnx.rollback()
        except:
            pass
        return False, str(e)

def withdraw(account_no, amount):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        cnx.start_transaction()
        # lock row
        cursor.execute("SELECT Balance FROM Account WHERE AccountNo=%s FOR UPDATE", (account_no,))
        row = cursor.fetchone()
        if not row:
            cnx.rollback()
            cursor.close()
            cnx.close()
            return False, "Account not found"
        bal = float(row[0])
        if bal < amount:
            cnx.rollback()
            cursor.close()
            cnx.close()
            return False, "Insufficient funds"
        cursor.execute("UPDATE Account SET Balance = Balance - %s WHERE AccountNo = %s", (amount, account_no))
        cursor.execute("INSERT INTO Transaction (TransactionID, AccountNo, TransactionType, Amount, TDate) VALUES (%s,%s,%s,%s,NOW())", (91000+int(account_no), account_no, 'Withdraw', amount))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True, "Withdraw successful"
    except Exception as e:
        try:
            cnx.rollback()
        except:
            pass
        return False, str(e)

def transfer(from_acc, to_acc, amount):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        cnx.start_transaction()
        # lock both accounts in consistent order
        a1, a2 = (from_acc, to_acc) if from_acc <= to_acc else (to_acc, from_acc)
        cursor.execute("SELECT AccountNo, Balance FROM Account WHERE AccountNo IN (%s,%s) FOR UPDATE", (a1, a2))
        rows = cursor.fetchall()
        acc_map = {r[0]: float(r[1]) for r in rows}
        if from_acc not in acc_map:
            cnx.rollback()
            cursor.close()
            cnx.close()
            return False, "From account not found"
        if to_acc not in acc_map:
            cnx.rollback()
            cursor.close()
            cnx.close()
            return False, "To account not found"
        if acc_map[from_acc] < amount:
            cnx.rollback()
            cursor.close()
            cnx.close()
            return False, "Insufficient funds"
        cursor.execute("UPDATE Account SET Balance = Balance - %s WHERE AccountNo=%s", (amount, from_acc))
        cursor.execute("UPDATE Account SET Balance = Balance + %s WHERE AccountNo=%s", (amount, to_acc))
        cursor.execute("INSERT INTO Transaction (TransactionID, AccountNo, TransactionType, Amount, TDate) VALUES (%s,%s,%s,%s,NOW())", (20000+from_acc, from_acc, 'Transfer Out', amount))
        cursor.execute("INSERT INTO Transaction (TransactionID, AccountNo, TransactionType, Amount, TDate) VALUES (%s,%s,%s,%s,NOW())", (30000+to_acc, to_acc, 'Transfer In', amount))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True, "Transfer successful"
    except Exception as e:
        try:
            cnx.rollback()
        except:
            pass
        return False, str(e)

def get_transaction_history_for_account(account_no, limit=100):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT TransactionID, TransactionType, Amount, TDate FROM Transaction WHERE AccountNo=%s ORDER BY TDate DESC LIMIT %s", (account_no, limit))
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    return rows

# -------------------------
# Admin utilities: create customer & account, run normalization demo, run DCL demo
# -------------------------
def create_customer_and_account(customer_id, name, address, phone, branch_id, username, password, account_no, account_type, initial_balance):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        cnx.start_transaction()
        cursor.execute("INSERT INTO Customer (CustomerID, Name, Address, Phone, BranchID, Username, Password) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                       (customer_id, name, address, phone, branch_id, username, password))
        cursor.execute("INSERT INTO Account (AccountNo, CustomerID, BranchID, Balance, AccountType) VALUES (%s,%s,%s,%s,%s)",
                       (account_no, customer_id, branch_id, initial_balance, account_type))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True, "Customer and account created"
    except Exception as e:
        try:
            cnx.rollback()
        except:
            pass
        return False, str(e)

def dcl_create_demo_user():
    # Demonstrate GRANT/REVOKE (only works if current DB user has privilege)
    try:
        cnx = get_connection(use_db=False)
        cursor = cnx.cursor()
        cursor.execute("CREATE USER IF NOT EXISTS 'demo_teller'@'localhost' IDENTIFIED BY 'demo_pass'")
        cursor.execute(f"GRANT INSERT ON {DBConfig.database}.Transaction TO 'demo_teller'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")
        cnx.commit()
        cursor.close()
        cnx.close()
        return True, "Created demo_teller and granted INSERT on Transaction (if permitted)"
    except Exception as e:
        return False, str(e)

def dcl_revoke_demo_user():
    try:
        cnx = get_connection(use_db=False)
        cursor = cnx.cursor()
        cursor.execute(f"REVOKE INSERT ON {DBConfig.database}.Transaction FROM 'demo_teller'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")
        cnx.commit()
        cursor.close()
        cnx.close()
        return True, "Revoked INSERT privilege from demo_teller (if permitted)"
    except Exception as e:
        return False, str(e)

def normalization_lossless_demo():
    # create an unnormalized table view and decompose to show lossless join
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        cursor.execute("DROP TABLE IF EXISTS UnnormalizedRaw")
        cursor.execute(
            "CREATE TABLE UnnormalizedRaw AS "
            "SELECT c.CustomerID, c.Name, c.Address, c.Phone, b.BranchName, b.Location AS BranchLocation, a.AccountNo, a.Balance AS AccountBalance "
            "FROM Customer c JOIN Branch b ON c.BranchID=b.BranchID JOIN Account a ON a.CustomerID=c.CustomerID"
        )
        cursor.execute("DROP TABLE IF EXISTS CustProv")
        cursor.execute("CREATE TABLE CustProv AS SELECT DISTINCT CustomerID, Name, Address, Phone, BranchName, BranchLocation FROM UnnormalizedRaw")
        cursor.execute("DROP TABLE IF EXISTS AccProv")
        cursor.execute("CREATE TABLE AccProv AS SELECT AccountNo, CustomerID, AccountBalance FROM UnnormalizedRaw")
        cnx.commit()
        # counts
        cursor.execute("SELECT COUNT(*) FROM UnnormalizedRaw")
        raw_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM (SELECT cp.CustomerID, cp.Name, cp.Address, cp.Phone, cp.BranchName, cp.BranchLocation, a.AccountNo, a.AccountBalance FROM CustProv cp JOIN AccProv a ON cp.CustomerID = a.CustomerID) t")
        recon = cursor.fetchone()[0]
        cursor.close()
        cnx.close()
        return True, {"raw_count": raw_count, "reconstructed": recon}
    except Exception as e:
        try:
            cnx.rollback()
        except:
            pass
        return False, str(e)

# -------------------------
# Tkinter App
# -------------------------
class BankingAppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Banking Management System")
        self.geometry("940x640")
        self.resizable(False, False)
        self.user = None  # dict: {'type':'customer'/'admin', 'data':...}
        self.style = ttk.Style(self)
        # set theme
        try:
            self.style.theme_use('clam')
        except:
            pass
        self.create_login_screen()

    def clear(self):
        for w in self.winfo_children():
            w.destroy()

    def create_login_screen(self):
        self.clear()
        frame = ttk.Frame(self, padding=20)
        frame.pack(expand=True, fill='both')

        title = ttk.Label(frame, text="Banking Management System", font=("Helvetica", 20, "bold"))
        title.pack(pady=(10,20))

        form = ttk.Frame(frame)
        form.pack()

        ttk.Label(form, text="Username:").grid(row=0, column=0, sticky='e', padx=6, pady=6)
        username_entry = ttk.Entry(form, width=30)
        username_entry.grid(row=0, column=1, pady=6)

        ttk.Label(form, text="Password:").grid(row=1, column=0, sticky='e', padx=6, pady=6)
        password_entry = ttk.Entry(form, width=30, show='*')
        password_entry.grid(row=1, column=1, pady=6)

        ttk.Label(form, text="Role:").grid(row=2, column=0, sticky='e', padx=6, pady=6)
        role_box = ttk.Combobox(form, values=['customer', 'admin'], state='readonly')
        role_box.current(0)
        role_box.grid(row=2, column=1, pady=6)

        def attempt_login():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            role = role_box.get()
            if role == 'customer':
                row = get_customer_by_username(username)
                if not row:
                    messagebox.showerror("Login", "Customer not found")
                    return
                # demo password check
                if row.get('Password') and row.get('Password') != password:
                    messagebox.showerror("Login", "Invalid password")
                    return
                self.user = {'type': 'customer', 'data': row}
                self.create_customer_dashboard()
            else:
                row = get_employee_by_username(username)
                if not row:
                    messagebox.showerror("Login", "Admin not found")
                    return
                if row.get('Password') and row.get('Password') != password:
                    messagebox.showerror("Login", "Invalid password")
                    return
                self.user = {'type': 'admin', 'data': row}
                self.create_admin_dashboard()

        login_btn = ttk.Button(frame, text="Login", command=attempt_login)
        login_btn.pack(pady=12)

        hint = ttk.Label(frame, text="Demo credentials inserted if you initialized sample data.\nCustomers: amit/a | rohit/r | sita/s  — Admin: admin/adminpw", foreground='gray')
        hint.pack(pady=(6,0))

    # ---------------- Customer Dashboard ----------------
    def create_customer_dashboard(self):
        self.clear()
        user = self.user['data']
        top = ttk.Frame(self, padding=10)
        top.pack(fill='x')
        ttk.Label(top, text=f"Welcome, {user['Name']}", font=("Helvetica", 16, "bold")).pack(side='left')
        ttk.Button(top, text="Logout", command=self.logout).pack(side='right')

        mid = ttk.Frame(self, padding=10)
        mid.pack(fill='x')
        # balance display
        balance_var = tk.StringVar()
        def refresh_balance():
            try:
                s = get_total_balance(user['CustomerID'])
                balance_var.set(f"Total Balance: ₹{s:,.2f}")
                # refresh accounts table
                accounts = get_accounts_for_customer(user['CustomerID'])
                for i in accounts_tree.get_children():
                    accounts_tree.delete(i)
                for acc in accounts:
                    accounts_tree.insert('', 'end', values=(acc['AccountNo'], acc['AccountType'], f"₹{float(acc['Balance']):,.2f}"))
            except Exception as e:
                balance_var.set("Error fetching balance")

        ttk.Label(mid, textvariable=balance_var, font=("Helvetica", 14)).pack(side='left')
        ttk.Button(mid, text="Refresh", command=refresh_balance).pack(side='left', padx=8)
        ttk.Button(mid, text="Transaction History", command=lambda: self.open_transaction_history_for_customer(user)).pack(side='right')

        actions = ttk.Frame(self, padding=10)
        actions.pack(fill='x')
        ttk.Button(actions, text='Deposit', command=lambda: self.open_deposit_window(user, refresh_balance)).pack(side='left', padx=8)
        ttk.Button(actions, text='Withdraw', command=lambda: self.open_withdraw_window(user, refresh_balance)).pack(side='left', padx=8)
        ttk.Button(actions, text='Transfer', command=lambda: self.open_transfer_window(user, refresh_balance)).pack(side='left', padx=8)

        accounts_frame = ttk.LabelFrame(self, text="Your Accounts", padding=8)
        accounts_frame.pack(fill='both', expand=True, padx=12, pady=12)

        cols = ("AccountNo", "AccountType", "Balance")
        accounts_tree = ttk.Treeview(accounts_frame, columns=cols, show='headings', height=8)
        for c in cols:
            accounts_tree.heading(c, text=c)
            accounts_tree.column(c, anchor='center')
        accounts_tree.pack(fill='both', expand=True)

        # load
        refresh_balance()

    def open_deposit_window(self, user, refresh_cb):
        w = tk.Toplevel(self)
        w.title("Deposit")
        ttk.Label(w, text="Account No:").grid(row=0, column=0, padx=6, pady=6)
        acc_entry = ttk.Entry(w)
        acc_entry.grid(row=0, column=1, padx=6, pady=6)
        ttk.Label(w, text="Amount:").grid(row=1, column=0, padx=6, pady=6)
        amt_entry = ttk.Entry(w)
        amt_entry.grid(row=1, column=1, padx=6, pady=6)
        def do_deposit():
            try:
                acc = int(acc_entry.get().strip())
                amt = float(amt_entry.get().strip())
            except:
                messagebox.showerror("Input", "Invalid account or amount")
                return
            ok, detail = deposit(acc, amt)
            if ok:
                messagebox.showinfo("Deposit", f"Deposit successful. New balance: {detail}")
                refresh_cb()
                w.destroy()
            else:
                messagebox.showerror("Deposit Failed", detail)
        ttk.Button(w, text="Deposit", command=do_deposit).grid(row=2, column=0, columnspan=2, pady=8)

    def open_withdraw_window(self, user, refresh_cb):
        w = tk.Toplevel(self)
        w.title("Withdraw")
        ttk.Label(w, text="Account No:").grid(row=0, column=0, padx=6, pady=6)
        acc_entry = ttk.Entry(w)
        acc_entry.grid(row=0, column=1, padx=6, pady=6)
        ttk.Label(w, text="Amount:").grid(row=1, column=0, padx=6, pady=6)
        amt_entry = ttk.Entry(w)
        amt_entry.grid(row=1, column=1, padx=6, pady=6)
        def do_withdraw():
            try:
                acc = int(acc_entry.get().strip())
                amt = float(amt_entry.get().strip())
            except:
                messagebox.showerror("Input", "Invalid account or amount")
                return
            ok, detail = withdraw(acc, amt)
            if ok:
                messagebox.showinfo("Withdraw", detail)
                refresh_cb()
                w.destroy()
            else:
                messagebox.showerror("Withdraw Failed", detail)
        ttk.Button(w, text="Withdraw", command=do_withdraw).grid(row=2, column=0, columnspan=2, pady=8)

    def open_transfer_window(self, user, refresh_cb):
        w = tk.Toplevel(self)
        w.title("Transfer")
        ttk.Label(w, text="From Account No:").grid(row=0, column=0, padx=6, pady=6)
        from_entry = ttk.Entry(w)
        from_entry.grid(row=0, column=1, padx=6, pady=6)
        ttk.Label(w, text="To Account No:").grid(row=1, column=0, padx=6, pady=6)
        to_entry = ttk.Entry(w)
        to_entry.grid(row=1, column=1, padx=6, pady=6)
        ttk.Label(w, text="Amount:").grid(row=2, column=0, padx=6, pady=6)
        amt_entry = ttk.Entry(w)
        amt_entry.grid(row=2, column=1, padx=6, pady=6)
        def do_transfer():
            try:
                fa = int(from_entry.get().strip())
                ta = int(to_entry.get().strip())
                amt = float(amt_entry.get().strip())
            except:
                messagebox.showerror("Input", "Invalid accounts or amount")
                return
            ok, detail = transfer(fa, ta, amt)
            if ok:
                messagebox.showinfo("Transfer", detail)
                refresh_cb()
                w.destroy()
            else:
                messagebox.showerror("Transfer Failed", detail)
        ttk.Button(w, text="Transfer", command=do_transfer).grid(row=3, column=0, columnspan=2, pady=8)

    def open_transaction_history_for_customer(self, user):
        w = tk.Toplevel(self)
        w.title("Transaction History")
        ttk.Label(w, text=f"Transaction history for all your accounts (latest)").pack(pady=6)
        tree = ttk.Treeview(w, columns=("TxnID","AccountNo","Type","Amount","Date"), show='headings')
        for c in ("TxnID","AccountNo","Type","Amount","Date"):
            tree.heading(c, text=c)
            tree.column(c, anchor='center')
        tree.pack(fill='both', expand=True)
        accounts = get_accounts_for_customer(user['CustomerID'])
        for acc in accounts:
            rows = get_transaction_history_for_account(acc['AccountNo'], limit=200)
            for r in rows:
                tree.insert('', 'end', values=(r['TransactionID'], acc['AccountNo'], r['TransactionType'], f"₹{float(r['Amount']):,.2f}", r['TDate']))

    def logout(self):
        self.user = None
        self.create_login_screen()

    # ---------------- Admin Dashboard ----------------
    def create_admin_dashboard(self):
        self.clear()
        user = self.user['data']
        top = ttk.Frame(self, padding=10)
        top.pack(fill='x')
        ttk.Label(top, text=f"Admin Panel - {user['Name']}", font=("Helvetica", 16, "bold")).pack(side='left')
        ttk.Button(top, text="Logout", command=self.logout).pack(side='right')

        actions = ttk.Frame(self, padding=8)
        actions.pack(fill='x')

        ttk.Button(actions, text="View Customers", command=self.open_view_customers).pack(side='left', padx=6)
        ttk.Button(actions, text="Create Customer & Account", command=self.open_create_customer_account).pack(side='left', padx=6)
        ttk.Button(actions, text="Normalization Demo", command=self.run_normalization_demo).pack(side='left', padx=6)
        ttk.Button(actions, text="DCL Demo (GRANT)", command=self.run_dcl_create).pack(side='left', padx=6)
        ttk.Button(actions, text="DCL Demo (REVOKE)", command=self.run_dcl_revoke).pack(side='left', padx=6)

        # quick stats area
        stats = ttk.Frame(self, padding=8)
        stats.pack(fill='both', expand=True)
        # show tables and counts
        try:
            cnx = get_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT COUNT(*) FROM Customer")
            cust_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Account")
            acc_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Transaction")
            txn_count = cursor.fetchone()[0]
            cursor.close()
            cnx.close()
        except Exception:
            cust_count = acc_count = txn_count = 'NA'

        ttk.Label(stats, text=f"Total Customers: {cust_count}", font=("Helvetica", 12)).pack(anchor='nw', pady=6)
        ttk.Label(stats, text=f"Total Accounts: {acc_count}", font=("Helvetica", 12)).pack(anchor='nw', pady=6)
        ttk.Label(stats, text=f"Total Transactions: {txn_count}", font=("Helvetica", 12)).pack(anchor='nw', pady=6)

    def open_view_customers(self):
        w = tk.Toplevel(self)
        w.title("All Customers")
        tree = ttk.Treeview(w, columns=("CustomerID","Name","Phone","BranchID","Username"), show='headings')
        for c in ("CustomerID","Name","Phone","BranchID","Username"):
            tree.heading(c, text=c)
            tree.column(c, anchor='center')
        tree.pack(fill='both', expand=True)
        try:
            cnx = get_connection()
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT CustomerID, Name, Phone, BranchID, Username FROM Customer")
            for r in cursor.fetchall():
                tree.insert('', 'end', values=(r['CustomerID'], r['Name'], r['Phone'], r['BranchID'], r.get('Username')))
            cursor.close()
            cnx.close()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_create_customer_account(self):
        w = tk.Toplevel(self)
        w.title("Create Customer & Account")
        frm = ttk.Frame(w, padding=8)
        frm.pack()
        labels = ["CustomerID","Name","Address","Phone","BranchID","Username","Password","AccountNo","AccountType","InitialBalance"]
        entries = {}
        for i, lab in enumerate(labels):
            ttk.Label(frm, text=lab+":").grid(row=i, column=0, sticky='e', padx=6, pady=4)
            e = ttk.Entry(frm)
            e.grid(row=i, column=1, padx=6, pady=4)
            entries[lab] = e
        def do_create():
            try:
                cid = int(entries["CustomerID"].get().strip())
                name = entries["Name"].get().strip()
                addr = entries["Address"].get().strip()
                phone = entries["Phone"].get().strip()
                bid = int(entries["BranchID"].get().strip())
                uname = entries["Username"].get().strip()
                pwd = entries["Password"].get().strip()
                accno = int(entries["AccountNo"].get().strip())
                atype = entries["AccountType"].get().strip()
                ibal = float(entries["InitialBalance"].get().strip())
            except Exception:
                messagebox.showerror("Input", "Invalid or missing input")
                return
            ok, msg = create_customer_and_account(cid, name, addr, phone, bid, uname, pwd, accno, atype, ibal)
            if ok:
                messagebox.showinfo("Success", msg)
                w.destroy()
            else:
                messagebox.showerror("Failed", msg)
        ttk.Button(frm, text="Create", command=do_create).grid(row=len(labels), column=0, columnspan=2, pady=8)

    def run_normalization_demo(self):
        ok, result = normalization_lossless_demo()
        if ok:
            raw = result.get('raw_count')
            recon = result.get('reconstructed')
            messagebox.showinfo("Normalization Demo", f"Unnormalized rows: {raw}\nReconstructed after decomposition: {recon}\nLossless decomposition test: {'PASS' if raw==recon else 'FAIL'}")
        else:
            messagebox.showerror("Normalization Demo Failed", str(result))

    def run_dcl_create(self):
        ok, msg = dcl_create_demo_user()
        if ok:
            messagebox.showinfo("DCL", msg)
        else:
            messagebox.showerror("DCL Failed", msg)

    def run_dcl_revoke(self):
        ok, msg = dcl_revoke_demo_user()
        if ok:
            messagebox.showinfo("DCL", msg)
        else:
            messagebox.showerror("DCL Failed", msg)

# -------------------------
# Main: prompt credentials, initialize DB optionally, run GUI
# -------------------------
def main():
    # Prompt DB creds
    prompt_db_credentials()
    # Ask whether to initialize DB and insert sample data
    root_prompt = tk.Tk()
    root_prompt.withdraw()
    init = messagebox.askyesno("Initialize Database", f"Create database '{DBConfig.database}' and tables if not present?")
    create_sample = False
    if init:
        create_sample = messagebox.askyesno("Sample Data", "Insert demo sample data (customers/accounts/employees)? (Recommended for demo)")
    root_prompt.destroy()

    ok = initialize_database(create_sample)
    if not ok:
        print("Database initialization failed. Exiting.")
        sys.exit(1)

    # Launch GUI
    app = BankingAppGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
