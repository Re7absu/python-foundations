# without cpmorehension
numbers = []
for i in range(1, 6):
    numbers.append(i)
print(numbers)

nums = [i for i in range(6, 11)]
print(nums)

names = ["Ali", "Sara", "Rehab"]
upper_names = [name.upper() for name in names]
print(upper_names)


# comprehensions with if
numbers = [1, 2, 3, 4, 5, 6]
odd_nums = [i for i in numbers if i % 2 != 0]
print(odd_nums)

########## Nested Comprehension

# without comprehensions
matrix = [[1, 2], [3, 4], [5, 6]]
result = []
for row in matrix:
    for number in row:
        result.append(number)

# with comprehensions
res = [number for row in matrix for number in row]
print(res)

########## dictionary Comprehension

# without dic
sq = {1: 2, 2: 4, 3: 9, 4: 16}

num2 = [1, 2, 3, 4]
# with dic
squares = {number: number**2 for number in num2}
# {key: value for item in iterable}
print(squares)

# لو ابغى بس يعطيني من الدكشنري الاسم بس
employees = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 17},
    {"name": "Rehab", "age": 30},
]
nams2 = [employee["name"] for employee in employees if employee["age"] == 17]
print(nams2)
