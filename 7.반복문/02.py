#while

count = 0
while count < 3: #조건문
    print(f'count = {count}')
    count += 1

# 무한 루프때 ctr+c 로 키보드 강제중지 시킬수있음
count = 0
while True:
    print(f'count = {count}')
    count += 1
    if count == 3:
        break
    