def mindist(dist,check):
    min2=100000

    for i in range(1,n+1):
        if(check[i]!=1 and dist[i]<=min2):
            min2=dist[i]
            f=i
    
    return f


#t- NO. OF TEST CASES
t=int(input())
for i in range(t):
    #N- NO. OF VERTICES M- NO. OF EDGES
    n,m=map(int,input().split())
    a=[]*(n+1)
    list1={}
    weight={}
    # a- ADJANCEY MATRIX  list1- VISITED VERTRICES   weight-MIN DISTANCE FROM SOURCE
    for j in range(n+1):
        a.append([-1]*(n))
        list1[j]=0
        weight[j]=100000
    
    for j in range(m):
        b=[]*4
        b=list(map(int, input().split()))
        if(a[b[0]][b[1]-1]==-1 or a[b[0]][b[1]-1]>b[2]):
            a[b[0]][b[1]-1]=b[2]
        if(a[b[1]][b[0]-1]==-1 or a[b[1]][b[0]-1]>b[2]):
            a[b[1]][b[0]-1]=b[2]
    k1=int(input())
    #k1- GIVEN SOURCE FROM USER
    weight[k1]=0
    for j in range(n-1):
        u=mindist(weight,list1)
        #mindist- FUNCTION TO FIND EDGE WITH SHORTEST WEIGHT
        list1[u]=1
        for v in range(0,n):
            if(list1[v+1]!=1 and a[u][v]!=-1 and weight[u]!=100000 and (a[u][v]+weight[u]<weight[v+1])):
                weight[v+1]=a[u][v]+weight[u]
       
        
            
   
    
    for j in range(n):
        if(weight[j+1]!=0 and  weight[j+1]!=100000):
            print(weight[j+1],end=" ")
        elif(weight[j+1]==100000):
            print("-1",end=" ")
    print()



'''
Sample Input

1
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1
Sample Output

24 3 15
                    

'''               
                        
                
            
    
    
