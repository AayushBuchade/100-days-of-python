student_scores =[150,142,185,120,171,184,149,24,59,98,199,78,89,86]
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


max_score = student_scores[0]
for score in student_scores:
    if score > max_score:
        max_score = score

print(f'The highest score in the class is: {max_score}')
