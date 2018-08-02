def sum(alist):
    if len(alist) == 0:
        return 0
    else:
        return alist[0] + sum(alist[1:])


if __name__ == "__main__":
    print(sum([0, 1, 2, 3, 4, 5]))
