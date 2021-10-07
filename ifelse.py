# value = 8
# if value == 7 :
#     print("The value is 7")
# elif value == 8:
#     print('The value is 8')
# else:
#     print('The value is not one we are looking for')

# print("Finished!")
# print(3 == 4)
# print(3 != 4)

# print(3 > 4)
# print(3 < 4)
# print(3 >= 4)
# print(3 <= 4)

first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number > 1:
    print('At least one value is greater than 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')