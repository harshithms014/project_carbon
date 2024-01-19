import MySQLdb

def connection():
    conn = MySQLdb.connect("localhost","root","1234","flask")
    c = conn.cursor()
    return c,conn