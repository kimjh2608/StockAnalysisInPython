# pandas는 구조화된 데이터를 쉽고 빠르게 가공할 수 있는 자료형과 함수를 제공
# pandas는 numpy를 기반으로 구현했기 때문에 대부분 함수가 numpy와 유사
# Series와 dataframe 자료형 객체를 제공한다.
# Series는 index 처리가 된 1차원 벡터 형태의 자료형이다.
# Dataframe은 여러 series가 한 가지 index를 기준으로 합쳐진 형태의 자료형이다.

# ---------------------------------------- #
# 2. dataframe
# ---------------------------------------- #
import pandas as pd

# dataframe 생성자에 dict 형식으로 입력
# 별도의 인덱스 미지정 시 0부터 시작하는 정수 인덱스가 자동 생성됨
df = pd.DataFrame({'KOSPI' : [1915, 1961, 2026, 2467, 2041],
                   'KOSDAQ' : [542, 682, 631, 798, 675]}, 
                    index = [2014, 2015, 2016, 2017, 2018])
print(df)
print(df.describe())
print(df.info())

# Series 여러개를 합쳐서 dataframe 생성
kospi = pd.Series([1915, 1961, 2026, 2467, 2041], 
                    index = [2014, 2015, 2016, 2017, 2018], 
                    name = 'KOSPI')

kosdaq = pd.Series([542, 682, 631, 798, 675], 
                    index = [2014, 2015, 2016, 2017, 2018], 
                    name = 'KOSDAQ')

print(kospi)
print(kosdaq)

df = pd.DataFrame({kospi.name : kospi, kosdaq.name : kosdaq})
print(df)

# List를 이용한 dataframe 생성
columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]
rows = []
rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])

df = pd.DataFrame(rows, columns = columns, index = index)
print(df)

# data 순회처리 (for문)
for i in df.index:
    print(i, df['KOSPI'][i], df['KOSDAQ'][i])

for row in df.itertuples(name='KRX'):
    print(row)

for row in df.itertuples():
    print(row[0], row[1], row[2])











