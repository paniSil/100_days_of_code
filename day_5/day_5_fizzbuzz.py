# Write your code here 👇
for n in range(1, 101):
    if not n % 3 == 0 and not n % 5 == 0:
        print(n)
    elif n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
