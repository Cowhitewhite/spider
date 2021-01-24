import sqlite3


# conn = sqlite3.connect("test.db") # 打开或创建数据库文件
# print("open database....")
# c = conn.cursor()
# sql = '''
#     create table test
#       (id int primary key not null,
#       name text not null,
#       age int not null,
#       address char(500),
#       salary real);
# '''
# c.execute(sql)
# conn.commit()
# conn.close()
# print("table complete....")



# 插入数据
# conn = sqlite3.connect("test.db") # 打开或创建数据库文件
# print("open database....")
# c = conn.cursor()
# sql = '''
#      insert into test(id,name,age,address,salary) values
#      (1,"张三","123","test",8000);
# '''
# c.execute(sql)
# conn.commit()
# conn.close()
# print("table complete....")

# 查询数据
conn = sqlite3.connect("test.db") # 打开或创建数据库文件
print("open database....")
c = conn.cursor()
sql = '''
     select * from test
'''
cursor = c.execute(sql)
for row in cursor:
    print(row)
conn.close()
print("table complete....")