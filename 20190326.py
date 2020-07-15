number=int(input('수를 입력하세요 : '))
print(number,'을(를) 입력하셨습니다')
if number<0:
    print('판별할 수 없는 수를 입력하셨습니다')
elif number % 2 == 0:
        print(number,'은(는) 짝수입니다')
else:
        print((number,'은(는) 홀수입니다'))

treehit=0
while treehit < 10:
    treehit = treehit+1
    print('나무를 %d번 찍었습니다.'%treehit)
    if treehit==10:
        print('나무 넘어갑니다.')

prompt="""
1. Add
2. Del
3. List
4. Quit
Enter number."""
number=0
while number !=4:
    print(prompt)
    number = int(input())

coffee = 3
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피의 양은 %d입니다" %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break

coffee=3
while True:
    money = int(input('돈을 넣어 주세요:'))
    if money==300:
        print('커피를 줍니다')
        coffee = coffee - 1
        print('남은 커피의 양은 %d잔입니다' %coffee)
    elif money<300:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.')
        print('남은 커피의 양은 %d잔입니다' % coffee)
    elif money>300:
        print('거스름돈',money-300,'을(를) 주고 커피를 줍니다.')
        coffee = coffee - 1
        print('남은 커피의 양은 %d잔입니다' % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break

i=0
while i < 6:
    print('*'*i)
    i=i+1