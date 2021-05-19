import pymysql
import traceback

def DeleteData():
    try:
        id=eval(input("Enter your ID = "))
        connection=pymysql.connect(host="localhost",user="root",password="root",db="iitnit")
        with connection.cursor() as cursor:
            sql="Delete from company where ID=%s"
            try:
                cursor.execute(sql,(id))
                connection.commit()
                print("Data Delete successfully")
            except Exception:
                traceback.print_exc()
    except Exception:
            traceback.print_exc()


DeleteData()