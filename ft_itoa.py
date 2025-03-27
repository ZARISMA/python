def ft_itoa(n: int) -> str:
    negative = False
    if n == 0:
        return "0"
    if n < 0:
        negative = True
        n = -n  
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(chr(48 + digit))
        n = n // 10
    if negative:
        digits.append('-')
    digits.reverse()
    return "".join(digits)


print(ft_itoa(245678))
    