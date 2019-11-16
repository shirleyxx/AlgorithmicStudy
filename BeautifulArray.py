class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1: [1]}
        def sub(N):
            if N not in memo:
                odds = sub((N+1)//2)
                evens = sub(N//2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        return f(N)
