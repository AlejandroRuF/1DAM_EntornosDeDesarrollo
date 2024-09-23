def prueba(n, a, b, c):
    s = 0
    for i in range(n):
        if a > 1 and b > 2 and c > 3:
            s = (a + b) * (b + c) * (a + c)
        if s > 0:
            s = s / (a * b * c)
    return s

if __name__ == "__main__":
 prueba(-1, -1, -1, .1)
 prueba(2, 2, 3, 4)