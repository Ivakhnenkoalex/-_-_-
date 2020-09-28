def additional(a):
    r = ""
    if a >= 0:
        while a:
            c = a % 2
            if c == 0:
                r = "0" + r
            else:
                r = "1" + r
            a = a // 2
            while len(r) < 8:
                r = "0" + r
        print(r)
    else:
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
        print(r)
