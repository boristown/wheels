import sys

input = sys.stdin.readline

#int input
def inp():
    return(int(input()))

#list input
def inlt():
    return(list(map(int,input().split())))

#string input
def insr():
    return input()[:-1]

#strings input
def inss(n):
    return [insr() for _ in range(n)]

#variables input
def invr():
    return(map(int,input().split()))

#matrix input
def inmt(n):
    return [inlt() for _ in range(n)]