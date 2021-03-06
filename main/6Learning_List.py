# List는 배열이라고 생각하면 편합니다.

a = [] # a = list()와 동일
b = [1, 3, 5]
c = ['Leopold', 'Myungseo', 'Kang', 'L3opold7']
d = [7, 9, ['Myungseo', 'L3opold7']]
# List 안에는 여러가지 자료형을 담을 수 있습니다.

# List에도 Slicing String에서 말한 것들을 적용할 수 있습니다.

print(b[-1])     # 5
print(c[-2])     # Kang
print(d[-1][0])  # Myungseo
# 이중 List에서 인덱싱은 다음과 같이 할 수 있습니다.
# ==========================================
# List 값 수정
test = [1, 2, 3, 4, 5]
test[3] = 6

print(test)  # [1, 2, 3, 6, 5]
# 이렇게 인덱스를 지정해서 직접 값을 바꿔줄 수 있습니다.
# ==========================================
# List 연속된 값으로 변경
test = [1, 2, 3, 4, 5]
test[2:3] = ['a', 'b', 'c']

print(test)  # [1, 2, 'a', 'b', 'c', '4', '5']
# 2이상 3미만의 인덱스 부분에 a,b,c List를 변경해주는 것입니다.

# ==========================================
# List 요소 삭제
test = ['a', 'b', 'c', 'd', 'e']
test[2:4] = []

print(test)  # ['a', 'b', 'e']
# del 함수 사용
test = ['a', 'b', 'c', 'd', 'e']
del test[2]

print(test)  # ['a', 'b', 'd', 'e']
# del 함수를 사용해서 삭제할 수도 있습니다.

test = ['a', 'b', 'c', 'd', 'e']
del test[2:4]

print(test)  # ['a', 'b', 'e']
# 마찬가지로 인덱스를 범위로 지정하는 것 또한 가능합니다.
# ==========================================
# List 내장 함수들!

test = [1, 2]
test.append(3)  # 맨 뒤에 값 추가
print(test)  # [1, 2, 3]
# append(x) 함수는 인자를 1개밖에 받지 않기 때문에 여러개의 인자를 넘겨줄 경우 에러가 납니다.

# ==========================================

test = [3, 1, 2, 5, 4]
test.sort()
print(test)  # [1, 2, 3, 4, 5]

test.sort(reverse=True)
print(test)  # [5, 4, 3, 2, 1]
# sort() 함수는 List를 자동으로 정렬해줍니다. 역순으로 정렬하기 위해서는 sort 함수에 reverse 옵션을 True로 설정해주면 됩니다.

# ==========================================

test = [3, 1, 2]
test.reverse()
print(test)  # [2, 1, 3]
# reverse() 함수는 현재의 List를 역순으로 뒤집어 줍니다. 정렬은 하지 않고 현재의 List를 역순으로 뒤집어 줍니다.

# ==========================================

test = [1, 2, 3, 4, 5]
print(test.index(3))  # 2
print(test.index(5))  # 4
# index(x) 함수는 x 라는 값이 있는 경우 , x 의 인덱스를 반환해주는 함수입니다.

# ==========================================

test = [1, 2, 3, 4, 5]
test.insert(0, 6)
print(test)  # [6, 1, 2, 3, 4, 5]
# insert(x, y) 함수는 x 위치에 y 라는 값을 삽입해주는 함수입니다.

# ==========================================

test = [1, 2, 3, 4, 3]
test.remove(3)
print(test)  # [1, 2, 4, 3]
# remove(x) 함수는 첫 번째로 나오는 x 라는 값을 List에서 삭제해주는 함수입니다. 보시다시피 뒷부분에 있는 3은 삭제되지 않았습니다.

# ==========================================

test = [1, 2, 3]
print(test.pop())  # 3
print(test)        # [1, 2]
# pop() 함수는 List의 가장 마지막 인덱스의 값을 반환해주고 그 값을 삭제해주는 함수입니다. 위의 예제에서 굳이 3이라는 값이 필요없을 경우에는 print() 함수를 빼도 상관없습니다.

# ==========================================

test = [1, 2, 3, 1, 1]
print(test.count(1))  # 3
# count(x) 함수는 x 라는 값이 List 안에 몇 개나 있는지 반환해주는 함수입니다.

# ==========================================

test = [1, 2, 3]
test.extend([4, 5, 6])
print(test)  # [1, 2, 3, 4, 5, 6]
# extend(x) 함수는 x 부분에 List를 받아서 원래의 List와 병합시켜주는 함수입니다.

# List에서는 위와 같은 내장 함수들을 사용할 수 있습니다. 여기에 더해서 len() 함수로 List 값들의 개수를 얻을 수 있습니다.