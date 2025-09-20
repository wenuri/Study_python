# 고객별 구매금액 딕셔너리 매핑
# 조회
# 없는 고객을 조회하려고 하면 에러발생
# try ~ except ~ else 사용해 키가 없는 경우 처리, 정상적인 경우엔 추가작업


# 구매고객 리스트
customers_purchases = {'김민수' : 15000, '이민정' : 230000, '박소연' : 45000}

while True: 
    # 고객 이름을 받아서 조회
    #search_name = '이순신' # 존재하지 않는 고객
    search_name = input('검색하려는 고객이름을 입력하세요:') 
    try :
        if not search_name.isalpha():
            raise ValueError(f'오류 : {search_name}은 이름이 아닙니다. 이름을 입력하세요')
            
        amount = customers_purchases[search_name]

    except KeyError :
        print(f'오류 : {search_name}이 고객 데이터가 없습니다.')

    except ValueError as e:
        print(e)
    else:
        print(f'{search_name} 고객의 구매금액은 : {amount}원')
        break