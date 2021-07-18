# 연평균 성장률 함수 (연복리 수익률)
def getCAGR(first, last, years):
    return (last/first)**(1/years) - 1

cagr = getCAGR(65300, 2669000, 20)
print("SEC CAGR : {:.2f}".format(cagr))

# 함수 정의 시 반환값 미설정할 경우 None 반환
def func1():
    pass

print(func1())
print(func1() == None)
print(func1() is None)

# 함수의 여러 결과값 반환 시 튜플 객체로 변환됨
def myFunc():
    var1 = 'a'
    var2 = [1,2,3]
    var3 = max

    return var1, var2, var3

print(myFunc())

# 함수 반환 순서대로 여러 객체를 나누어 받기 (쉼표로 구분)
s, l ,f = myFunc()
print(s)
print(l)
print(f)

# 람다 (lamda) : 이름 없는 간단한 함수를 만들때 사용
insertComma = lambda x : format(x, ',') # 천 단위 숫자에 쉼표 추가
print(insertComma(123456789))


