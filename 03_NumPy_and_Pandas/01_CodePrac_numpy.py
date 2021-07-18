import numpy as np

A = np.array([[1,2],[3,4]])
print(A)
print(type(A)) # numpy 배열은 ndarray 타입 클래스이다.

# Numpy 배열의 속성
print(A.ndim) # 배열의 차원
print(A.shape) # 배열의 크기
print(A.dtype) # 원소 자료형

# Numpy 배열 객체에서 제공하는 함수
print(A.max(), A.mean(), A.min(), A.sum())

# 인덱싱, 슬라이싱
print(A[0]) # A 배열의 첫번째 행 (Default axis = 1)
print(A[1]) # A 배열의 두번째 행

print(A[0][0]) # A 배열의 첫번째 원소에 접근
print(A[0][1]) # A 배열의 첫번째 원소에 접근

print(A[0,0]) # A 배열의 첫번째 원소에 접근
print(A[0,1]) # A 배열의 첫번째 원소에 접근

print(A[A>1])

# 배열 형태 바꾸기
print(A.T) # A.Transpose()
print(A.flatten()) # 다차원 배열을 1차원 배열로 변환

# 배열의 연산
print(A+A) # np.add(A,A)
print(A-A) # np.subtract(A,A)
print(A*A) # np.multiply(A,A), Element-wise 곱
print(A/A) # np.divided(A,A), Element-wise 나누기

# 브로드캐스팅
B = np.array([10, 100])
print(A*B) # 행렬B는 [10,100]에서 [[10,100], [10,100]]으로 브로드캐스팅된다.

# 내적(inner-product)
print(B*B)
print(B.dot(B))



















