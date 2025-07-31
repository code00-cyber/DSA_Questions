def longestSubarray(self, arr, k):  
        # code here
        i = 0
        j = 0
        n = len(arr)
        sum = 0
        max = 0
        while j< n:
            sum+= arr[j]
            if sum < k:
                j+=1
            elif sum == k:
                l = j-i+1
                if l > max:
                    max = l
                j+=1
                    
            elif sum > k:
                while sum > k:
                    sum = sum-arr[i]
                    i+=1
                if sum == k:
                    l = j - i + 1
                    if l > max:
                        max = l
                j+=1
        return max
                
            
