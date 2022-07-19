# second.py 파일

def sayMyName():
    print("BlockDMask")


def addNumbers(*args):
    result = 0
    for val in args:
        result += val

    return result


def mulNumbers(*args):
    result = 1
    for val in args:
        result *= val

    return result