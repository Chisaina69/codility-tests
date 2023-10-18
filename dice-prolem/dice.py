def solution(A, F, M):
    N = len(A)
    total_sum = M * (N + F)  
    existing_sum = sum(A)  

    missing_sum = total_sum - existing_sum  
    if missing_sum > F * 6 or missing_sum < F: 
        return [0]

    result = [6] * F
    missing_sum -= 6 * F

    for i in range(F):
        if missing_sum > 0:
            decrease = min(5, missing_sum)  
            result[i] -= decrease
            missing_sum -= decrease

    return result
