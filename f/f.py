from collections import Counter

def py_solver(query):
    target = int(query.split('\n')[0])
    arr = Counter(list(map(lambda x: int(x), query.split('\n')[1].split())))
    for num1 in arr:
        if target - num1 in arr and (num1 != target - num1 or arr[num1] > 1):
            return 1
    return 0


if __name__ == "__main__":
    solver()
