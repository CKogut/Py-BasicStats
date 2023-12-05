# You may only use the following functions to construct your code:
#
# python builtin sum()
# python builtin max()
# python builtin min()
# python Math function Math.sqrt()
# python normal operators on floats (*, /, +, -, etc)
import math
import pandas as pd


def zcount(lst: list) -> int:
    count = 0
    for i in lst:
        count += 1
    return count


def zmean(lst: list) -> float:
    return round(sum(lst) / zcount(lst), 3)


def zmode(lst: list) -> set:
    count_list = []
    for i in range(zcount(lst)):  # Iterate through list, count the times each value appears
        count_list.append(lst.count(lst[i]))

    d1 = dict(zip(lst, count_list))  # Create a dictionary. Key is the number, count is the value

    if max(count_list) == 1:  # If no number appears more than once, no mode.
        return set()
    else:
        return {k for (k, v) in d1.items() if v == max(count_list)}  # Return set of number(s) that occur the most


def zmedian(lst: list) -> float:
    lst.sort()
    l = len(lst)
    mid = int(l/2)
    if l % 2 == 1:  # if odd length list, return middle index
        return lst[mid]
    else:           # if even length list, return avg of two center indices
        return round((lst[mid-1] + lst[mid]) / 2, 3)


def zvariance(lst: list) -> float:
    mean = zmean(lst)
    n = zcount(lst) - 1

    deviations = []

    for i in lst:
        value = mean - i
        abs_value = max(value, -value)
        deviations.append(abs_value ** 2)

    return round(sum(deviations) / n, 3)


def zstddev(lst: list) -> float:
    return round(math.sqrt(zvariance(lst)), 3)


def zstderr(lst: list) -> float:
    return round(zstddev(lst) / math.sqrt(zcount(lst)), 3)


def zcorr(listx: list, listy: list) -> float:
    sum = 0

    if zcount(listx) != zcount(listy):
        pass

    for i in range(zcount(listx)):
        sum += (listx[i] - zmean(listx)) * (listy[i] - zmean(listy))
    cov = sum/(zcount(listx)-1)

    # correlation(l1, l2) = covariance(l1, l2) / (stddev(l1) * stddev(l2))
    return round(cov / (zstddev(listx) * zstddev(listy)), 3)


dataZero = pd.read_csv('dataZero.csv')
d0x = dataZero['x'].values.tolist()
d0y = dataZero['y'].values.tolist()

print(zmean(d0x), zvariance(d0x), zmean(d0y), zvariance(d0y), zcorr(d0x, d0y))

dataOne = pd.read_csv('dataOne.csv')
d1x = dataOne['x'].values.tolist()
d1y = dataOne['y'].values.tolist()

print(zmean(d1x), zvariance(d1x), zmean(d1y), zvariance(d1y), zcorr(d1x, d1y))

dataTwo = pd.read_csv('dataTwo.csv')
d2x = dataTwo['x'].values.tolist()
d2y = dataTwo['y'].values.tolist()

print(zmean(d2x), zvariance(d2x), zmean(d2y), zvariance(d2y), zcorr(d2x, d2y))

dataThree = pd.read_csv('dataThree.csv')
d3x = dataThree['x'].values.tolist()
d3y = dataThree['y'].values.tolist()

print(zmean(d3x), zvariance(d3x), zmean(d3y), zvariance(d3y), zcorr(d3x, d3y))





