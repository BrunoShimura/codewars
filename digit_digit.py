def square_digits(num):
    array = []
    for i in str(num):
        array.append(str(int(i)**2))
    return int("".join(array))

print(square_digits(765))