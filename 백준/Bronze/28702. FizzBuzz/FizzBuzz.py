first = input()
second = input()
third = input()
li = [first,second,third]
for i in range(1,len(li)+1):
    if li[i-1].isdigit():
        ans = int(li[i-1])+(4-i)

if ans % 3 == 0 and ans % 5 == 0:
    print('FizzBuzz')
elif ans % 3 == 0:
    print('Fizz')
elif ans % 5 == 0:
    print('Buzz')
else:
    print(ans)