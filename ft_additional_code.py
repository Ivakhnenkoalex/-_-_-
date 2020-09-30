def ft_reverse_code(a):
    r = ""
    q = a
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
    elif a < 0:
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
    elif a == 0:
        r = '00000000'
    a = q
    if a >= 0:
        return (r)
    elif a < 0:
        if r[1] == '0':
            r = r[0] + '1' + r[2] + r[3] + r[4] + r[5] + r[6] + r[7]
        elif r[1] == '1':
            r = r[0] + '0' + r[2] + r[3] + r[4] + r[5] + r[6] + r[7]
        if r[2] == '0':
            r = r[0] + r[1] + '1' + r[3] + r[4] + r[5] + r[6] + r[7]
        elif r[2] == '1':
            r = r[0] + r[1] + '0' + r[3] + r[4] + r[5] + r[6] + r[7]
        if r[3] == '0':
            r = r[0] + r[1] + r[2] + '1' + r[4] + r[5] + r[6] + r[7]
        elif r[3] == '1':
            r = r[0] + r[1] + r[2] + '0' + r[4] + r[5] + r[6] + r[7]
        if r[4] == '0':
            r = r[0] + r[1] + r[2] + r[3] + '1' + r[5] + r[6] + r[7]
        elif r[4] == '1':
            r = r[0] + r[1] + r[2] + r[3] + '0' + r[5] + r[6] + r[7]
        if r[5] == '0':
            r = r[0] + r[1] + r[2] + r[3] + r[4] + '1' + r[6] + r[7]
        elif r[5] == '1':
            r = r[0] + r[1] + r[2] + r[3] + r[4] + '0' + r[6] + r[7]
        if r[6] == '0':
            r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + '1' + r[7]
        elif r[6] == '1':
            r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + '0' + r[7]
        if r[7] == '0':
            r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + r[6] + '1'
        elif r[7] == '1':
            r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + r[6] + '0'
        return (r)
def ft_additional_code(a):
    if a > 0:
        r = ''
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
    if a == 0:
        r = ''
        r = '00000000'
        return (r)
    if a < 0:
        r = ""
        q = a
        if a < 0:
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
        a = q
        if a < 0:
            if r[1] == '0':
                r = r[0] + '1' + r[2] + r[3] + r[4] + r[5] + r[6] + r[7]
            elif r[1] == '1':
                r = r[0] + '0' + r[2] + r[3] + r[4] + r[5] + r[6] + r[7]
            if r[2] == '0':
                r = r[0] + r[1] + '1' + r[3] + r[4] + r[5] + r[6] + r[7]
            elif r[2] == '1':
                r = r[0] + r[1] + '0' + r[3] + r[4] + r[5] + r[6] + r[7]
            if r[3] == '0':
                r = r[0] + r[1] + r[2] + '1' + r[4] + r[5] + r[6] + r[7]
            elif r[3] == '1':
                r = r[0] + r[1] + r[2] + '0' + r[4] + r[5] + r[6] + r[7]
            if r[4] == '0':
                r = r[0] + r[1] + r[2] + r[3] + '1' + r[5] + r[6] + r[7]
            elif r[4] == '1':
                r = r[0] + r[1] + r[2] + r[3] + '0' + r[5] + r[6] + r[7]
            if r[5] == '0':
                r = r[0] + r[1] + r[2] + r[3] + r[4] + '1' + r[6] + r[7]
            elif r[5] == '1':
                r = r[0] + r[1] + r[2] + r[3] + r[4] + '0' + r[6] + r[7]
            if r[6] == '0':
                r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + '1' + r[7]
            elif r[6] == '1':
                r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + '0' + r[7]
            if r[7] == '0':
                r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + r[6] + '1'
            elif r[7] == '1':
                r = r[0] + r[1] + r[2] + r[3] + r[4] + r[5] + r[6] + '0'
        if 

print(ft_additional_code(10))
