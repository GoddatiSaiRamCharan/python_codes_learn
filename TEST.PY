from collections import deque

n = int(input())

for _ in range(n):
    m = int(input())
    cubes = deque(map(int, input().strip().split()))
    print(cubes.index[1])
    cube = 0
    for _ in range(m):
        left, right = cubes[0], cubes[-1]
        if left >= right:
            if cube >= left or cube == 0:
                cube = left
                cubes.popleft()
        else:
            if cube >= right or cube == 0:
                cube = right
                cubes.pop()

    if len(cubes) == 0:
        print('Yes')
    else:
        print('No')
