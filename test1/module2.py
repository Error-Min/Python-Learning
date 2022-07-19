# first.py
import module1 # second.py 모듈로 가지고오기

module1.sayMyName()

result1 = module1.addNumbers(1, 2, 3, 4, 5)
result2 = module1.mulNumbers(1, 2, 3, 4, 5)

print(f"second.addNumbers(arr) : {result1}")
print(f"second.mulNumbers(arr) : {result2}")