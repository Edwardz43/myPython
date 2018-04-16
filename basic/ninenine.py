for x in range(1, 10):
    result = []
    for y in range(2, 6):
        s = '{0:2d} x {1:2d} = {2:2d}'.format(y, x, y * x)
        result.append(s)

    print(result[0], result[1], result[2], result[3])

print()
for x in range(1, 10):
    result = []
    for y in range(6, 10):
        s = '{0:2d} x {1:2d} = {2:2d}'.format(y, x, y * x)
        result.append(s)

    print(result[0], result[1], result[2], result[3])
