crispr ={'EDIT':'Editas Medicine', 'NTLA':'Intellia Therapeutics', 'CRSP':'CRISPR Therapeutics'}

# 출력 형식 (format)
#1) % 기호방식
for x in crispr:
    print('%s : %s' % (x, crispr[x]))

#2) {} 기호방식
for x in crispr:
    print('{} : {}'.format(x, crispr[x]))

#3) f-strings 방식
for x in crispr:
    print(f'{x} : {crispr[x]}')

nums = [1,2,3,4,5]
for x in nums:
    print(f'{x:.2f}')