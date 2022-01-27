# -*- coding: utf-8 -*-
import shutil
from os.path import getctime
import os
import datetime

def data_int(st):
    d1 = st.split(":")
    if(len(d1) == 2):
        ch = int(d1[0]) * 3600
        mi = int(d1[1]) * 60
    else:
        print(st)
    return ch + mi
path_log = "log.txt"
def write_log(text):
    with open(path_log, "a") as file:
        file.write(text)

path = "sorted files.txt"
file_path = ""

if __name__ == "__main__":
    d3 = []
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    d2 = data.split("\n")
    prom = d2[0].split("|")
    file_path = prom[0]
    ras = prom[1:]
    for i in range(len(d2)):
        if d2[i] != "":
            a = d2[i].strip()
            a = a.split("|")
            if len(a) == 5 and i != 0:
                a[2] = data_int(a[2])
                a[3] = data_int(a[3])
                d3.append(a)
    file_list = os.listdir(file_path)
    for i in range(len(file_list)):
        if file_list[i][-3:] in ras or len(ras) == 0 or ras == [""]:
            f1 = file_path+"\\"+file_list[i]
            f3 = str(datetime.datetime.fromtimestamp(getctime(f1)).date())
            f4 = str(datetime.datetime.fromtimestamp(getctime(f1)).strftime('%H:%M'))#время
            f5 = str(datetime.datetime.fromtimestamp(getctime(f1)).strftime('%w'))# день недели
            f4 = data_int(f4)
            for i2 in range(len(d3)):
                if d3[i2][1] == f5 and (f4>d3[i2][2] and f4 <  d3[i2][3]):
                    ff = d3[i2][4] + "\\" +f3
                    if not os.path.isdir(ff):
                        os.mkdir(ff)
                        write_log(f"папка {f3} создана в директории {d3[i2][4]}\n")
                    shutil.move(f1,ff)
                    write_log(f"\t{file_list[i]} перемещён в {ff} \n")
    
   
