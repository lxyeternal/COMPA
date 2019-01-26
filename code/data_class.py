# _coding:utf-8_*_
import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("../data/H-data/WV - H.xlsx")
'''
data/H-data/OH - H.xlsx
data/H-data/KY - H.xlsx
data/H-data/PA - H.xlsx
data/H-data/VA - H.xlsx
data/H-data/WV - H.xlsx
'''
sheet = book.sheet_by_name("Data")
countycount = []
listcounty_name = []
list_rate_county = []
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(0, sheet.nrows):

    county = str(sheet.cell(r,2).value)
    listcounty_name.append(county)
setlistcounty_name = list(set(listcounty_name))
setlistcounty_name.sort(key=listcounty_name.index)
for i in setlistcounty_name:
    countycount.append(listcounty_name.count(i))
# print (countycount)
# print(listcounty_name)
# print (setlistcounty_name)

txt = open('../txt/H-TXT/WV-H.txt', 'w')
count = 0
for i in countycount:

    one_county_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for r in range(count, count + i):

        year = int(sheet.cell(r, 0).value)
        state = str(sheet.cell(r, 1).value)
        countyname = str(sheet.cell(r, 2).value)
        dragnum = float(sheet.cell(r, 4).value)
        dragcountynum = int(sheet.cell(r, 5).value)
        rate_county = dragnum / dragcountynum
        # print (year,state,countyname,dragnum,dragcountynum,rate_county)

        if year == 2010:
            one_county_list[0] = rate_county
        if year == 2011:
            one_county_list[1] = rate_county
        if year == 2012:
            one_county_list[2] = rate_county
        if year == 2013:
            one_county_list[3] = rate_county
        if year == 2014:
            one_county_list[4] = rate_county
        if year == 2015:
            one_county_list[5] = rate_county
        if year == 2016:
            one_county_list[6] = rate_county
        if year == 2017:
            one_county_list[7] = rate_county

        one_county_list[8] = countyname
        one_county_list[9] = state

    count = count + i
    list_rate_county.append(one_county_list)

    for k in one_county_list:
        txt.write(str(k))
        txt.write('    ')
    txt.write('\n')
txt.close()

print (list_rate_county)



