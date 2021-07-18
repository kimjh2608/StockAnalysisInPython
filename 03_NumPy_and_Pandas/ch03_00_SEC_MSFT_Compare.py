from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

# Open/ High / Low / Close --> OHLC
# Volume = 거래량, Adj Close = 수정종가
# print(sec.head())
# print(sec.tail())

# print(msft.head())
# print(msft.tail())

# print(sec.index) # dataframe index 구성 확인
# print(sec.columns) # dataframe column 속성 확인

# 일간 변동률 (daily percent change, dpc)
# print(sec['Close'])
# print(sec['Close'].shift(1)) # 이전 거래일의 종가

sec_dpc = ((sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1)) * 100
# print(sec_dpc.head())
sec_dpc.iloc[0] = 0 # nan 값을 0으로 변경
# print(sec_dpc.head())

# 일간 변동률 히스토그램 (구간별 빈도수)
# plt.hist(sec_dpc, bins = 18) # bins = 히스토그램 구간수
# plt.grid(True)
# plt.show()

# print(sec_dpc.describe())

# 일간 변동률 누적합 
sec_dpc_cs = sec_dpc.cumsum()
# print(sec_dpc_cs)

msft_dpc = ((msft['Close'] - msft['Close'].shift(1)) / msft['Close'].shift(1)) * 100
msft_dpc.iloc[0] = 0 # nan 값을 0으로 변경
msft_dpc_cs = msft_dpc.cumsum()

plt.plot(sec.index, sec_dpc_cs, 'b', label = 'Samsung')
plt.plot(msft.index, msft_dpc_cs, 'r--', label = 'Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()
