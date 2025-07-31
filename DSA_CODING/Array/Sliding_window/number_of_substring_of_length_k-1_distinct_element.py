from collections import Counter
def substrCount(self, s, k):
        # code here
        
        s_c = Counter()
        n = len(s)
        i = 0
        j = 0
        count= 0
        while j<n:
            s_c[s[j]]+=1
            if j-i+1 < k:
                j+=1
                
            elif j-i+1 == k:
                if len(s_c) == k-1:
                    count+=1
                
                s_c[s[i]] -= 1
                if s_c[s[i]] == 0:
                    del s_c[s[i]]
                i+=1
                j+=1
        return count
            
            
        
