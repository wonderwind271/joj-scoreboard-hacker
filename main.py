# -*- coding: UTF-8 -*-
from unit_quire import *
import pandas as pd

base_url = input("please input the main page url of the course, for example, "
                 "https://joj.sjtu.edu.cn/d/ve280_summer_2022_paul/: ")
assignment = input("please input the homework id (not problem id) of the course, for example, "
                   "62d078c1dec511000876c05d: ")
problem = input("please input the problem id of the course, for example, "
                "62c77752dec511000876987b: ")
id_2020 = open("2020_id.txt", "r")
id_2021 = open("2021_id.txt", "r")
id_2019 = open("2019_id.txt", "r")
id_2018 = open("2018_id.txt", "r")
sel = input("please input the selection of students, in 18, 19, 20, 21 entry, for example, "
            "0011 means choose 20 and 21 entry: ")
all_id = []
if sel[0] == '1':
    all_id += id_2018.read().split('\n')
if sel[1] == '1':
    all_id += id_2019.read().split('\n')
if sel[2] == '1':
    all_id += id_2020.read().split('\n')
if sel[3] == '1':
    all_id += id_2021.read().split('\n')
data = []
for stud_id in all_id:
    (case_num, AC_count, score, state, username) = quire(stud_id, base_url, assignment, problem)
    if state == 3:
        print(f"student {stud_id} {username}: total case: {case_num}, accepted case: {AC_count}, score: {score}")
        data.append([stud_id, username, case_num, AC_count, score])
    elif state == 1:
        print(f"student {stud_id} {username}: compile error")
        data.append([stud_id, username, "compile error", 0, 0])
df = pd.DataFrame(data, index=range(1, len(data) + 1), columns=["sjtu id", "name", "total case", "AC case", "score"])
output_filename = input("please enter the csv name. Empty means abort. No need to add .csv: ")
if output_filename != "":
    df.to_csv(output_filename+".csv")
    print("data exported to "+output_filename+".csv")
else:
    print("data not exported")
