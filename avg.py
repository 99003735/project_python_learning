from collections import namedtuple
n = int(input()); student = namedtuple('student', input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(n))/n)