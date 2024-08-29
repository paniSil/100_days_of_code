# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
height = 0
sum = 0
for h in student_heights:
    height += h
    sum += 1
res = round(height/sum)

print("total height =", height)
print("number of students =", sum)
print("average height =", res)
