from time import strftime,localtime
def convert(seconds):
    return strftime('%Y-%m-%d_%H:%S',localtime(seconds))
print(convert(1601901810))