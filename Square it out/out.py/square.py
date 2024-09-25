def square_values(Start,End):
    return [i**2 for i in range(Start, End+1)]

Start_range = 1
End_range = 17
Square_list = square_values(Start_range,End_range)

print("Square values between", Start_range, "and", End_range, ":")
for value in Square_list:
    print(value)
