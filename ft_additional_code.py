def ft_additional_code(a):
    x = ''
    if a >= 0:
        while a:
            b = a % 2
            if b ==0:
                x = '0' + x
            else:
                x = '1' + x
            a = a // 2
        while len(x) < 8:
            x = '0' +x
        return x

    else:
        a = a *(-1)
        while a:
            b = a % 2
            if b == 0:
                x = '1' + x
            else:
                x = '0' + x
            a = a // 2
        while len(x) < 8:
            x = '1' + x
        return x