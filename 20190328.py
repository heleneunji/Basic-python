for i in range(2,10):
    print("구구단 %d단 시작 ! "%i,end=' ')
    for j in range(1,10):
        print(i*j ,end=' ')
    print()

age=input('나이를 입력하세요')
high=input('키를 입력하세요')
if int(age) >10:  #if (age>=10) and (high>=165)
    if int(high) <165:
        print('놀이기구를 탈 수 없습니다')
    else:
        print('놀이기구를 탈 수 있습니다')
else:
    print('놀이기구를 탈 수 없습니다')

ID=['Kim','Lee','Park']
id=input('아이디: ')
if id not in ID:
    print('알 수 없는 사용자입니다')
else:
    password=input('패스워드: ')
    if password=='1234':
        print('환영합니다')
    else:
        print('잘못된 패스워드입니다')

import random
number = random.randint(1,100)
trytime=0
while True:
    trytime=trytime+1
    get=int(input('숫자를 입력하시오'))
    if get<number:
        print('낮음!')
    elif get>number:
        print('높음!')
    else:
        print('축하합니다','시도횟수=%d'%trytime)
        break

A=[70,60,55,75,95,90,80,80,85,100]
sum=0
for i in A:
    sum += i
avg = sum/len(A)
print('Average is %4.2f' %avg)

result=[n for n in A if n>=avg]
print('Scores above average are',result)