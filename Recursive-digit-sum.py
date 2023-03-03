  p = n * k
    
    def fun(p):
        if len(p) == 1:
            return int(p[0])
        
        adder = 0
        for i in p:
            adder += int(i)
        
        return fun(str(adder))
    
    return fun(p)
