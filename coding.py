'''def duplicate(nums):
    seen=[]
    count=0
    for i in nums:
        if nums[i] in seen:
            count+=1
        else:
            seen.append(i)
    return count,seen
nums=[1,1,2]
print(duplicate(nums))'''

'''def removed(nums):
    val=int(input())
    for i in nums:
        if i==val:
            nums.pop(i)
    return nums
nums=[1,2,2,1,3,4,5,4]
print(removed(nums))'''

'''def zero(nums):
    i=0
    while i<len(nums)-1:
        if nums[i]==0:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i+=1
        else:
            i+=1
    return nums
nums=[1,1,0,3,5,0]
print(zero(nums))'''

# large and second largest
'''def largest(nums):
    large=-1
    slarge=-1
    for num in nums:
        if num>large:
            slarge=large
            large=num
        elif(num>slarge and slarge!=large):
            slarge=num
    return slarge
nums=[1,5,4,3,2,5,9]
print(largest(nums))'''


'''def slargest(nums):
    large=nums[0]
    secondlarge=float("-inf")
    for i in range(len(nums)):
        if(nums[i]>large):
            secondlarge=large
            large=nums[i]
        elif(large>nums[i] and secondlarge<nums[i]):
            secondlarge=nums[i]
    return secondlarge
nums=[-1,-2,-5,-3,-1,0]
print(slargest(nums))'''

# second smallest
'''def ssmallest(arr):
    small=arr[0]
    secondsmall=float('inf')
    for i in range(len(arr)):
        if(small>arr[i]):
            secondsmall=small
            small=arr[i]
        elif(small!=arr[i] and secondsmall>arr[i]):
            secondsmall=arr[i]
    return secondsmall
arr=[1,2,3,4,0,4,2,4]
print(ssmallest(arr))'''


# check array is sorted or not
'''def Sorted(arr):
    for i in range(1,len(arr)):
        if(arr[i]>=arr[i-1]):
            return True
        else:
            return False
    return True
arr=[1,1,2,2,3,3]
print(Sorted(arr))'''

# return unique values from sortred array
'''def duplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1     
     return arr[:i+1] #return i+1
arr=[1,1,1,2,2,3,3,4]
print(duplicates(arr))'''

# return duplicates from array

'''def duplicates(nums):
    nums.sort()
    temp=[]
    for i in range(len(nums)):
        if(nums[i]==nums[i-1]):
            temp.append(nums[i])
    return temp
nums=[1,1,2,3,3,4]
print(duplicates(nums))'''

# left-shift the array elements by one place
'''def left_Shift(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp
    return arr
arr=[1,2,3,4,5]
print(left_Shift(arr))'''


# right shift
'''def right_Shift(arr):
    temp = arr[-1]              # O(1)
    for i in range(len(arr)-1, 0, -1):  # O(n)
        arr[i] = arr[i-1]
    arr[0] = temp               # O(1)
    return arr'''

# rotate by k notations
'''def k_shift(arr,val):
    return arr[-val:]+arr[:val+1]
val=2
arr=[1,2,3,4,5]
print(k_shift(arr,val))'''

'''def rotate(arr,num):
    n=len(arr)
    num=num%n
    temp=[]
    for i in range(num):
        temp.append(arr[i])
    for i in range(num,n):
        arr[i-num]=arr[i]
    j=0
    for i in range(n-num,n):
        arr[i]=temp[j]
        j+=1
    return arr
arr=[1,2,3,4,5]
num=12
print(rotate(arr,num))'''


'''def zeero(arr):
    n=len(arr)
    temp=[]
    for i in range(n):
        if(arr[i]!=0):
            temp.append(arr[i])
    for i in range(len(temp)):
        arr[i]=temp[i]
    for i in range(len(temp),n):
        arr[i]=0
    return arr
arr=[0,1,2,0,3,0,4]
print(zeero(arr))'''


# zero at last
'''def zero(arr):
    j=-1
    n=len(arr)
    for i in range(n):
        if(arr[i]==0):
            j=i
            break
    for i in range(j+1,n):
        if(arr[i]!=0):
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
arr=[0,1,2,0,3,0,4]
print(zero(arr))'''

# largest element from given arry
'''def large(arr):
    large=arr[0]
    slarge=-1
    for i in range(len(arr)):
        if(arr[i]>large):
            slarge=large
            large=arr[i]
        elif(slarge!=large and slarge<arr[i]):
            slarge=arr[i]
    return slarge
arr=[2,4,6,2,3,5]
print(large(arr))'''


# second smallest
'''def smallest(arr):
    small=arr[0]
    ssmall=float('-inf')
    for i in range(len(arr)):
        if(arr[i]<small):
            ssmall=small
            small=arr[i]
        elif(ssmall<arr[i] and ssmall!=small):
            ssmall=arr[i]
    return ssmall
arr=[7,3,4,6,1,3]
print(smallest(arr))'''

# array is sorted or not
'''def sorted(arr):
    n=len(arr)
    for i in range(1,n):
        if(arr[i]<arr[i-1]):
            return False
    return True
arr=[1,2,3,4,5,7]
print(sorted(arr))'''

# remove duplicates
'''def duplicates(arr):
    arr.sort()
    i=0
    for j in range(1,len(arr)):
        if(arr[i]!=arr[j]):
            arr[i+1]=arr[j]
            i+=1
    return arr[:i+1]
arr=[1,3,2,4,2,1,2]
print(duplicates(arr))'''

# left shift by one
'''def left(arr):
    temp=arr[0]
    for i in range(len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp
    return arr
arr=[1,2,3,4,5]
print(left(arr))'''

# right shift
'''def right(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    return arr
arr=[1,2,3,4,5]
print(right(arr))'''

# rotate left by k notations.
'''def rotate(arr,k):
    n=len(arr)
    k=k%n
    temp=[]
    for i in range(k):
        temp.append(arr[i])
    for i in range(k,n):
        arr[i-k]=arr[i]
    j=0
    for i in range(n-k,n):
        arr[i]=temp[j]
        j+=1
    return arr
arr=[1,2,3,4,5]
print(rotate(arr,3))'''

# rotate right by k-notations
'''def rotate_right(nums,k):
    n=len(nums)
    k=k%n
    temp=[]
    for i in range(n-k,n):
        temp.append(nums[i])
    for i in range(n-k-1,-1,-1):
        nums[i+k]=nums[i]
    j=0
    for i in range(k):
        nums[i]=temp[j]
        j+=1
    return nums
nums=[1,2,3,4,5]
print(rotate_right(nums,3))'''

# move zero to last
''''def zero(arr):
    j=-1
    n=len(arr)
    for i in range(n):
        if(arr[i]==0):
            j=i
            break
    for i in range(j+1,n):
        if(arr[i]!=0):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
arr=[1,2,3,0,4,0,2,0]
print(zero(arr))
'''

# linear search
'''def search(arr,num):
    for i in range(len(arr)):
        if(arr[i]==num):
            return i
    return -1
arr=[1,2,4,6,7,4,5]
print(search(arr,8))'''

# union of two arrays
'''def union(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    st=set()
    for i in range(n1):
        st.add(arr1[i])
    for i in range(n2):
        st.add(arr2[i])
    temp=[]
    for i in st:
        temp.append(i)
    return temp
arr1=[1,2,3,4]
arr2=[2,1,3,5]
print(union(arr1,arr2))'''

# intersection of two arrays
'''def interrsection(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    temp=[]
    for i in range(n1):
        for j in range(n2):
            if(arr1[i]==arr2[j]):
                temp.append(arr1[i])
    return temp
arr1=[1,2,3,4,5]
arr2=[3,2,4,1]
print(interrsection(arr1,arr2))'''


'''def inter(a,b):
    n1=len(a)
    n2=len(b)
    temp=[]
    i=0
    j=0
    while(i<n1 and j<n2):
        if(a[i]<b[j]):
            i+=1
        elif(a[i]>b[j]):
            j+=1
        else:
            temp.append(a[i])
            i+=1
            j+=1
    return temp
a=[1,2,3,4,5]
b=[3,2,4,5,6]
print(inter(a,b))'''

# fing the missing number from 1 to n:
'''def missing(arr):
    for i in range(1,len(arr)+1):
        present=0
        for j in range(len(arr)):
            if(i==arr[j]):
                present=1
                break
        if(present==0):
            return i
arr=[1,2,3,4,6]
print(missing(arr))
'''

'''def missing(arr):
    dict={}
    for i in range(len(arr)):
        dict[arr[i]]=1
    for i in range(1,len(arr)+2):
        if i not in dict:
            return i
arr=[1,2,3,4,6]
print(missing(arr))'''

'''def missing(arr):
    n=len(arr)+1
    sum=n*(n+1)//2
    s2=0
    for i in arr:
        s2+=i
    return sum-s2
arr=[1,2,3,4,6]
print(missing(arr))'''



'''def consecutive(arr):
    maxi=0
    count=0
    for i in range(len(arr)):
        if(arr[i]==1):
            count+=1
            maxi=max(maxi,count)
        else:
            count=0
    return maxi
arr=[1,1,0,1,1,1,0,1]
print(consecutive(arr))'''


# find the element that appears once int twice array
'''def once(arr):
    for i in range(len(arr)):
        num=arr[i]
        cont=0
        for j in range(len(arr)):
            if(arr[j]==num):
                cont+=1
        if (cont==1):
            return num
arr=[1,1,2,2,3,4,4]
print(once(arr))'''

'''def once_repeated(arr):
    xor=0
    for i in range(len(arr)):
        xor=xor^arr[i]
    return xor
arr=[1,1,2,2,3,4,4]
print(once_repeated(arr))'''

# 2 sum problem
'''def two_sum(nums,k):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i==j):
                continue
            if(nums[i]+nums[j]==k):
                return i,j
nums=[2,5,4,-3,6]
print(two_sum(nums,9))'''

'''def two_sum(nums,k):
    seen={}
    for i in range(len(nums)):
        need=k-nums[i]
        if need in seen:
            return [seen[need],i]
        seen[nums[i]]=i
nums=[2,3,4,-3,6]
print(two_sum(nums,9))'''

# sort the array which contains 0,1,2's
'''def Sort(nums):
    cont1=0
    cont2=0
    cont3=0
    for i in range(len(nums)):
        if(nums[i]==0):
            cont1+=1
        elif(nums[i]==1):
            cont2+=1
        else:
            cont3+=1
    for i in range(cont1):
        nums[i]=0
    for i in range(cont1,cont1+cont2):
        nums[i]=1
    for i in range(cont2+cont1,len(nums)):
        nums[i]=2
    return nums
nums=[1,2,0,2,0,1,1,0]
print(Sort(nums))'''

'''def Sort(nums):
    low=0
    mid=0
    high=len(nums)-1
    while(mid<=high):
        if(nums[mid]==0):
            nums[mid],nums[low]=nums[low],nums[mid]
            mid+=1
            low+=1
        elif(nums[mid]==1):
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums
nums=[1,2,0,2,0,1,1,0]
print(Sort(nums))'''

# return the element which is n/2 size of the array
'''def majorityElement(nums):
    dict={}
    for i in nums:
        dict[i]=dict.get(i,0)+1         
                                    if i in cont:
                                        cont[i]+=1
                                    else:
                                        cont[i]=1
        
    for key,value in dict.items():
        if (value>=len(nums)//2):
            return key
nums=[2,2,3,3,3,4,2,2]
print(majorityElement(nums))'''

'''def majority(nums):
    size=len(nums)//2
    for i in range(len(nums)):
        cont=0
        for j in range(1,len(nums)):
            if(nums[i]==nums[j]):
                cont+=1
        if cont>=size:
            return nums[i]
nums= [1, 1, 1, 2, 1, 2]
print(majority(nums))'''

# maximum subarray from array
'''def Max_subarray(nums):
    maxi=float('-inf')
    for i in range(len(nums)):
        sum=0
        for j in range(i,len(nums)):
            sum+=nums[j]
            maxi=max(sum,maxi)
    return maxi
nums=[-2,-3,4,-1,-2,1,5,-3]
print(Max_subarray(nums))'''

'''def Max_subarray(nums):
    sum=0
    maxi=float('-inf')
    for i in range(len(nums)):
        sum+=nums[i] 
        if(sum>maxi):
            maxi=sum
        if(sum<0):
            sum=0
    return maxi
nums=[-2,-3,-4,-1,-2,-1,-5,-3]
print(Max_subarray(nums))'''

# rearrange the elements based on sign
'''def rearrange(nums):
    n=len(nums)
    positive=[]
    negitive=[]
    for i in range(n):
        if nums[i]>0:
            positive.append(nums[i])
        else:
            negitive.append(nums[i])
    for i in range(n//2):
        nums[2*i]=positive[i]
        nums[2*i+1]=negitive[i]
    return nums
nums=[1,2,-3,-4,6,-5]
print(rearrange(nums)) '''  

'''def rearrange(nums):
    ans=[0]*len(nums)
    pos=0
    neg=1
    for i in range(len(nums)):
        if(nums[i]<0):
            ans[neg]=nums[i]
            neg+=2
        else:
            ans[pos]=nums[i]
            pos+=2
    return ans
nums=[1,2,-3,-4,6,-5]
print(rearrange(nums))'''

'''def Rearrange(nums):
    n=len(nums)
    pos=[]
    neg=[]
    for i in range(n):
        if(nums[i]>0):
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    if(len(pos)>len(neg)):
        for i in range(len(neg)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        index=len(neg)*2
        for i in range(len(neg),len(pos)):
            nums[index]=pos[i]
            index+=1
    else:
        for i in range(len(pos)):
            nums[2*i]=pos[i]
            nums[2*i+1]=neg[i]
        index=len(pos)*2
        for i in range(len(pos),len(neg)):
            nums[index]=neg[i]
            index+=1
    return nums
nums=[1,2,-3,-4,3,5,-4,-2,-1]
print(Rearrange(nums))'''

# buy and sell stock
'''def stockBuySell(arr, n):
    mini=arr[0]
    profit=0
    for i in range(1,n):
        cost=arr[i]-mini
        profit=max(cost,profit)
        mini=min(mini,arr[i])
    return profit
arr=[7,1,5,3,6,4]
print(stockBuySell(arr,len(arr)))'''

'''def maxProfit(self, prices):
        profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            elif profit<prices[i]-buy:
                profit=prices[i]-buy
        return profit'''

# longest continued sequence
'''def consucutive(nums):
    cont=0
    num_set=set(nums)
    for i in num_set:
        if i-1 not in num_set:
            current=i
            length=1
            while current+1 in num_set:
                current+=1
                length+=1 
            cont=max(cont,length)
    return cont    
nums=nums = [1,2,3,10,11]
print(consucutive(nums)) '''

'''def fizzBuzz(n):
        lst=[]
        for i in range(n):
            if(i%3==0):
                print("Fizz")
            elif(i%5==0):
                print("Buzz")
            elif(i%3==0 and i%5==0):
                print("FizzBuzz")
            else:
                lst.append(i)
        return lst
print(fizzBuzz(5))'''

# zero matrix
'''def markcol(j):
    for row in range(len(nums)):
        if(nums[row][j]!=0):
            nums[row][j]=-1
def markrow(i):
    for col in range(len(nums)):
        if(nums[i][col]!=0):
            nums[i][col]=-1

def matrix(nums):
    n=len(nums)
    m=len(nums[0])
    for i in range(n):
        for j in range(m):
            if(nums[i][j]==0):
                markrow(i)
                markcol(j)
    for i in range(n):
        for j in range(m):
            if(nums[i][j]==-1):
                nums[i][j]=0
    return nums

nums = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(matrix(nums))'''