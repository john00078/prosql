
import pymysql
import traceback

try:
    connection=pymysql.connect(host="localhost",user="root",password="root",db="iitnit")
    with connection.cursor() as cursor:
        sql="insert into company(id,name,company,salary) values(%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(5,'pichai','windows',450))
            connection.commit()
            print("Data Saved successfully")
        except Exception:
            traceback.print_exc()
except Exception:
    traceback.print_exc()
