class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        l = len(beginWord)
        change_map = {}
        words = wordList

        for w in words:
            for i in range(l):
                try:
                    change_map[w[:i] + "*" + w[i+1:]].add(w) 
                except:
                    change_map[w[:i] + "*" + w[i+1:]] = {w}
                    
        for t in change_map.values():
            t = list(t)
            
        queue = [beginWord] 
        visited = dict.fromkeys(words+[beginWord], 1)

        while queue:
            w_cur = queue.pop(0)
           
            for i in range(l):
                w = w_cur[:i] + "*" + w_cur[i+1:]
                if w in change_map:
                    for w_next in change_map[w]:
                            if w_next == endWord:
                                visited[w_next] = visited[w_cur] + 1
                                return visited[endWord]
                            if visited[w_next] == 1 and w_next != beginWord:
                                visited[w_next] = visited[w_cur] + 1
                                queue.append(w_next)

        return 0

