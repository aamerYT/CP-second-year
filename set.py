# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the li that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    li=[]
    
    sum=0
    
    li.append({})
    
    
    sum+=1
    
    
    for j in range(1,n+1):
        
        
        li.append({j})
        sum+=1
        if(sum>=k):
                return li
    
    for i in range(1,n+1):
        
        for j in range(i+1,n+1):
            li.append({i,j})
            
            sum+=1
            
            if(sum>=k):
                
                return li
    
    
        
print(limitedPowerSet(5,10))