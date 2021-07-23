# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
    
    #first condition 
        if (n==0):
            return True
        elif(f==0):
        
	        return False
    #considering factor rule 
    #factor condition, making absolute to ignore -ve integers
        elif(abs(n)% abs(f)==0):
            return True
    
    

        return False 
    
