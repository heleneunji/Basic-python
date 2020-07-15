def square (a):
    return a*a
a=3
print(square(a))

def bigger (a,b):
    if a>b:
        return a
    else:
        return b
b=40
c=70
print(bigger(b,c))


def hello():
    print("""안녕 파이썬
    즐거운 코딩시간이야""")
hello()
def goodbye():
    print ("""파이썬 어렵지않아
    다음 시간에 또 만나요""")
goodbye()

def how_old_are_you(year):
    age=2019-year+1
    print('%d년생:'%year,end='')
    print('올해 %d살 입니다.'%age)
how_old_are_you(1998)

def is_even(a):
    if int(a)%2==0:
        return True
    else:
        return False
print(is_even(40))

def average(*group):
    sum=0
    for i in group:
        sum = sum+i
    return sum/len(group)
print(average(30,60,90,20))

print('챗봇> 안녕하세요')
print('챗봇> 나는 인공지능 채팅 로봇입니다.')
name=input("""챗봇> 당신의 이름은 무엇인가요?'
사람> """)
print('챗봇> ' ,name ,'씨 만나서 반가워요')
place=input("""챗봇> 당신의 고향은 어디인가요?'
사람> """)
print('챗봇> ',name,' 씨는 아름다운 ',place,' 에서 왔군요')
print('챗봇> 안녕 다음에 또 만나요')