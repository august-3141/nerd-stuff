# Recursive code yay

def recurve(x):
    if x > 0:
        return x + recurve(x - 1)
    else:
        return 0

num = 1
while num < 100:
    out = recurve(num)
    print(out)
    num = num + 1