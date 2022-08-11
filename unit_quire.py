# -*- coding: UTF-8 -*-
import requests


def quire(stud_id, base_url, assignment, problem):
    '''
    :param stud_id: student's sjtu id
    :param base_url: the main page url of this course
    :param assignment: the id of the homework (not sub-problem)
    :param problem: the id of the sub-problem
    :return: a tuple (case_num, AC_count, score, state, name), state 1: Compile error, 2: not found, 3: get score
    '''
    # start search process
    url = base_url + "records?uid_or_name=" + str(stud_id) + "&pid="+problem+"&tid=" + assignment
    r = requests.get(url)  # can use param, but let's be straightforward here
    res1 = str(r.content)
    place1 = res1.find("data-rid")  # place==-1 means id not found. will be tackled later
    place_start = res1.find('\"', place1)
    place_end = res1.find('\"', place_start + 1)
    link_id = res1[place_start + 1:place_end]
    url_score_page = base_url + "records/" + link_id
    # print(url_score_page)  # link to the first record of the student in this assignment. It's the sentence test
    r2 = requests.get(url_score_page)
    res2 = str(r2.content, 'utf8')
    # get username
    username = ""
    place_user_label = res2.find("user-profile-name")
    if place_user_label>=0:
        l1 = res2.find(">", place_user_label)
        l2 = res2.find("<", l1)
        username = res2[l1+1:l2]
    # count ac and all results. if "Compile Error" is found, get 0 directly
    if(res2.count("Compile Error")):
        # print("compile error")
        return (0, 0, 0, 1, username)
    AC_count = res2.count("icon pass")
    count = res2.count("icon pass") + res2.count("icon fail")
    if AC_count == count:
        AC_count -= 1
        count -= 1
    else:
        count -= 1
    if count <= 0:  # student not found
        return (-1, -1, -1, 2, username)
    score = 100 * AC_count / count
    # print(f"total case: {count}, accepted case: {AC_count}, score: {score}")
    return (count, AC_count, score, 3, username)
