x = 0

def function_1(n):
    global x
    if n > 0:
        x += 1
        return function_1(n-1) + x
    else:
        return 0

a = 5 
print(function_1(a)) 
