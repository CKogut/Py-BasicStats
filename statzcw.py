# You may only use the following functions to construct your code:
#
# python builtin sum()
# python builtin max()
# python builtin min()
# python Math function Math.sqrt()
# python normal operators on floats (*, /, +, -, etc)


def zcount(lst: list) -> float:
    count = 0
    for i in lst:
        count += 1
    return count


def zmean(lst: list) -> float:
    return sum(lst) / len(lst)


def zmode(lst: list) -> set:
    count_list = []
    for i in range(len(lst)):
        count_list.append(lst.count(lst[i]))
        i += 1

    d1 = dict(zip(lst, count_list))

    if max(count_list) == 1:
        return set()
    else:
        return {k for (k, v) in d1.items() if v == max(count_list)}


def zmedian(lst: list) -> float:
    lst.sort()
    l = len(lst)
    mid = int(l/2)
    if l % 2 == 1:  # if odd length list, return middle index
        return lst[mid]
    else:           # if even length list, return avg of two center indices
        return (lst[mid-1] + lst[mid]) / 2


def zvariance(lst: list) -> float:  
    pass



lst1 = [1, 2, 2, 3, 4, 4]
print(zcount(lst1))
print(zmean(lst1))
print(zmode(lst1))
print(zmedian(lst1))





# zvariance(list: List[]) -> float
# zstddev(list: List[]) -> float
# zstderr(list: List[]) -> float
# zcorr(listx: List[], listy: List[]) -> float