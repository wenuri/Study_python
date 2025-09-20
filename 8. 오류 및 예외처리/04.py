purchases =[1000,2000,4000,-3000]

# 사용자 정의 오류 사용하기
#음수는 있으면 안된다, 음수값이 발생되면 경고메세지 출력하고 해당데이타 패스
# 음수값이 발견되면 예외를 발생시켜 해당오류를 except에서 처리
#총 구매금액
total = 0
for p in purchases :
    try : 
        if p < 0 :
            raise ValueError(f"음수금액발견 : {p}")
        total += (p)
    except ValueError as e : # ValueError 를 e로 별칭
        print(f'오류 : {e} 해당 데이터 건너뜀')
        
print(f'총 구매액 : {total}')
