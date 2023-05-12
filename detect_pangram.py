import string

def is_pangram(s):
    cont = 0
    for a in list(string.ascii_lowercase):
        for i in [*s.lower()]:
            if(a == i):
                cont += 1
                break
    if (cont == len(string.ascii_lowercase)):
       return True
    else:
       return False