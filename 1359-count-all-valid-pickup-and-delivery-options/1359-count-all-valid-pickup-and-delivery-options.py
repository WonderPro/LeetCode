class Solution:
    def countOrders(self, n: int) -> int:
        mod = 1e9+7
        ans = 1
        for i in range(1,n+1):
            ans = (ans * i)%mod
            ans = ans * ( 2 * i- 1) % mod
        return int(ans)
