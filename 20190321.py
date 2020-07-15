a=input('첫 번째 단어를 입력하세요: ')
b=input('두 번째 단어를 입력하세요: ')
c=input('세 번째 단어를 입력하세요: ')
d=a[0]+b[0]+c[0]
e=d.upper()
print('입력한 단어들의 약자는?',e)

f=input('이메일 주소를 입력하세요: ')
print('이메일 주소 = ',f)
g=f.split('@')
h=g[0]
i=g[1]
print('아이디 = ',h)
print('도메인 = ',i)

j=input('친구 이름을 받아 입력하세요(1/3) : ')
k=input('친구 이름을 받아 입력하세요(2/3) : ')
l=input('친구 이름을 받아 입력하세요(3/3) : ')
m=[j,k,l]
m.sort()
print(m)

n='A','B','C','D','E'
print(n[0])
print(n[1])
student='영희', 20,'CS'
name=student[0]
age=student[1]
major=student[2]
print('name = ',name)
print('age = ',age)
print('major = ',major)

o={'one':'하나','two':'둘','three':'셋'}
p=input('단어를 입력하세요 : ')
print(o.get(p,'없음'))

q=set(['Lee', 'Sanders','Harris','Davis'])
r=set(['Park','Harris','Clark','Lee'])
print("""2개의 파티에 모두 참석한 사람은 다음과 같다.
""",q.intersection(r))