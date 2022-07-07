# set1 = {
#     1, 2, 3, 4, 5
# }
# set2 = {1, 2, 3, 4, 5, 4, 6}
# print(set1.union(set2))
# print(set1)
# set1.update(set2)
# print(set1)

# set1 = {"Hello", "banana"}
# set2 = {"Hell", "apple", "pineapple"}
# set1.update(set2)
# print(set1)
# print(set1.isdisjoint(set2))

# set1 = {"Hello", "banana"}
# set2 = {"Hello", "apple", "pineapple"}
# set3 = {"Hello", "potato"}
# print(set1.intersection(set3, set2))

# set1 = {1, 2}
# set2 = {3}
# set3 = {4, 5}
# set4 = {3, 2, 6}
# set5 = {6}
# set6 = {7, 8}
# set7 = {9, 8}
# print(set1.intersection(set7, set6, set5, set4, set3, set2))
# print(set1.intersection(set4))
# print(set2.intersection(set4))
# print(set6.intersection(set7))
# print(set4.intersection(set5))
# print(set1.union(set2, set3, set5, set7, set6, set4))


# set1 = {1, 3, 5}
# set2 = {1, 3, 5, 6}
# if set1.issubset(set2):
#     print("Супермножество не обнаружено")
# elif set1.issuperset(set2):
#     print("Объект является чистым супермножеством")
#
# if set1 == set2:
#     print("Множества равны")

# comprehentions - lists, dict

# while n > 1: my version
#     factorial *=n
#     n-= 1
# print(factorial)

# lists = []
# for i in range(1, 10001):
#     lists.append(i)
# print(lists)

# lists = [i for i in range(1, 10001)]
# print(lists)

# str1 = "didjheud; 'fcsd'dscdscc;vghgb"
# lists = [i for i in str1]
# print(lists)

# import datetime
# time_now = datetime.datetime.now()
# print(time_now)

# import datetime
#
# lists = []
# time_now = datetime.datetime.now()
# for i in range(1, 10001):
#     lists.append(i)
# delta = datetime.datetime.now() - time_now
# print(delta)

# time_now = datetime.datetime.now()
# lists = [i for i in range(1, 10001)]
# delta = datetime.datetime.now() - time_now
# print(delta)

# lists = [i for i in range(1, 10001) if i % 2 == 0 and i % 5 == 0]
# print(lists)
# lists = [i**2 for i in range(1, 10001) if i % 2 == 0 and i % 5 == 0]
# print(lists)

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)

#
# dicts = {i: i ** 2 for i in range(1, 5)}
# print(dicts)

# lists = ['apple', 'banana']
# dicts = {i: i * 2 for i in lists}
# print(dicts)

import random
# while True:
#     lists = ['rock', 'scissors', 'paper']
# aliya = input("Choose: ")
# comp = random.choice(lists)
# if aliya == comp:
#     print("Ничья!")
#
# elif aliya == 'rock':
#     if comp == 'paper':
#         print("comp: 1")
#     elif aliya == 'paper':
#         if comp == 'rock':
#             print("aliya: 1")
#     elif aliya == 'scissors':
#         if comp == 'rock':
#             print("comp: 2")












