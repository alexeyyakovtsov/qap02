
def decor(func):
    def decor_1(*args):
        res = list(args)
        return res[::-1]
    return decor_1

@decor
def function_into(a, b):
    return a, b

print(function_into(1, 2)) 
