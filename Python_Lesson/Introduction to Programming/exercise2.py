# for i in range(10):  # the range function list the number within a range
#    print(i)

# for j in range(5, 10):  # the range function takes the start and end of the range
#    print(j)

# for k in range(2, 12, 2):  # the range function takes the start and end of the range as well as the step
#   print(k)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#    total = total + price
# print(total)

# for x in range(4):
#    for y in range(3):
#        print(f"({x}, {y})")

# numbers = [1, 1, 1, 1, 5]
# for x_count in numbers:
#    output = ""
#    for count in range(x_count):
#        output += "x"
#    print(output)

items = [3, 5, 7, 9, 5, 6, 7, 2]
max_num = items[0]
for i in items:
    if i > max_num:
        max_num = i
print(f"your largest number is {max_num}")




