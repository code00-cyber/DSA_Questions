	def search(self,pat, txt):
	    # code here
	    i = 0
	    j=0
	    n = len(txt)
	    k = len(pat)
	    count = 0
	    pat_count = Counter(pat)
	    txt_count = Counter()
	    while j < n:
	        txt_count[txt[j]]+= 1
	        
	        if j-i+1 < k:
	            j+=1
	        elif j-i+1 == k:
	            if txt_count == pat_count:
	                count +=1
	            
    	        txt_count[txt[i]] -= 1
    	        if txt_count[txt[i]] == 0:
    	            del txt_count[txt[i]]
	        
	            i+=1
	            j+=1
	    return count
	           
	                            
