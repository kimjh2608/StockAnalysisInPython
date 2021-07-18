# 파이선 프로그램 성능 측정 표준 라이브러리, timeit
import timeit
# timeit(테스트구문, setup=테스트 준비구문, num=테스트 반복횟수)

#1) 순회속도 비교하기
# 0~9999개 정수 1만개를 원소로 갖는 list, tuple, set을 생성
# 각 반복 자료형별로 모든 원소를 순회하는 동작을 1000번 반복하는데 걸리는 시간 측정

iteration_test = """
for i in itr:
    pass

"""
print(timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=1000))
print(timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=1000))
print(timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=1000))

#2) 검색속도 비교하기
# 0~9999 중 임의의 난수를 생성 후 0~9999까지의 반복 자료형에 존재하는 검색하는 시간 측정

search_test = """
import random
x = random.randint(0,len(itr)-1)
if x in itr:
    pass
"""

print(timeit.timeit(search_test, setup='itr = list(range(10000))', number=1000))
print(timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=1000))
print(timeit.timeit(search_test, setup='itr = set(range(10000))', number=1000))

# 결론 : 성능 측정결과 특정 원소가 존재하는지 검색하는데 set이 가장 효율적!!