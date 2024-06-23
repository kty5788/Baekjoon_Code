ans = ''
number, nota = map(int,input().split())

while number != 0:
    if 55 + number % nota >= 65:
        ans += chr(55+ number % nota)
    else:
        ans += str(number % nota)
    number //= nota

print(ans[::-1])