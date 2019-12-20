class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        l = len(beginWord)
        change_map = {}
        if beginWord in wordList:
            wordList.remove(beginWord)

        for w in wordList:
            for i in range(l):
                try:
                    change_map[w[:i] + "*" + w[i+1:]].add(w) 
                except:
                    change_map[w[:i] + "*" + w[i+1:]] = {w}
                    
        queue = [beginWord] 
        visited = dict.fromkeys(wordList, 0)
        visited[beginWord] = 1

        while queue:
            w_cur = queue.pop(0)
            for i in range(l):
                w = w_cur[:i] + "*" + w_cur[i+1:]
                if w in change_map:
                    for w_next in change_map[w]:
                            if w_next == endWord:
                                visited[w_next] = visited[w_cur] + 1
                                return visited[endWord]
                            if visited[w_next] == 0:
                                visited[w_next] = visited[w_cur] + 1
                                queue.append(w_next)

        return 0

