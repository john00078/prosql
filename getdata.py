import pymysql
import traceback
def getData():
    result=""
    try:
        connection=pymysql.connect(host="localhost",user="root",password="root",db="iitnit")
        with connection.cursor() as cursor:
            sql="select * from company"
            try:
                cursor.execute(sql)
                result=cursor.fetchall()                
            except Exception:
                traceback.print_exc()
    except Exception:
            traceback.print_exc()
    return result
dataList=getData()
print("id name company salary")
for list in dataList:
    print(list[0], list[1], list[2], list[3])