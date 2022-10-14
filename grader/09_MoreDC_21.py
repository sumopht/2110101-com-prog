def factor(N):
    factors = []
    for divisor in range(2, N + 1):
        if N < divisor:
            break
        power_count = 0
        while N % divisor == 0:
            N /= divisor
            power_count += 1
        if power_count == 0:
            continue
        factors.append([divisor, power_count])
        if N < divisor:
            break
    return factors


exec(input().strip())
