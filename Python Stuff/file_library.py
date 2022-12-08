# I love file handling

def opendoc(x):
    open(f"{x}.txt", "w", encoding="UTF-8")
    return (f"Opened {x}.txt")

def writedoc(x, y):
    file = open(f"{x}.txt", "a", encoding="UTF-8")
    file.write(f"{y} \n")
    return (f"Text saved on {x}.txt.")

def readdoc(x):
    file = open(f"{x}.txt", "r", encoding="UTF-8")
    return (file.read())