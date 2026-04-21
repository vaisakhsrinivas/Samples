def climbStairs(steps):

    if steps == 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2

    dp = [0] * (steps+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, steps+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[steps]


print(climbStairs(4))
print(climbStairs(5))
print(climbStairs(10))
print(climbStairs(18))
print(climbStairs(29))
print(climbStairs(50))

