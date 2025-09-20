# try : except : pass
# 

import traceback
try : 
    print('error')
    print('4')
    int('ssss')
    print('정상종료')
#except Exception as e:
except :
    print('에러가 발생')
    traceback.print_exc()



