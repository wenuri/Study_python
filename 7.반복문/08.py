# 딕셔너리[키] += 값

#구매고객

customers = ['홍길동','이순신','홍길동','강감찬']
purchases = [10000,20000,15000,30000]

#고객별 구매금액의 합을 출력
# ex 고객명 : 호길동 / 구매액 : 25000


result = {} #dictionary 생성
for idx, name in enumerate(customers) :
    if name not in result :
        result[name] = purchases[idx]
    else :
        result[name] += purchases[idx]

# 출력
for key, value in result.items() :
    print(f'고객명: {key} / 구매금액 : {value}')
