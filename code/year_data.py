# _coding:utf-8_*_
import xlrd
import pymysql
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook("../data/year-data/year/2016.xlsx")

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

print (len(countycount))
print(listcounty_name)
print (setlistcounty_name)

count = 1
all_sum = []
all_rate = []
for i in countycount:
    onesum = 0
    for j in range(count,count + i ):
        onesum = onesum + int(sheet.cell(j, 7).value)
        drugnum = int(sheet.cell(j, 8).value)
        # print (drugnum)
    all_sum.append(onesum)
    count = count + i
    sumcounty.append(drugnum)

for i in range(len(all_sum)):
    all_rate.append(float(all_sum[i])/sumcounty[i])
setlistcounty_name = ['ACCOMACK', 'ADAIR', 'ADAMS', 'ALBEMARLE', 'ALEXANDRIA CITY', 'ALLEGHANY', 'ALLEGHENY', 'ALLEN', 'AMELIA', 'AMHERST', 'ANDERSON', 'APPOMATTOX', 'ARLINGTON', 'ARMSTRONG', 'ASHLAND', 'ASHTABULA', 'ATHENS', 'AUGLAIZE', 'AUGUSTA', 'BALLARD', 'BARBOUR', 'BARREN', 'BATH', 'BEAVER', 'BEDFORD', 'BEDFORD CITY', 'BELL', 'BELMONT', 'BERKELEY', 'BERKS', 'BLAIR', 'BLAND', 'BOONE', 'BOTETOURT', 'BOURBON', 'BOYD', 'BOYLE', 'BRACKEN', 'BRADFORD', 'BRAXTON', 'BREATHITT', 'BRECKINRIDGE', 'BRISTOL', 'BROOKE', 'BROWN', 'BRUNSWICK', 'BUCHANAN', 'BUCKINGHAM', 'BUCKS', 'BUENA VISTA CITY', 'BULLITT', 'BUTLER', 'CABELL', 'CALDWELL', 'CALHOUN', 'CALLOWAY', 'CAMBRIA', 'CAMERON', 'CAMPBELL', 'CARBON', 'CARLISLE', 'CAROLINE', 'CARROLL', 'CARTER', 'CASEY', 'CENTRE', 'CHAMPAIGN', 'CHARLOTTE', 'CHARLOTTESVILLE CITY', 'CHESAPEAKE CITY', 'CHESTER', 'CHESTERFIELD', 'CHRISTIAN', 'CLARION', 'CLARK', 'CLARKE', 'CLAY', 'CLEARFIELD', 'CLERMONT', 'CLINTON', 'COLONIAL HEIGHTS CITY', 'COLUMBIA', 'COLUMBIANA', 'COSHOCTON', 'CRAIG', 'CRAWFORD', 'CRITTENDEN', 'CULPEPER', 'CUMBERLAND', 'CUYAHOGA', 'DANVILLE CITY', 'DARKE', 'DAUPHIN', 'DAVIESS', 'DEFIANCE', 'DELAWARE', 'DICKENSON', 'DINWIDDIE', 'DODDRIDGE', 'EDMONSON', 'ELK', 'ELLIOTT', 'EMPORIA CITY', 'ERIE', 'ESSEX', 'ESTILL', 'FAIRFAX', 'FAIRFAX CITY', 'FAIRFIELD', 'FALLS CHURCH CITY', 'FAUQUIER', 'FAYETTE', 'FLEMING', 'FLOYD', 'FLUVANNA', 'FOREST', 'FRANKLIN', 'FRANKLIN CITY', 'FREDERICK', 'FREDERICKSBURG CITY', 'FULTON', 'GALAX CITY', 'GALLATIN', 'GALLIA', 'GARRARD', 'GEAUGA', 'GILES', 'GLOUCESTER', 'GOOCHLAND', 'GRANT', 'GRAVES', 'GRAYSON', 'GREEN', 'GREENBRIER', 'GREENE', 'GREENSVILLE', 'GREENUP', 'GUERNSEY', 'HALIFAX', 'HAMILTON', 'HAMPTON CITY', 'HANCOCK', 'HANOVER', 'HARDIN', 'HARDY', 'HARLAN', 'HARRISON', 'HARRISONBURG CITY', 'HART', 'HENDERSON', 'HENRICO', 'HENRY', 'HIGHLAND', 'HOCKING', 'HOLMES', 'HOPEWELL CITY', 'HOPKINS', 'HUNTINGDON', 'HURON', 'INDIANA', 'ISLE OF WIGHT', 'JACKSON', 'JAMES CITY', 'JEFFERSON', 'JESSAMINE', 'JOHNSON', 'JUNIATA', 'KANAWHA', 'KENTON', 'KING GEORGE', 'KING WILLIAM', 'KNOTT', 'KNOX', 'LACKAWANNA', 'LAKE', 'LANCASTER', 'LARUE', 'LAUREL', 'LAWRENCE', 'LEBANON', 'LEE', 'LEHIGH', 'LESLIE', 'LETCHER', 'LEWIS', 'LEXINGTON CITY', 'LICKING', 'LINCOLN', 'LIVINGSTON', 'LOGAN', 'LORAIN', 'LOUDOUN', 'LOUISA', 'LUCAS', 'LUNENBURG', 'LUZERNE', 'LYCOMING', 'LYNCHBURG CITY', 'LYON', 'MADISON', 'MAGOFFIN', 'MAHONING', 'MANASSAS CITY', 'MARION', 'MARSHALL', 'MARTIN', 'MARTINSVILLE CITY', 'MASON', 'MATHEWS', 'MCCRACKEN', 'MCCREARY', 'MCDOWELL', 'MCKEAN', 'MCLEAN', 'MEADE', 'MECKLENBURG', 'MEDINA', 'MEIGS', 'MENIFEE', 'MERCER', 'METCALFE', 'MIAMI', 'MIDDLESEX', 'MIFFLIN', 'MINERAL', 'MINGO', 'MONONGALIA', 'MONROE', 'MONTGOMERY', 'MONTOUR', 'MORGAN', 'MORROW', 'MUHLENBERG', 'MUSKINGUM', 'NELSON', 'NEW KENT', 'NEWPORT NEWS CITY', 'NICHOLAS', 'NOBLE', 'NORFOLK CITY', 'NORTHAMPTON', 'NORTHUMBERLAND', 'NORTON CITY', 'NOTTOWAY', 'OHIO', 'OLDHAM', 'ORANGE', 'OTTAWA', 'OWEN', 'OWSLEY', 'PAGE', 'PATRICK', 'PAULDING', 'PENDLETON', 'PERRY', 'PETERSBURG CITY', 'PHILADELPHIA', 'PICKAWAY', 'PIKE', 'PITTSYLVANIA', 'POCAHONTAS', 'POQUOSON CITY', 'PORTAGE', 'PORTSMOUTH CITY', 'POTTER', 'POWELL', 'POWHATAN', 'PREBLE', 'PRESTON', 'PRINCE EDWARD', 'PRINCE GEORGE', 'PRINCE WILLIAM', 'PULASKI', 'PUTNAM', 'RADFORD', 'RALEIGH', 'RANDOLPH', 'RAPPAHANNOCK', 'RICHLAND', 'RICHMOND', 'RITCHIE', 'ROANE', 'ROANOKE', 'ROBERTSON', 'ROCKBRIDGE', 'ROCKCASTLE', 'ROCKINGHAM', 'ROSS', 'ROWAN', 'RUSSELL', 'SALEM', 'SANDUSKY', 'SCHUYLKILL', 'SCIOTO', 'SCOTT', 'SENECA', 'SHELBY', 'SHENANDOAH', 'SIMPSON', 'SMYTH', 'SNYDER', 'SOMERSET', 'SOUTHAMPTON', 'SPENCER', 'SPOTSYLVANIA', 'STAFFORD', 'STARK', 'STAUNTON CITY', 'SUFFOLK CITY', 'SULLIVAN', 'SUMMERS', 'SUMMIT', 'SURRY', 'SUSQUEHANNA', 'SUSSEX', 'TAYLOR', 'TAZEWELL', 'TIOGA', 'TODD', 'TRIGG', 'TRIMBLE', 'TRUMBULL', 'TUCKER', 'TUSCARAWAS', 'TYLER', 'UNION', 'UPSHUR', 'VAN WERT', 'VENANGO', 'VINTON', 'VIRGINIA BEACH CITY', 'WARREN', 'WASHINGTON', 'WAYNE', 'WAYNESBORO CITY', 'WEBSTER', 'WESTMORELAND', 'WETZEL', 'WHITLEY', 'WILLIAMS', 'WILLIAMSBURG CITY', 'WINCHESTER CITY', 'WIRT', 'WISE', 'WOLFE', 'WOOD', 'WOODFORD', 'WYANDOT', 'WYOMING', 'WYTHE', 'YORK']
txt = open('../txt/N-TXT/2016.txt', 'w')
for i in range(351):
        # print (setlistcounty_name[i])
        txt.write(setlistcounty_name[i].title())
        txt.write('    ')
        try:
            txt.write(str(sumcounty[i]))
            txt.write('    ')
            txt.write(str(all_sum[i]))
            txt.write('    ')
            txt.write(str(all_rate[i]))
        except IndexError:
            txt.write('    ')
            txt.write('    ')
            txt.write('    ')
            txt.write('    ')
            txt.write('    ')
        txt.write('\n')
txt.close()




