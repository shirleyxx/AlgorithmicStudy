def Partition(n, #number to be broken
              m  #maximum number in partition
             ) -> int:
    if n < 2:
        return n
    
    f = [[0]*(m+1) for i in range(n+1)]
    for j in range(1,m+1):
        f[1][j] = 1
    
    for i in range(2, n+1):
        for j in range(m+1):
            if i<j:
                f[i][j] = f[i][j-1]
            elif i==j:
                f[i][j] = f[i][j-1] + 1
            else:
                f[i][j] = f[i][j-1] + f[i-j][j]
           

    return f

for n in [5,6,7,8]:
    print('Partition of {}: {}'.format(n, Partition(n,n)[n][n]))
    
 