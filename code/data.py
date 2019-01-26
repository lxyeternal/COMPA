# _coding:utf-8_*_
import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("../data/H-data/WV - H.xlsx")
sheet = book.sheet_by_name("Data")
#建立一个MySQL连接
conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='1011',
        db='usa',
        port=3306,
        charset='utf8'
        )
# 获得游标
cur = conn.cursor()
# 创建插入SQL语句
query = 'insert into test (year,state,county,drag_name,dragnum,dragcountynum,dragstatenum) values (%s, %s, %s, %s, %s, %s, %s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(0, sheet.nrows):
    year      = int(sheet.cell(r,0).value)
    state       = str(sheet.cell(r,1).value)
    county          = str(sheet.cell(r,2).value)
    drag_name     = str(sheet.cell(r,3).value)
    dragnum       = int(sheet.cell(r,4).value)
    dragcountynum = int(sheet.cell(r,5).value)
    dragstatenum = int(sheet.cell(r,6).value)
    values = (year,state,county,drag_name,dragnum,dragcountynum,dragstatenum)
    print (values)
      # 执行sql语句
    cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")