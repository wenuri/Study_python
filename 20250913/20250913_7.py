# 자료형 - 데이터의 집합
# 리스트 편집하기

scores = [10,20,20]

scores2 = scores.copy()

scores2[0] = 100

print(scores)

print(scores2)


a= [10, 20]
b=a
print(b)
b[0] = 100
print(a)

# 깊은 복사
a = [10, 20]
b = a.copy()  #copy()는 a리스트값을 복사해 다른주소에 만듬
b[0] = 100
print(a)


print("--------------여기부터는 추가연습----------------")
a = [10,20,30,40,10]
a.insert(1,-1)  #index[]는 index값을 알려주는것
print(a)

print(a.index(10))

print("--------------여기부터는 삭제연습----------------")
print(a)
del a[0]
print(a)


test = a.pop(1) #가장 마지막애를 지움, 번호를 주면 해당값을 지우는데 delete랑 다른건 삭제값을 알수있다-복원가능
a.insert(0,test)
print(a)
print(a[2:4])

