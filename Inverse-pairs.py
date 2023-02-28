n=int(input())
a=list(map(int,input().split()))

def Merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q

    LEFT = [0]*(n1+1)
    RIGHT = [0]*(n2+1)
    
    for i in range(0,n1):
        LEFT[i]=A[p+i]
    for j in range(0,n2):
        RIGHT[j]=A[q+1+j]

    #Only need to larger than 10^5,to represnet infinity
    LEFT[n1] = 100001   
    RIGHT[n2] = 100001

    result = 0

    i = 0
    j = 0

    for m in range(p,r+1):
        if LEFT[i]<RIGHT[j]:   #Only code to modified is here <= becomes < (Homework1,P2)(hahaha)
            A[m]=LEFT[i]     #We want the max number of crossings
            i+=1               #Crossing could also generate in the same segment
        else:
            result+=(n1-i)
            A[m]=RIGHT[j]
            j+=1
    return result

def Inversions_Count(A,p,r):
    if p>=r:
        return 0
    q = int((p+r)/2)
    LeftInversion = Inversions_Count(A,p,q)
    RightInversion = Inversions_Count(A,q+1,r)
    result = LeftInversion + RightInversion + Merge(A,p,q,r)
    return result

result = Inversions_Count(a,0,n-1)

print(int(result))


