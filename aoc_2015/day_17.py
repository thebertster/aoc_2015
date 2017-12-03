containers = ( 11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3 )

containerSize = {}

n = 0
minContainers = len(containers)

for i in range(2**len(containers) - 1):
    sum = 0
    containersRequired = 0
    for j in range(len(containers)):
        if (i >> j) & 1:
            sum += containers[j]
            containersRequired += 1
    if sum == 150:
        if containersRequired < minContainers:
            minContainers = containersRequired
        containerSize[containersRequired] = containerSize.setdefault(containersRequired, 0) + 1

print(minContainers, containerSize[minContainers])