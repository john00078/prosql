import pymysql
import traceback

def InsertData():
    try:
        id=eval(input("Enter your ID = "))
        name=input("Enter your Name = ")
        company=input("Enter your company = ")
        salary=int(input("enter your salary = "))
                          

        connection=pymysql.connect(host="localhost",user="root",password="root",db="iitnit")
        with connection.cursor() as cursor:
            sql="insert into company(id,name,company,salary) values(%s,%s,%s,%s)"
            try:
                cursor.execute(sql,(id,name,company,salary))
                connection.commit()
                print("Data Saved successfully")
            except Exception:
                traceback.print_exc()
    except Exception:
            traceback.print_exc()

for x in range(0,1):
    InsertData()