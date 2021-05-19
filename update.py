import pymysql
import traceback

def UpdateData():
    try:
        id=eval(input("Enter your ID = "))
        name=input("Enter your Name = ")
        company=input("Enter your company = ")
        salary=int(input("enter your salary = "))
    
        connection=pymysql.connect(host="localhost",user="root",password="root",db="iitnit")
        with connection.cursor() as cursor:
            sql="update company set name=%s,company=%s,salary=%s where id=%s"
            
            #sql="insert into unit(ID,CITY,CAPACITY) values(%s,%s,%s)"
            try:
                cursor.execute(sql,(name,company,salary,id))
                connection.commit()
                print("Data Updated successfully")
            except Exception:
                traceback.print_exc()
    except Exception:
            traceback.print_exc()

UpdateData()