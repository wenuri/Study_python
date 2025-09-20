# continue

count= 0
while count < 10:
    print (f'count = {count}')
    count +=1

count_1= 0
while count_1 < 10:
    count_1 += 1
    if count_1 == 5:
        break
    print (f'count_1 = {count_1}')
   

count_2= 0
while count_2 < 10:
    count_2 += 1
    if count_2 == 5:
        continue # continue를 만나면 밑의 문장을 실행안하고 다신순환문의 다음스텝으로 넘어감 그러므로 5 가 출력 안됨
    print (f'count_2 = {count_2}')
   