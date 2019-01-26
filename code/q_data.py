# _coding:utf-8_*_
import xlrd

'''
data/Q-data/OH - Q.xlsx
data/Q-data/KY - Q.xlsx
data/Q-data/PA - Q.xlsx
data/Q-data/VA - Q.xlsx
data/Q-data/WV - Q.xlsx

'''

book = xlrd.open_workbook("../data/Q-data/WV - Q.xlsx")
sheet = book.sheet_by_name("Data")

listcounty_name = []
countycount = []
list_rate_county = []

for r in range(0, sheet.nrows):

    county = str(sheet.cell(r,2).value)
    listcounty_name.append(county)

setlistcounty_name = list(set(listcounty_name))
setlistcounty_name.sort(key=listcounty_name.index)

for i in setlistcounty_name:
    countycount.append(listcounty_name.count(i))

# print (listcounty_name)
# print (setlistcounty_name)
# print (countycount)

count = 0
txt = open('../txt/Q-TXT/WV-Q.txt', 'w')
for i in countycount:

    one_county_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    rate_qlist = [0,0,0,0,0,0,0,0]
    num = [1,1,1,1,1,1,1,1]

    for r in range(count, count + i):

        year = int(sheet.cell(r, 0).value)
        state = str(sheet.cell(r, 1).value)
        countyname = str(sheet.cell(r, 2).value)
        dragnum = float(sheet.cell(r, 4).value)
        dragcountynum = int(sheet.cell(r, 5).value)

        print (year,state,countyname,dragnum,dragcountynum)

        if year == 2010:
            rate_qlist[0] = dragnum + rate_qlist[0]
            num[0] = dragcountynum
        if year == 2011:
            rate_qlist[1] = dragnum + rate_qlist[1]
            num[1] = dragcountynum
        if year == 2012:
            rate_qlist[2] = dragnum + rate_qlist[2]
            num[2] = dragcountynum
        if year == 2013:
            rate_qlist[3] = dragnum + rate_qlist[3]
            num[3] = dragcountynum
        if year == 2014:
            rate_qlist[4] = dragnum + rate_qlist[4]
            num[4] = dragcountynum
        if year == 2015:
            rate_qlist[5] = dragnum + rate_qlist[5]
            num[5] = dragcountynum
        if year == 2016:
            rate_qlist[6] = dragnum + rate_qlist[6]
            num[6] = dragcountynum
        if year == 2017:
            rate_qlist[7] = dragnum + rate_qlist[7]
            num[7] = dragcountynum

        one_county_list[8] = countyname
        one_county_list[9] = state

    for k in range(8):

        one_county_list[k] = rate_qlist[k]/num[k]

    count = count + i
    print (i)
    print (count)
    list_rate_county.append(one_county_list)

    for k in one_county_list:
        txt.write(str(k))
        txt.write('    ')
    txt.write('\n')
txt.close()

print (list_rate_county)

