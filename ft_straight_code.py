def ft_straight_code(a):
    r = ""
    if a > 0:
        while a:
            c = a % 2
            if c == 0:
                r = "0" + r
            else:
                r = "1" + r
            a = a // 2
        while len(r) < 8:
            r = "0" + r
        return (r)
    if a < 0:
        r = ""
        a = -a
        while a:
            c = a % 2
            if c == 0:
                r = "0" + r
            else:
                r = "1" + r
            a = a // 2

        while len(r) < 8:
            r = "0" + r
        r = '1' + r[1] + r[2] + r[3] + r[4] + r[5] + r[6] + r[7]
        return (r)
    if a == 0:
        r = '00000000'
        return (r)
