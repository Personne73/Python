def fact(n):
    if n <= 0:
        return 'n must be strictly positive'
    if n <= 2:
        return n
    return n*fact(n-1)