#_*_coding:utf-8_*_
import csv
import os
import random

cannel = []
remove_list = [1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 4, 1, 2, 1, 1, 5, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 3, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 4, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 2, 1, 1, 3, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 3, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 4, 4, 4, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2]
def Reader(filepath,d_path,e_path,num1,num2):

    data_scv = open(filepath,'r')
    reader = csv.reader(data_scv)
    remove = [65, 66, 69, 70, 71, 72, 73, 74, 75, 76]
    die_char = ['-','**','*****','+','***']
    one_d_info = []
    one_e_info = []
    county_name = []
    # cannel_d_list = []
    # cannel_e_list = []
    # cannel_de_list = []
    csvstart = 3
    txtstart = 4
    d = open(d_path,'w')
    e = open(e_path,'w')

    for i in reader:

        if len(i[3]) > 8:
            continue
        len_data = len(i)
        county_name.append(i[3])
        d_data = []
        e_data = []
        num_reader = int(len_data/4)
        print (num_reader)

        for j in range(num_reader):

            if j in remove:
                continue

            csv_start = csvstart + j*4
            txt_start = txtstart + j*4
            # print (csv_start,txt_start)

            if i[csv_start] != '(X)' and i[txt_start] != '(X)':

                if i[csv_start] == '0':
                    i[csv_start] = random.randint(100,200)
                if i[csv_start] in die_char  or i[txt_start] in die_char:
                    i[csv_start] = num1
                    i[txt_start] = num2
                # if i[csv_start] == '-' or i[csv_start] == '**' or i[csv_start] == '*****' or i[txt_start] == '-' or i[txt_start] == '**' or i[txt_start]:
                #     i[csv_start] = 0
                #     i[txt_start] = 0
                d_data.append(i[csv_start])
                e_data.append(i[txt_start])
            else:
                cannel.append(j)
                # cannel_e_list.append(txt_start)
                continue
        # cannel_de_list.append(cannel_d_list)
        # cannel_de_list.append(cannel_e_list)
        one_d_info.append(d_data)
        one_e_info.append(e_data)

    # cannel.append(cannel_de_list)
    # print (cannel)
    # print (len(one_d_info[1]))
    # print (len(one_e_info[1]))
    count = 0
    for m in range(len(remove_list)):
        for k in range(len(one_d_info[count])):
            d.write(str(one_d_info[count][k]))
            d.write('    ')
            e.write(str(one_e_info[count][k]))
            e.write('    ')
        d.write('\n')
        e.write('\n')
        count = count + remove_list[m]
    d.close()
    e.close()

#   获取当前路径下的所有csv文件路径
def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
        for i in list_name:
            if i == '..//data//csv-data/.DS_Store' or  i == '..//txt//C-TXT/.DS_Store':
                list_name.remove(i)


if __name__ == '__main__':

    path_csv = '..//data//csv-data'
    path_txt = '..//txt//C-TXT'
    prefex_name = '../data/csv-data'
    dir_csv_name = []
    dir_txt_name = []
    listdir(path_csv,dir_csv_name)
    listdir(path_txt,dir_txt_name)
    dir_csv_name = sorted(dir_csv_name)
    dir_txt_name = sorted(dir_txt_name)

    for i in range(len(dir_csv_name)):
        print ("______")
        num1 = 100 + i
        num2 = 10+i
        csv_path_name = dir_csv_name[i]
        txt_d_path_name = dir_txt_name[2*i]
        txt_e_path_name = dir_txt_name[2*i+1]
        Reader(csv_path_name,txt_d_path_name,txt_e_path_name,num1,num2)



