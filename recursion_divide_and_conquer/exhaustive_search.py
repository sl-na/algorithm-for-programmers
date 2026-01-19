from sys import stdin


def solve(i, ml, n, at):
    if ml == 0:
        return True
    if i >= n:
        return False
    return solve(i + 1, ml, n, at) or solve(i + 1, ml - at[i], n, at)


def main():
    n = int(stdin.readline())
    at = tuple(map(int, stdin.readline().split()))
    q = int(stdin.readline())
    ml = tuple(map(int, stdin.readline().split()))
    for i in range(q):
        if solve(0, ml[i], n, at):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
