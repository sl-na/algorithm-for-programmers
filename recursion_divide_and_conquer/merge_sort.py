from sys import stdin

cnt = 0


def validate_list(nl):
    validated_l = []
    for i in nl:
        if 0 <= i <= 10**9:
            validated_l.append(i)
        else:
            pass
    return validated_l


def merge(nl, left, mid, right):
    left_l = nl[left:mid]
    right_l = nl[mid:right]
    i = j = 0
    k = left
    global cnt
    while i < len(left_l) and j < len(right_l):
        if left_l[i] <= right_l[j]:
            nl[k] = left_l[i]
            i += 1
        else:
            nl[k] = right_l[j]
            j += 1
        cnt += 1
        k += 1
    while i < len(left_l):
        nl[k] = left_l[i]
        i += 1
        k += 1
        cnt += 1
    while j < len(right_l):
        nl[k] = right_l[j]
        j += 1
        k += 1
        cnt += 1


def merge_sort(nl, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(nl, left, mid)
        merge_sort(nl, mid, right)
        merge(nl, left, mid, right)


def main():
    n = int(stdin.readline())
    nl = list(map(int, stdin.readline().split()))
    nl = validate_list(nl)
    if n != len(nl):
        raise ValueError(
            "the length of the second input must be the same as the first input value. or there is an out of range value in the input."
        )
    merge_sort(nl, 0, n)
    for index, value in enumerate(nl):
        if index != len(nl) - 1:
            print(value, end=" ")
        else:
            print(value)
    global cnt
    print(cnt)


if __name__ == "__main__":
    main()
