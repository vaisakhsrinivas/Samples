n = int(input())
A = set(list(map(int, input().strip().split(' '))))
N = int(input())
for i in range(0, N):
    inp = list(input().strip().split(' '))
    op = inp[0]
    inp2 = set(list(map(int, input().strip().split(' '))))
    if op == 'intersection_update':
        A.intersection_update(inp2)
    elif op == 'update':
        A.update(inp2)
    elif op == 'symmetric_difference_update':
        A.symmetric_difference_update(inp2)
    elif op == 'difference_update':
        A.difference_update(inp2)

print(sum(A))