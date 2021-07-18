# Module : .py 파일

# help('datetime')

import keyword
print(keyword.kwlist, '\n')

print(keyword.__file__, '\n')

import calendar
print(calendar.month(2020,1))

from calendar import month
print(month(2020,1))

import datetime
print(datetime.datetime.now())

from datetime import datetime as dt
print(dt.now())

# Package : 여러 모듈(.py 파일)을 특정 디렉터리에 모아놓은 것
# EX) A.B : A 패키지의 하위 모듈인 B를 호출한다.

import urllib.request
print(type(urllib.request)) # urllib 패키지의 request 모듈의 type = module
print(urllib.__path__) # urllibsms 경로속성을 가지고 있으므로 패키지로 부를 수 있다.

# --------------------------------------------------- #

# module 내 __name__을 단독 실행 시에는 '__main__' 문자열이 된다.
# module을 import  시 __name__은 실제 모듈명 (myPackage.moduleA)가 된다.
# import myPackage.moduleA
# myPackage.moduleA.functionA()

# 패키지 하위에 정의된 모든 모듈 객체를 한번에 import하기 위해서는 __init__.py 파일 정의가 필요하다. 
# from myPackage import * 

# import 시에는 __name__ 속성이 실제 모듈명인 myPackage.module이므로
# if __name__ == '__main__' 비교 구문이 false가 되어 아무런 코드도 실행되지 않는다. 
# 만약 main() 함수를 호출하려면 패키지명.모듈명.함수명 순으로 직접 입력해야한다.
import myPackage.moduleA
myPackage.moduleA.main()












