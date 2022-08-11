# joj-scoreboard-hacker
A tool to get scoreboard for a homework on [joj](https://joj.sjtu.edu.cn/) even if TA closed the scoreboard.



## prerequisites

python 3, together with python library

- requests
- pandas

install them with command

``` bash
pip3 install requests
pip3 install pandas
```



## how to use

Run the `main.py`, and then enter the prompt message

```bash
wonderwind@DESKTOP-53BM3RL:/mnt/c/Users/X1G8/Desktop/newrepo/joj-scoreboard-hacker$ python3 main.py
please input the main page url of the course, for example, https://joj.sjtu.edu.cn/d/ve280_summer_2022_paul/: https://joj.sjtu.edu.cn/d/ve280_summer_2022_paul/
please input the homework id (not problem id) of the course, for example, 62d078c1dec511000876c05d: 62d078c1dec511000876c05d
please input the problem id of the course, for example, 62c77752dec511000876987b:
```

enter the main page url, the hw id and the problem id. Main page url is the url of this course when you're at the main page. Homework id id is the id after the main page url when you click into a homework. For example, we can see the url of VE280 SU22 project 5 is https://joj.sjtu.edu.cn/d/ve280_summer_2022_paul/homework/62d078c1dec511000876c05d, so the homework id is "62d078c1dec511000876c05d".

Problem id is useful when a homework contains multiple problems. However, you can enter an empty line when the homework only contains one problem. Just as an example, the problem url of the VE280 SU22 project 5 is https://joj.sjtu.edu.cn/d/ve280_summer_2022_paul/homework/62d078c1dec511000876c05d/62c77752dec511000876987b, so the only problem's problem id is "62c77752dec511000876987b". You can of course, leave an empty message here.

Next, the program will ask you to enter the database of students.

```bash
please input the selection of students, in 18, 19, 20, 21 entry, for example, 0011 means choose 20 and 21 entry: 1110
```

Here, the input format is always $$a_1a_2a_3a_4$$, where $$a_i=0 \text{ or } 1$$ for $$i=1,2,3,4$$. When $$a_i=1$$, the corresponding grade (年级) of student is selected. For example, when we enter "1110" here, the student in 2018, 2019, 2020 entry are selected.

The program will then start to give students' score in this homework.

```
student 518370910034 金彤: total case: 85, accepted case: 85, score: 100.0
student 518370910107 ***: total case: 85, accepted case: 47, score: 55.294117647058826
student 518021910448 ***: total case: 85, accepted case: 16, score: 18.823529411764707
student 518021911016 ***: total case: 85, accepted case: 15, score: 17.647058823529413
student 518370990038 ***: total case: 85, accepted case: 85, score: 100.0
student 519370910050 ***: total case: 85, accepted case: 57, score: 67.05882352941177
...
```

The "***" here is the students' name. 

Note that the speed in one grade of student is determined by **the total number of students in that grade, not the total number that enrolled in this course**. Since very few students in 2018 entry choose VE280 this semester, we can see that the speed when one line of student's score is given at a lower speed than in 2020 entry.

Finally, when all the students' score are shown, you'll be prompt to export the data to a csv file.

```
student 520370910134 **: total case: 85, accepted case: 85, score: 100.0
student 520370910135 ***: total case: 85, accepted case: 46, score: 54.11764705882353
student 520370910142 ***: total case: 85, accepted case: 85, score: 100.0
please enter the csv name. Empty means abort. No need to add .csv: VE280_SU22_p5
data exported to VE280_SU22_p5.csv
```

Here, we can enter the name of the exported file. Here we enter "VE280_SU22_p5", and we get a csv file "VE280_SU22_p5.csv" in the current folder with all the data above.

If you do not want the csv, just enter an empty line, and the csv will not be generated. 



## further notice

The speed is subject to your internet speed and joj server's respond speed. It's not related to your CPU.

The principle of this program is to take advantage of joj's "recent submission" function, and try each student in the database.

Do not abuse it since it may burden the joj server.

Also, it seems that the joj will be upgraded. I'm not sure if this will still work at that time.
