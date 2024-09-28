import math


def judgeSquareSum(c: int) -> bool:
    for i in range(round(math.sqrt(c + 1) + 1)):
        for j in range(round(math.sqrt(c + 1) + 1)):
            if i ** 2 + j ** 2 == c:
                return True
    return False


print(judgeSquareSum(0))
