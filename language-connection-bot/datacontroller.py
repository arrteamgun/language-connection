
import random

def get_line(data):
    res = data[random.randint(0, len(data)-1)]
    strres = f"{res[0]}\n{res[1]}\n{res[2]}"
    return strres