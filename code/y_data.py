import csv
import os


def get_county():

    csv_county_path = '../data/1.csv'
    csv_reader = open(csv_county_path,'r')
    reader = csv.reader(csv_reader)
    csv_county_list = []
    for i in reader:
        csv_county_list.append(i[0])
    return csv_county_list

def deal_county(list_county):

    for i in range(len(list_county)):
        list_county[i] = list_county[i].split(' ')[0]

    for k in range(len(list_county)):
        list_county[k] = list_county[k].title()
    return list_county


if __name__ == '__main__':

    countycount = []
    csv_list_county = get_county()
    deal_list_county = deal_county(csv_list_county)
    print (deal_list_county)
    setlistcounty_name = list(set(deal_list_county))
    setlistcounty_name.sort(key=deal_list_county.index)
    for i in setlistcounty_name:
        countycount.append(deal_list_county.count(i))
    print (setlistcounty_name)
    print (len(setlistcounty_name))

    writefile = open('../txt/N-TXT/countyname.txt','w')
    for i in deal_list_county:
        writefile.write(str(i))
        writefile.write('\n')
    writefile.close()
    print ('OK')
