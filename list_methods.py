
numbers = [5, 2, 1, 7, 4]
print(numbers)
numbers.append(20)
print(numbers)
numbers.insert(0, 9)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.clear()
print(numbers)
numbers = [5, 2, 1, 7, 4]
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(5))
print(50 in numbers)
print(5 in numbers)
numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5))
# sorts ascending
numbers.sort()
print(numbers)
numbers = [5, 2, 1, 5, 7, 4]
# sorts decending
numbers.reverse()
print(numbers)
numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.pop()
print(numbers)
print(numbers2)
