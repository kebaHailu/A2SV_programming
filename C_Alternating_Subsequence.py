for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = arr[0] > 0
    ans = 0
    max_val = float("-inf")
    for i in arr:
        if pos:
            if i > 0:
                max_val = max(max_val, i)
            else:
                pos = False
                ans += max_val
                max_val = i
        else:
            if i < 0:
                max_val = max(max_val, i)
            else:
                pos = True
                ans += max_val
                max_val = i
    ans += max_val
    print(ans)