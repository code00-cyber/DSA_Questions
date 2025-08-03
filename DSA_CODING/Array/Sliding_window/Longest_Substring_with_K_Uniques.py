def longestKSubstr(self, s, k):
        # code here
        i = 0
        j = 0
        n = len(s)
        max_len = -1
        m = Counter()
        while j<n:
            m[s[j]]+=1
            
            while len(m) > k:
                m[s[i]]-=1
                if m[s[i]] == 0:
                    del m[s[i]]
                i+=1
            if len(m) == k:
                max_len = max(max_len, j-i+1)
                
            j+=1
        return max_len
        
