def func(a=8,b=9):
    y=100*a+10*b+1
    return y
print(func(3,5))
print(func(3))
print(func())

def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a
A,B=bigger(28,463)
print('첫번째 정수 : ',A)
print('두번째 정수 : ',B)

def circle(a):
    pi=3.14
    return 2*a*pi,a*a*pi
for a in (10,15,20):
    round, square = circle(a)
    print('반지름이 %3d 인 원의 둘레는 %8.2f 입니다.'%(a,round))
    print('반지름이 %3d 인 원의 넓이는 %8.2f 입니다.'%(a,square))

print((lambda a,b: (a,b)if a>b else(b,a))(20,10))

f=open('새파일.txt','w')
for i in range(1,11):
    data='%d번째 줄입니다.\n'%i
    f.write(data)
f.close()

for i in range(1,11):
    data='%d번째 줄입니다.'%i
    print(data)

f=open('새파일.txt','r')
data=f.read()
print(data)
f.close

f=open('새파일.txt','a')
for i in range(11,20):
    data='%d 번째 줄입니다.\n'%i
    f.write(data)
f.close()

f=open('phones.txt','w')
data="""눈송이 010-1234-5678
꽃송이 010-1234-5679
별송이 010-1234-5680
"""
f.write(data)
f.close()

f=open('phones.txt','r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f=open('phones.txt','r')
lines=f.readlines()
print(lines)
f.close()

f=open('phones.txt','r')
liness=f.read()
print(liness)
f.close()

f=open('phones.txt','a')
data='꿀송이 010-1234-5681 \n'
f.write(data)
f.close()

f=open('phones.txt','r')
liness=f.read()
print(liness)
f.close()
