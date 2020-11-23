grades = [[50,90,60],[15,60,75],[99,95,91]]
first_av = 0
second_av = 0
third_av = 0
for i in grades[0]:
  first_av += i
f_f = (first_av * 3) / 10 
for i in grades[1]: 
  second_av += i
f_s = (second_av * 3) / 10 
for i in grades[2]:
  third_av += i
f_t = (third_av * 4) / 10
av_grade = f_f + f_s + f_t
print(av_grade) 