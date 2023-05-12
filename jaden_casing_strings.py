def to_jaden_case(string):
    array = string.split()
    new_array = []
    for a in array:
        new_array.append(a.capitalize())
    return " ".join(new_array)