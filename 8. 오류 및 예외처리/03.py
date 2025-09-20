# 구매고객의 데이터를 받았는데 실수로 문자열이 들어온경우 

purchases =['1000','2000','삼천','3000','30 00']

#총 구매금액
total = 0
for p in purchases :
    try : 
        total += int(p)
    except :
        print(f'에러 : {p}')
        pass

print(f'총 구매액 : {total}')
