def two_sum(nums, target):
    """这样写更直观，遍历列表同时查字典"""
    dct = {}
    for i, n in enumerate(nums):
        cp = target - n
        print("cp==", cp)
        if cp in dct:
            print("3333", dct)
            return [dct[cp], i]
        else:
            dct[n] = i
            print("44444", dct)


nums = [1, 2, 31, 14, 7, 4]
target = 6
[a, b] = two_sum(nums, target)
print(a, b)
