import sys
import math
input = sys.stdin.readline

a, b, v = map(int, input().split())
day = math.ceil((v - a) / (a - b)) + 1
print(day)
