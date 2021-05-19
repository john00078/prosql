import pymysql
import traceback


try:
    connection=pymysql.connect(host="localhost",user="root",password="root",db="school")
    print("Connection is done")
except Exception:
    traceback.print_exc()
    