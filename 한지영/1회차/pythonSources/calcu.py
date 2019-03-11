# 숫자1 입력받는다
# 연산자 입력 받는다.
# 숫자2 입력 받는다.
# 계산한다
# - 만약에 연산자가 +이면, 숫자 1과 2를 더한다.

number1 = input('숫자 1 : ')
number1 = int(number1)

operator = input('연산자 : ')

number2 = input('숫자 2 : ')
number2 = int(number2)

result = 0
if operator == "+":
    result = number1 + number2
elif operator == "*":
    result = number1 * number2
elif operator == "-":
    result = number1 - number2
elif operator == "/":
    result = number1 / number2
else:
    print('제공되지 않는 기능입니다.')

print(result)
