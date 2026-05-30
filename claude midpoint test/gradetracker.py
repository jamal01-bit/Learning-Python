studentlist = []
scorelist = []
while True:
 name = input("Enter student name (or 'done'): ")
 if (name == 'done' or name == 'Done'):
  break
 else: 
  score = int(input(f"Score for {name}: "))
  studentlist.append(name)
  scorelist.append(score)
highestscore = 0
topstudent = ''
grade = ''
for i in range(len(scorelist)):
 score = scorelist[i]
 if (score > highestscore):
  highestscore = score
  topstudent = studentlist[i]
 if score >= 90:
   grade = 'A'
 elif (score >= 80):
   grade = 'B'
 elif (score >= 70):
   grade ='C'
 elif (score >= 60):
   grade = 'D'
 elif (score < 60):
   grade = 'F'
 print('Name         Score    Grade')
 print(f'{studentlist[i]}           {scorelist[i]}       {grade}')
print(f'Class Average: {round(sum(scorelist) / len(scorelist), 1)}')
print(f'Top student: {topstudent}') 
