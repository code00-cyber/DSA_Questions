def reverseWithSpacesIntact(self, s):
        # code here
        s = list(s)
        n = len(s)
        i = 0
        j = n-1
        
        while(i< j):
            if s[i] == ' ':
                i+=1
                continue
            if s[j] == ' ':
                j-=1
                continue
            
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return (''.join(s))
