test = "Hello World!"
print(test)  # Hello World!

test = 'Hello!'
print(test)  # Hello!

test = 'I don\'t need Coke!'
print(test)  # I don't need Coke!

test = "I don't need Coke!"
print(test)  # I don't need Coke!

# ””,’’ 로 감싸진 문자열을 string으로 인식합니다. 싱글쿼터 혹은 더블쿼터를 문자열로 사용하려면 앞에 \ 가 들어가야 합니다.
# 다른 방법으로는 더블쿼터로 문자열을 감싸고 문자열 내에서 싱글쿼터를 사용하는 것입니다.

#==================================================================================================================

test = r'C:\Nature'
print(test)  # C:\Nature

# r’’ 로 문자열을 감싸주게 되면 raw라는 뜻으로 아무 의미없는 문자열이라는 것을 나타내줍니다

#==================================================================================================================

first = 'Myungseo'
last = 'Kang'

print(first + last)  # Myungseo Kang
print(last * 5)      # KangKangKangKangKang

#==================================================================================================================