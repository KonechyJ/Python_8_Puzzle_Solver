


dash = ('   -')
A = [[dash, 3],
    [2,1]]

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
        for row in A]))