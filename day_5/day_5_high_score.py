# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

res = student_scores[0]
for n in student_scores:
    if n > res:
        res = n
    else:
        continue

print('The highest score in the class is:', res)
