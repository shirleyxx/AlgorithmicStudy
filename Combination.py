class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def comb(n,k,ans, output): 
            if k==0:     
                output.append(ans.copy())
                return 
            
            t = ans[-1] if ans else 0
            for i in range(t+1, n+1):
                ans.append(i)                
                comb(n, k-1, ans, output)   
                ans.pop()
                
        
        output = []
        comb(n,k,[], output)
        return output
