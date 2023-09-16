import sys
sys.stdin = open('input.txt')


T = 2
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)

    mx = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                s = arr[i]+arr[j]+arr[k]
                if s <= M:
                    if mx < s:
                        mx = s
                        break

    print(mx)
