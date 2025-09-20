# 고객 리스트 출력
sur_name = ['김','이','박','최','홍']
name = ['철수','영애','미애','영희','남준']
custms = []

import random

#print(random.choice(sur_name))  # sur_name 데이터중에서 읨의의 한개 선택

for _ in range(10) :
    f_name = random.choice(sur_name) + random.choice(name)
    custms.append(f_name)


# 고객 리스트 출력
#print(end='')
#print(custms)

for i in custms :
    print(f'고객명 : {custms}')

print('='*100)

#고객별 구매금액 10000~ 50000 사이값으로 랜덤하게 생성
purchases = []

for _ in range(10):
    purchases.append(random.randint(10,50)*1000) # 랜덤하게 1000단위 10000~ 50000 사이 값
print(purchases)





print('='*100)


total_price = 0
custm_counts = 0

# 총 구매금액
print(f'total 금액은 : {sum(purchases)}')

# 25000원 이상 구매한 고객의 수
for i in purchases: 
    if i >= 25000 :
        custm_counts += 1
print(f'25000원이상 구매고객의 수는 : {custm_counts}')

# 25000원 이상 구매한 고객의 이름

#custm_counts_name = []
#for index, i in enumerate(custms) : # enemerate (index번호, 리스트의 값)을 가져옴
 #    if i >= 200:
  #        result.append(fruit[index])
#print(f'200원 이상인 과일은 : {result}')

custm_counts_name = []
for t, i in enumerate(purchases): 
    if i >= 25000 :
           print(f'고객명 : {custms[t]} 구매가격 : {i}')
            #custm_counts_name.append(custms[t])

#print(f'25000원이상 구매고객의 이름은 : {custm_counts_name}')