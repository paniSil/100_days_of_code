target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
res = 0
for n in range(0, target+1, 2):
    res += n

print(res)
