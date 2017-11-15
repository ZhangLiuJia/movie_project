from django.test import TestCase

# Create your tests here.
li = [1, 2, 3, 3, 3, 4, 4, 5]


def bruteForce(li, num):
    left = -1
    for li_index, li_value in enumerate(li):
        if left >= 0:
            if li_value != num:
                right = li_index - 1
                break
        elif li_value == num:
            left = li_index
    else:
        right = len(li) - 1 if left >= 0 else 0

    return left if left >= 0 else 0, right


def bin_search(data_set, value):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:

            for p in range(mid, -1, -1):
                if data_set[p] != value:
                    left = p + 1
                    break
            else:
                left = 0
            for n in range(mid, len(data_set)):
                if data_set[n] != value:
                    right = n - 1
                    break
            else:
                right = len(data_set) - 1

            return left, right
        elif data_set[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return 0, 0



# print(bruteForce(li, 1))
# print(bin_search(li, 5))
# print(bin_search(list(range(10)), 6))


def check_pwd( pwd):
    import hashlib
    sha = hashlib.sha384()
    sha.update(bytes("不忘初心，方得始终!", encoding="utf-8"))
    sha.update(bytes("admin", encoding="utf-8"))
    sha.update(bytes(pwd, encoding="utf-8"))
    res = sha.hexdigest()

    print(res)


check_pwd("admin")