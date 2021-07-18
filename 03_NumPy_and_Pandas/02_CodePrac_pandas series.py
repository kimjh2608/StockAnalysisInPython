# pandas는 구조화된 데이터를 쉽고 빠르게 가공할 수 있는 자료형과 함수를 제공
# pandas는 numpy를 기반으로 구현했기 때문에 대부분 함수가 numpy와 유사
# Series와 dataframe 자료형 객체를 제공한다.
# Series는 index 처리가 된 1차원 벡터 형태의 자료형이다.
# Dataframe은 여러 series가 한 가지 index를 기준으로 합쳐진 형태의 자료형이다.

# ---------------------------------------- #
# 1. Series
# ---------------------------------------- #
import pandas as pd

s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s) # index를 별도로 지정하지 않으면 0부터 시작하는 정수형 index가 자동으로 생성된다.

# Series의 index 속성을 이용하여 index 정보를 설정하거나 변경할 수 있다.
s.index = pd.Index([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) # index 변경
s.index.name = 'MY_IDX' # index명 설정
s.name = 'MY_SERIES' # Series명 설정
print(s)

s[6.0] = 5.5 # Series에 값 추가
print(s)

ser = pd.Series([6.7, 4.2], index = [7.0, 8.0])
s = s.append(ser) # 두 series를 하나로 합치면 기존의 series명과 index명이 사라진다.
print(s)

# ---------------------------------------- #
# 데이터 인덱싱
print(s.index[-1]) # 제일 마지막 index
print(s.values[-1]) # 제일 마지막 데이터 (value)

print(s.loc[8.0]) # index 값을 사용하는 인덱서
print(s.iloc[-1]) # index 순서를 사용하는 인덱서

# iloc와 values는 index 순서에 해당하는 데이터를 출력
# values는 결과값이 복수일 때 array로 반환
# iloc는 결과값이 복수일 때 Series로 반환
print(s.values[:])
print(s.iloc[:])

# 데이터 삭제
print(s.drop(8.0))

# Series 정보 보기 : count, mean, std, min, max 등등
print(s.describe())

# ------------------------------------------ #
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0, 5.5, 6.7, 4.2])
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8, 5.9, 6.8, 8.0])

s.index.name = 'MY_IDX' # 인덱스명 입력
s.name = 'MY_SERIES' # 시리즈명 입력

plt.title('ELLIOTT_WAVE')
plt.plot(s, 'bs--')
plt.xticks(s.index)
plt.yticks(s.values)
plt.grid(True)
plt.show()

