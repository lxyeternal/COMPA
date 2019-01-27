# _coding:utf-8_*_
import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("../data/year-data/2017/WV.xlsx")
'''
data/H-data/OH - H.xlsx
data/H-data/KY - H.xlsx
data/H-data/PA - H.xlsx
data/H-data/VA - H.xlsx
data/H-data/WV - H.xlsx
'''
sheet = book.sheet_by_name("Sheet1")
countycount = []
listcounty_name = []
list_rate_county = []
sumcounty = []
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):

    county = str(sheet.cell(r,2).value)
    listcounty_name.append(county)
setlistcounty_name = list(set(listcounty_name))
setlistcounty_name.sort(key=listcounty_name.index)

for i in setlistcounty_name:
    countycount.append(listcounty_name.count(i))

print (countycount)
print(listcounty_name)
print (setlistcounty_name)

count = 1
for i in countycount:

    for j in range(count,count + i ):

        drugnum = int(sheet.cell(j, 8).value)
        print (drugnum)

    count = count + i
    sumcounty.append(drugnum)

txt = open('../txt/Y-TXT/2017/WV.txt', 'w')
for i in range(len(countycount)):
        print (setlistcounty_name[i])
        txt.write(setlistcounty_name[i])
        txt.write('    ')
        txt.write(str(sumcounty[i]))
        txt.write('\n')
txt.close()




