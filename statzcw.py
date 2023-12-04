# You may only use the following functions to construct your code:
#
# python builtin sum()
# python builtin max()
# python builtin min()
# python Math function Math.sqrt()
# python normal operators on floats (*, /, +, -, etc)
import math


def zcount(lst: list) -> float:
    count = 0
    for i in lst:
        count += 1
    return count


def zmean(lst: list) -> float:
    return sum(lst) / len(lst)


def zmode(lst: list) -> set:
    count_list = []
    for i in range(len(lst)):  # Iterate through list, count the times each value appears
        count_list.append(lst.count(lst[i]))
        i += 1

    d1 = dict(zip(lst, count_list))  # Create a dictionary. Key is the number, count is the value

    if max(count_list) == 1:  # If no number appears more than once, no mode.
        return set()
    else:
        return {k for (k, v) in d1.items() if v == max(count_list)}  # Return set of number that occur the most


def zmedian(lst: list) -> float:
    lst.sort()
    l = len(lst)
    mid = int(l/2)
    if l % 2 == 1:  # if odd length list, return middle index
        return lst[mid]
    else:           # if even length list, return avg of two center indices
        return (lst[mid-1] + lst[mid]) / 2


def zvariance(lst: list) -> float:
    mean = zmean(lst)
    n = zcount(lst) - 1

    deviations = []

    for i in lst:
        deviations.append((mean - i) ** 2)

    return sum(deviations) / n


def zstddev(lst: list) -> float:
    return math.sqrt(zvariance(lst))


def zstderr(lst: list) -> float:
    return zstddev(lst) / math.sqrt(zcount(lst))


def zcorr(listx: list, listy: list) -> float:
    #     sum = 0
    # make sure the count or a and b are equal!
    # then we can just use count(a)
    # for i in range(0, count(a))
    #     sum += ((a[i] - mean(a)) * (b[i] - mean(b)))
    # cov = sum/(count(a)-1)
    #
    pass


lst1 = [1, 2, 2, 3, 4, 4, -9]
print(zcount(lst1))
print(zmean(lst1))
print(zmode(lst1))
print(zmedian(lst1))
print(zvariance(lst1))
print(zstddev(lst1))
print(zstderr(lst1))





