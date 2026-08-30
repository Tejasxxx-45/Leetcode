class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Alice must take at least 2 stones initially.
        # Work backwards from the state where all stones are taken.
        ans = prefix[n - 1]

        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans