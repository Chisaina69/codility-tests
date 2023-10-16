def solution(A):
    if len(A) > 2:

        amp = max(A) - min(A)

        return amp


print(solution([10, 2, 44, 15, 39, 20]))  # 3
