import pymysql
from python_file import glb
conn = pymysql.connect(host=glb.get_value("MYSQL_IP"), user = "root", passwd="caoqiming6666", db="hospital_management", port=3306, charset="utf8")
cur = conn.cursor()
cur.execute("desc 专家系统结果")

result = cur.fetchall()
print(result)
conn.commit()

print(globals())


cur.close()
conn.close()