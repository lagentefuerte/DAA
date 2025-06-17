def solve (num, enemies, cumulative_sum):
    if enemies[0] > num :
        return 0, 0
    elif num < enemies[len(enemies)-1]:
        index = binarysearch(num, enemies, 0, len(enemies) - 1)
    else:
        index = len(enemies) - 1
    return index+1, cumulative_sum[index]

def binarysearch (num, enemies, a, b):
    mid = (a+b)//2
    if a > b or enemies[mid] == num:
        return mid
    elif enemies[mid] <= num:
        return binarysearch(num, enemies, mid+1, b)
    else:
        return binarysearch(num, enemies, a, mid-1)



n = int(input().strip())
enemies = list(map(int, input().strip().split()))
m = int(input().strip())
cumulative_sum = [0] * n
cumulative_sum[0] = enemies[0]
for i in range(1, n):
    cumulative_sum[i] = cumulative_sum[i - 1] + enemies[i]
for i in range(m):
    a, b = solve(int(input().strip()), enemies, cumulative_sum)
    print(str(a) + " " + str(b))