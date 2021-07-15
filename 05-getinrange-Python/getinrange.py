# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
    box =(bound1, bound2)
    
    
    #condition 1:::: X should be greater than bound 1 to return X
    if x>max(box):
    
            return max(box)
    
    #condition 2:::: X should be smaller than bound 2 to return X
    elif x<min(box):
        return min(box)
    else:
        return (x)
