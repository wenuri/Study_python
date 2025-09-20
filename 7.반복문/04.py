import random
print(random.sample(range(100),5)) #0-99사이에서 랜덤으로 중복되지 않은 5개를 뽑아 list형태로 반환
print(random.randint(1,100))  #1부터 100을 포함한 100까지 임의의 숫자 1개를 반환

# 중복을 허용하는 10개 random 숫자 추출 = list의 append 와 반복문사용
#num = random.randint(1,100)
#list_1.append(num)

list_1 = []

for _ in range(10) :
    num = random.randint(1,20)
    list_1.append(num)
    #print(list_1)
print(list_1)
print(f'list_1 = {list_1}')
