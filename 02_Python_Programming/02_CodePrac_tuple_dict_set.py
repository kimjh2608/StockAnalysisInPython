#########################################
#2. tuple (튜플)

# 튜플은 내장함수도 원소로 가질 수 있다
myTuple = ('a','b','c',[10,20,30],abs,max)
# 5번째 원소인 내장함수 abs에 -100을 파라미터로 전달
print(myTuple[4](-100)) 
# 6번째 원소인 내장함수 max에 리스트를 파라미터로 전달
print(myTuple[5](myTuple[3])) 

#########################################
#3. Dictionary (딕셔너리)

# key : value 형태의 원소들을 쉼표로 구분하여 중괄호로 감싸서 표현 (순서x)
crispr ={'EDIT':'Editas Medicine', 'NTLA':'Intellia Therapeutics'}

# 순서가 없는 반복 자료형으로 시퀀스 자료형처럼 인덱스로 값에 접근 불가
# print(crispr[1]) # keyError 발생
print(crispr['NTLA'])

# Dict 원소 추가 시 key와 value를 함께 지정해야한다.
crispr['CRSP'] = 'CRISPR Therapeutics'
print(crispr)

#########################################
#4. set (세트)

# set은 중복이 없는 원소의 집합이다.
s = {'A','P','P','L','E'}
print(s)

# 우리가 생성한 순서대로 원소가 저장되지 않는다.
mySet = {'B',6,1,2}
print(mySet)

if 'B' in mySet:
    print("'B' exists in", mySet)

# set은 인덱싱이 불가능하나 교집합,차집합,합집합을 구할수 있다.
setA = {1,2,3,4,5}
setB = {3,4,5,6,7}

print(setA & setB) # 교집합
print(setA | setB) # 합집합
print(setA - setB) # 차집합

# 빈 set은 s = set()으로 생성해야한다. s = {} 이면 dict 생성됨
# 중복없는 set의 특징을 이용하면 다음처럼 list에서 중복원소를 제거할수 있다.
ls = [1,3,4,2,2,3,4,2,1,1,1,5]
print(list(set(ls)))







