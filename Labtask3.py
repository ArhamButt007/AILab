# def search(numbers, key):
#     for num in numbers:
#         if(key == num):
#             print(f"{key} is in our list")
#             return
#     print(f"{key} is not in our list")


# print("Making List from user input")
# numbers = []
# for i in range (0,5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# key = int(input("Enter a number to search: "))

# search(numbers,key)

name = input("Enter you name: ")
letter = input("Enter a character: ")
if(letter in name):
    print(f"Your name {name} has letter {letter} in it")
else:
    print(f"Your name {name} does not have letter {letter} in it")




# def sum_of_even(numbers):
#     mylist = []
#     for num in numbers:
#         if(num%2==0):
#             mylist.append(num)
#     result = sum(mylist)
#     print(f"Sum of even numbers is {result}")

# numbers = [1,2,3,4,5,6,7,8,9,10]

# def sum_even(nums):
#     return sum([num for num in nums if num%2==0])

# sum_of_even(numbers)

# result = sum_even(numbers)

# print(result)

# names = ["Arham","Atique","Butt"]

# def reverse_str(names):
#     return [word[::-1]for word in names]

# def reversing_string(names):
#     list = []
#     for name in names:
#         list.append(name[::-1])
#     print(list)


# list = [1,2,3,4]
# square = [x**2 for x in list if x>2]
# print(square)
    


# list = reversing_string(names)