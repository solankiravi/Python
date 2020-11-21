def GCD(m,n):
    fm=fn =[]
    for i in range(1,m+1):
        if(m % i == 0):
            fm.append(i)
        if( n % i = 0):
            fn.append(i)
    
    for i in range(1,n+1):
        if(n % i == 0):
            fn.append(i)
    cf = []
    for i in range(0,len(fm)):
        if(n % fm[i] == 0):
            cf.append(fm[i])
    print(max(cf))

GCD(14,63)