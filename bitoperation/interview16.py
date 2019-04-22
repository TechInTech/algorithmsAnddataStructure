
G_INVALIDINPUT = False


def power(base, exponent):
    G_INVALIDINPUT = False

    if base == 0.0 and exponent < 0:
        G_INVALIDINPUT = True
        return 0.0

    absexponent = exponent
    if exponent < 0:
        absexponent = - exponent

    # result = powerwithunsignedexponent1(base, absexponent)
    result = powerwithunsignedexponent2(base, absexponent)
    if exponent < 0:
        result = 1.0 / result

    return result


def powerwithunsignedexponent1(base, exponent):
    result = 1.0
    for i in range(1, exponent + 1):
        result *= base
    return result


def powerwithunsignedexponent2(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = powerwithunsignedexponent2(base, exponent >> 1)
    result *= result
    if (exponent & 0x1 == 1):
        result *= base

    return result


def main():
    base = float(input('Input the base:'))
    exponent = int(input('Input the exponent:'))

    result = power(base, exponent)
    print('The power of %.1f in exponent of %d is %.2f' %
          (base, exponent, result))


if __name__ == '__main__':
    main()
