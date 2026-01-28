student_scores =[150,142,185,120,171,184,149,24,59,98,199,78,89,86]

highscore = student_scores[0]

for score in student_scores:
    if score > highscore:
        highscore = score

print(highscore)