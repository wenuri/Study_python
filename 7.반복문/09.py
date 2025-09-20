#매출 보고서

date = ['월','화','수','목','금']
sales = [25000, 18000,30000,22000,15000]
# 총 매출과 평균 매출을 출력
# 평균 이상 매출이 일어난 요일을 출력

total_sales = sum(sales)
avg_sales = total_sales / len(sales)  # sales.count(25000) - sales 리스트에서 25000이 몇개인지를 세는것  


# 총 매출과 평균 매출을 출력
print(f'총 매출 : {round(sum(sales))}, 평균 매출 : {round(avg_sales)}')

# 평균 이상 매출이 일어난 요일을 출력

for idx, sale in enumerate(sales) :
    if sale >= avg_sales:
        print(date[idx])


