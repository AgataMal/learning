#!/usr/bin/env python
if __name__ == '__main__':
    N = int(input())

    inpt = input()
    inputs = inpt.split()[:N]

    zzz = list(map(int, inputs))

    tpl = tuple(zzz)
    print(hash(tpl))
