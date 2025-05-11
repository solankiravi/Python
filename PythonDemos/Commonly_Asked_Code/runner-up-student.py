students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
second_lowest_score = sorted(set([student[1] for student in students]))[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_score]
second_lowest_students.sort()
print('\n'.join(second_lowest_students))
