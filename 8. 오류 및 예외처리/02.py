#예외 종류에 따라서 처리를 다르게 할수 있다 

# int ('ss') valueError
# list_1 = [1,2] list_1[2]  IndexError
# 10/0  ZeroDivisionError

try :
    pass
except ValueError :
    print('ValueError 발생시 적합한 처리')
except IndexError :
      print('ValueError 발생시 적합한 처리')
except : 
     print('그외다양한 에러 발생시 적합한 처리')

else :
     print('try 구분에서 에러가 발생하지 않으면 ')
finally :
     print('에러발생 상관없이 무조건 이부분은 실행') # 메모리를 할당받았다가 해제해줘야할때 많이 사용