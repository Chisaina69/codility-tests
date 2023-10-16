def alsphat(S):
    n = len(S)
    p = 0
    current_segment = 0
    
    for i in range(n):
        if S[i] == "X":
            current_segment += 1
            if current_segment == 3:
                p += 1
                current_segment = 0
    
    if current_segment > 0:
        p += 1
    
    return p


                                        
                
