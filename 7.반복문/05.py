# random한 데이터 10개를 리스트에 저장하고
# 순환문을 이용해 저장된 데이터에서 짝수만 찾아서 새로운 리스트에 저장
# 짝수 구분은 값 % 2 == 0 으로

import random

k = 10
target  = random.sample(range(100),k)
print(f'target = {target}')
even_list = []

for i in target :
     if i % 2 == 0 :
        even_list.append(i)
print(f'짝수의 집합 : {even_list}')


count = 0
even_list_1 = []
while count < k : 
    if target[count] % 2 == 0 :
        even_list_1.append(target[count])
    count +=1
print(f'짝수의 집합 : {even_list_1}')
 
 
