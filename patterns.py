# squre pattern
'''r=5
for i in range(r):
    for j in range(r):
        print("*",end=" ")
    print()
'''
# triangle pattern
'''r=5
for i in range(r):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
# decreasing triangle
'''r=5
for i in range(r):
    for j in range(i,r):
        print("*",end=" ")
    print()
    '''
# rightside triangle
'''r=5
for i in range(r):
    for j in range(i+1):
        print("#",end=" ")
    for j in range(i,r):
        print("*",end=" ")
    print()'''

# leftside triangle
'''r=5
for i in range(r):
    for j in range(i,r):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''

# triangle
'''t=5
for i in range(t):
    for j in range(i,t):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=(" "))
    print()'''

# upside down triangle
'''t=5
for i in range(t):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,t-1):
        print("*",end=" ")
    for j in range(i,t):
        print("*",end=" ")
    print()
'''

'''
# letter r
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or (j==4 and i<3) or i==2 or (i==j and i>2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# letter j
for i in range(5):
    for j in range(5):
        if i==0 or j==2 or (i==4 and j<3) or (j==0 and i>2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''
# letter u
for i in range(5):
    for j in range(5):
        if j==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

# alphabet triangle
'''num=65
for i in range(5):
    for j in range(i+1):
        ch=chr(num)
        print(ch,end=" ")
    num+=1
    print() '''


# letter a
'''n = 4 
for i in range(n):
    for j in range(7):
        if (i==0 and j==3) or (i==1 and (j==2 or j==4)) or (i==2 and (j!=0 and j!=6)) or (i==3 and (j==0 or j==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    n = 5 
for i in range(n):
    for j in range(4):
        if i == 0 or i == 2 or j == 0 or j == 3:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

# letter A
'''or i in range(5):
    for j in range(5):
        if j==0 or i==0 or j==4 or i==2:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()'''


# letter D
'''n = 6
for i in range(n):
    for j in range(4):
        if j == 0 or (i==0 and j == 1) or (i==1 and j==2) or (i==2 and j==3) or (i==3 and j==3) or (i==4 and j==2) or (i==5 and j==1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

# pascal triangle
'''import math
r=5
for i in range(r):
    print(" "*(r-i),end=" ")
    for j in range(i+1):
        print(math.comb(i,j),end=" ")
        # num=num*(i-j)//(j+1)
    print()'''


# RIGHT SIDE PASCAL TRIANGLE
'''r=5
for i in range(r):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()
'''
# letter a
'''n = 7
for i in range(n):
    for j in range(6):
        if (i == 0  and j!=0 and j!=5) or i == 3 or (j == 0 and i!=0) or (j == 5 and i!=0):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''for i in range(5):
    for j in range(5):
        if (i==0 and j!=0 and j!=4) or i==2 or (j==0 and i!=0) or (j==4 and i!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


# letter B
'''for i in range(5):
    for j in range(5):
        if j==0 or (i==0 and j!=4) or  ((j==4 and i!=0 and i!=2) and i!=4) or (i==4 and j!=4) or (i==2 and j!=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

# letter D
'''for i in range(5):
    for j in range(5):
        if j==0 or (i==0 and j!=4) or (i==4 and j!=4) or (j==4 and i!=0 and i!=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


# letter E
'''for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==4 or (i==2 and j!=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
 '''

