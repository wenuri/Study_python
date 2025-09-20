# for
    # 순환하는 횟수가 지정
    #range(), 자료구조(list, tutple, set, dict)
# while
    # 횟수는 없고 매 순환할때마다 조건을 판단해서 True

# 5번 반복
for i in range (5) : # (1,5,2)1부터 시작 4까지, 2개띠워서 즉 1,3 출력
    print(i)
    print(range(5))
    print(list(range(5)))

for i in list(range(5)) :
    print(i)


for name in ['a', 'b', 'c']:
    print(name)
    print(list(name))

  #tuple자료구조 순환
tuple_1 = (10,20,30)
for i in tuple_1 :
        print(f'i = {i}') #{}안을 변수로 인식 문자열과 변수를 함께 쓸수있다 f = format 최신 python에 적용됨


#set 순환
set_1 = {1,5,10}
for i in set_1:
     print(f'i={i}')  #set은 중복을 제거하는대신 순서를 보장하지 않는다 set은 중복제거, 교/합집합연산에 사용 순서가 필요하면 list로 씌운다

# dict 순환 - dict 자체는 key값들만 대상
dict_1 = {
     'name' :'홍길동',
     'age' : '25',
     'addr' : '서울'
}

for i in dict_1:
     print(f'i={i}') #dict 자체는 key값들만 대상 key 값만 나옴. 

for i in dict_1.keys():
     print(f'i={i}') #key 값만 리스트형태로 반환 


for i in dict_1.values():
     print(f'i={i}') #값만 리스트형태로 반환

for i in dict_1.items():
     print(f'i={i}') #(key,value) 형태의 리스트집합으로 반환     
     
print(dict_1.items())
print(list(dict_1.items()))

# 집합 데이터를 가져와 특정로직을 이용해 데이타를 추출하거나 또는 추출한 데이타에 함수를 통해 특정작업을 할때많이 사용