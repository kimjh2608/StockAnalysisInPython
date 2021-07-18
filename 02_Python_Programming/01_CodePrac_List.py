#########################################
#1. List (리스트)

# myList = 'Thoughts become things.'.split()
# print(type(myList))
# print(myList)

# myList = ' '.join(myList)
# print(myList)

# li = [2, 5, 3, 1, 4]
# li_sort = sorted(li)
# print(li)
# print(li_sort)
# li.sort()
# print(li)

#########################################
#1.1) 구분자 변경하기
# strList ='2012/01/04'
# print(strList)
# print('-'.join(strList.split('/')))
# print(strList.replace('/','-'))

# strList = '1,234,567,890'
# print(strList)
# print(''.join(strList.split(',')))
# print(strList.replace(',',''))

# print(format(1234567890,','))

#########################################
#1.2) 리스트 복사
# myList = ['Thoughts','become','things.']
# newList1 = myList
# print(newList1)
# newList1[-1] = 'actions.'
# print(newList1)
# print(myList)

# myList = ['Thoughts','become','things.']
# newList2 = myList[:]
# print(newList2)
# newList2[-1] = 'actions.'
# print(newList2)
# print(myList)

#########################################
#1.3) 리스트 내포 (comprehension)
# 열거형 객체의 전체 또는 일부 원소를 변경하여 새로운 객체 생성
# 보통 다른 언어에서는 이런 작업을 for문으로 수행하나
# python에는 comprehension을 사용
nums = [1,2,3,4,5]
squares = []
for x in nums: # for iteration
    squares.append(x**2)
print(squares)

nums = [1,2,3,4,5]
squares = [x**2 for x in nums] # comprehension
print(squares)

# Comprehension은 리스트에서 조건에 맞는 원소만 골라서 가공한 뒤 
# 새로운 리스트를 생성할 떄 편리하게 사용 가능
nums = [1,2,3,4,5]
even_squares = [x**2 for x in nums if x % 2 == 0]
print(even_squares)









