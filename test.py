from backend import mysql_tables
title = "Black Holes"
author = "Stephen Hawking"
edition = "1"
mysql_tables.cur.execute("select description from books where title=%s and author=%s and edition=%s",(title,author,edition))
result = mysql_tables.cur.fetchone()
print(result[0])