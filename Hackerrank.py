#!/usr/bin/env python
if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        n = input().split()
        if len(n) == 1:
            if n[0] == "print":
                print(arr)
            if n[0] == "pop":
                arr.pop()
            if n[0] == "sort":
                arr.sort()
            if n[0] == "reverse":
                arr.reverse()
        if len(n) == 2 and n[0] == "append":
            arr.append(int(n[1]))
        if len(n) == 3 and n[0] == "insert":
            arr.insert(int(n[1]), int(n[2]))
        if len(n) == 2 and n[0] == "remove":
            arr.remove(int(n[1]))