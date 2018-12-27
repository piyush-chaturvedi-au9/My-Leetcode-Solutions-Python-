class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        cs = self.countLetters(S)
        ans = 0
        for word in words:
            ws = self.countLetters(word)
            ans += self.checkWords(cs, ws)
        return ans
    def countLetters(self, S):
        cnt, lc = 0, ''
        ans = []
        for c in S:
            if c == lc:
                cnt += 1
            else:
                if cnt: ans.append((lc, cnt))
                cnt, lc = 1, c
        if cnt: ans.append((lc, cnt))
        return ans
    def checkWords(self, cs, ws):
        if len(cs) != len(ws): return 0
        for c, w in zip(cs, ws):
            if c[0] != w[0]: return 0
            if c[1] < w[1]: return 0
            if c[1] != w[1] and c[1] < 3: return 0
        return 1
