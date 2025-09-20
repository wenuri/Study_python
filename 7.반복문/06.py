# 2개의 집합 = list
# 1개는 과일이름
# 1개는 가격
# 2개의 리스트는 순서대로 데이터가 저장

fruit = ['사과','바나나','포도','오렌지']
price = [100, 200,150,400]

# 과일 가격중에 200원 이상인 과일은?
result = []
for index, i in enumerate(price) : # enemerate (index번호, 리스트의 값)을 가져옴
     if i >= 200:
          result.append(fruit[index])
print(f'200원 이상인 과일은 : {result}')

