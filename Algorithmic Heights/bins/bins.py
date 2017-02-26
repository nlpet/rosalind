

def read_dataset_multiple_anon(fname):
    """ read dataset and store each line as a list of numbers """
    result = []
    f = open(fname, 'r')
    for line in f.readlines():
        result.append([int(x) for x in line.replace('\n', '').strip().split()])
    return result


def binary_search2(n, array, pos):
    l = len(array)
    k = array[l // 2]
    if n == k:
        return pos + (l // 2)
    elif n > k:
        return binary_search(n, array[l // 2:], pos + l // 2)
    else:
        return binary_search(n, array[:l // 2], pos)
    return -1


def binary_search(l, value, low=0, high=-1):
    if not l:
        return -1
    if high == -1:
        high = len(l) - 1
    if low == high or high < low:
        if l[low] == value:
            return low + 1
        else:
            return -1
    mid = (low + high) // 2
    if l[mid] > value:
        return binary_search(l, value, low, mid - 1)
    elif l[mid] < value:
        return binary_search(l, value, mid + 1, high)
    else:
        return mid + 1


if __name__ == '__main__':
    numbers = read_dataset_multiple_anon('bins.txt')
    array = numbers[2]
    to_search = numbers[3]

    results = []

    for num in to_search:
        results.append(binary_search(array, num))

    print ' '.join((str(n) for n in results))
