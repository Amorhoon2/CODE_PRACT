# 진법 변경 (10진수 ㅡ>)
print(bin(12))
print(oct(12))
print(hex(12))

print(2/ 3)

print(5 /3)

# # 지수 표현 (제곱하는 횟수) 10^
print(314e-2)   # 314 * 0.01 == 3.14
print(314e2)    # 314 * 100 == 314.00.0



# f-string
print( 'Debugging roaches 13 room' )
bugs = 'roaches'
counts = 13 # ㅡ> 100
area = 'living room'
print( f'Debugging {bugs} {counts} {area}' )
# # 예전 방식
print('Debugging {} {} {}' .format(bugs, counts, area) )
# # 더 예전
print('Debugging %s %d %s' % (bugs, counts, area))

# # 응용
greeting = 'hi'
print(f'{greeting:^10}') # 10칸 중 중앙 정렬
print(f'{greeting:>10}') # 10칸 중 오른쪽 정렬
print(f'{3.141592:.4f}') # 앞의 실수를 소수점 4자리까지 출력 (반올림처리까지)



# # 불변과 가변
my_str = 'hello'
my_str[0] = 'z'
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)

list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1)  # [100, 2, 3]
print(list_2)  # [100, 2, 3]


x = 10
y = x

x = 20
print(x)  # 20 
print(y)  # 10
