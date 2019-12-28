class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0 for i in range(len(edges)+1)]
        size = [0 for i in range(len(edges)+1)]
        
        def find(n):
            while parent[n] != n:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
        
        for u, v in edges:
            if parent[u] == 0: parent[u] = u
            if parent[v] == 0: parent[v] = v
            pu, pv = find(u), find(v)
            if pu == pv: return [u, v]
            
            if size[pv] > size[pu]: u, v = v, u
            parent[pv] = pu
            size[pu] += size[pv]
 
        return []



            
        
