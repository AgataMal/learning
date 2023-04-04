#!/usr/bin/env python
if __name__ == '__main__':
    N = int(input())
    dictionary = {}
    for i in range(N):
        n = input().split()
        key_name = n[0]
        value_no = n[1:]
        dictionary[key_name] = value_no
    query_name = input()
    query = dictionary[query_name]
    suma = 0
    for x in query:
        suma += float(x)
    print("{:.2f}".format(suma/len(query)))
