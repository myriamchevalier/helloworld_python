temp_far = input("What is the temperature in Farenheit?")

if temp_far.isnumeric() == False:
    print(f"Input is not a number")
    exit()

temp_far = int(temp_far)
temp_cel = (temp_far - 32) * 5/9

print(f"{temp_far} in Farenheit is {temp_cel} in Celsius")