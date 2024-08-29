student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        mark = 'Outstanding'
    elif student_scores[key] > 80 and student_scores[key] < 91:
        mark = 'Exceeds Expectations'
    elif student_scores[key] > 70 and student_scores[key] < 81:
        mark = 'Acceptable'
    else:
        mark = 'Fail'
    student_grades[key] = mark

# 🚨 Don't change the code below 👇
print(student_grades)
