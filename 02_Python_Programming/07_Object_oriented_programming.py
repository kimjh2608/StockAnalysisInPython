# 객체 지향 프로그래밍 

class MyFirstClass:
    clsVar = 'The best way to predict the future is to invent it'
    def clsMethod(self):
        print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')

# class에서 생성된 객체를 인스턴스(instance)라고 부른다.
# class로부터 객체를 생성하는 것을 인스턴스화 라고 한다.
# mfc 인스턴스 생성 (인스턴스화)
mfc = MyFirstClass()

# class 변수에 접근
print(mfc.clsVar)

# class 매서드 호출
mfc.clsMethod()

# --------------------------- #
class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's methodB")
 
class C(A,B):
    def methodC(self):
        print("Calling C's methodC")

    # Overriding : 자식 class에서 부모 class의 메서드 이름과 인수형식으로 동일하게 메서드를 재정의
    # Overroad : 자식 class에서 부모 class의 메서드 이름은 동일하나 인수형식은 다르게 메서드를 재정의
    def method(self): #  Overriding 예시
        print("Calling C's overridden method")
        super().method() # 부모 class의 변수나 메소드를 사용할 때 super() 호출

c = C()
c.methodA()
c.methodB()
c.methodC()
c.method()

print('-'*100)
class NasdaqStock:
    # 독스트링 : class나 메서드를 설명하는 문자열
    # help() 함수에서 class나 메서드 설명을 출력한다.
    """Class for NASDAQ stocks""" 

    # Class 변수 정의
    # Class 내부에 존재하면서 메서드 밖에서 정의된 변수
    # Class 내 모든 인스턴스는 class 변수를 공유한다.
    count = 0 

    # __init__ 생성자 정의
    # Class 인스턴스가 생성될 때 자동으로 호출되는 메서드
    # 생성자에서 자동호출 시 넘겨받은 인수를 인스턴스 변수로 정의할 때 사용 (범위 : 인스턴스 내부)
    def __init__(self, symbol, price):
        """Constructor for NasDaqStock"""
        self.symbol = symbol # 인스턴스 변수, self.으로 시작
        self.price = price # 인스턴스 변수
        NasdaqStock.count += 1 # Class 변수
        print('Calling __init__ ({}, {:.2f}) > count: {}'.format(self.symbol, self.price, NasdaqStock.count))

    def __del__(self):
        """Destructor for NasdaqStock"""
        print('Calling __del__({})'.format(self))

gg = NasdaqStock('GOOG', 1154.05) # Class의 모든 인스턴스는 class 변수를 공유하므로 count가 1씩 증가한다.
del(gg)
ms = NasdaqStock('MSFT', 102.44)
del(ms)
amz = NasdaqStock('AMZN', 1746.00)
del(amz)

print(help(NasdaqStock))
















    