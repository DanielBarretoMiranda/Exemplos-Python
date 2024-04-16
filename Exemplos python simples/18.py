def fs(j, l, s):
    if j <= 10:
        if l <= j:
            s+= 1
            return fs(j, l +1, s)
        else:
            return fs(j + 1, 1, s)
    else:
        return s
print(fs(1, 1, 0))