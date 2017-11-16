def cal_lis(array: list) ->[int]:
    """
    calculate the longest increasing subsequence
    """
    sq = []
    sq.append([array[0]])

    for i in range(1, len(array)):
        sq.append([])
        for j in range(i):
            if array[j] < array[i] and len(sq[i]) < len(sq[j]) + 1:
                sq[i] = sq[j].copy()

        sq[i].append(array[i])

    max_len = len(sq[0])
    for s in sq:
        if len(s) > max_len:
            max_len = len(s)

    return max_len


if __name__ == "__main__":
    print(cal_lis([3,2,6,4,5,1]))
