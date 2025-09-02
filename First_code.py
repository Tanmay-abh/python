students_score = []
students_score.append(85)
students_score.append(90)
students_score.append(78)
students_score.append(92)
students_score.append(88)
print(students_score)
students_score.insert(2, 80)
print(students_score)
students_score.remove(92)
print(students_score)
students_score.sort()
print(students_score)
students_score.reverse()
print(students_score)
max_score = max(students_score)
min_score = min(students_score)
print("max_score:", max_score)
print("min_score:", min_score)
if 90 in students_score:
    print("90 is in the list")
else:
    print("90 is not in the list")
total = len(students_score)
print(total)
last_three = students_score[-3:]
print(last_three)
last = students_score[-1]
print(last)
students_score[2] = 50
print(students_score)
new_scores = students_score.copy()
print(new_scores)