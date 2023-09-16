# from itertools import combinations
import sys
sys.stdin = open('input.txt')


def solution(arr, a):
    from itertools import combinations as cb

    answer = 0

    for p, j, k in cb(arr, 3):
        if p + j + k <= a and p + j + k >= answer:
            answer = p + j + k

    return answer


T = 2
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    cards = list(map(int, input().split()))
    cards.sort()
    cards_per = []

    for i in cards:
        if i <= B:
            cards_per.append(i)

    print(solution(cards_per, B))
