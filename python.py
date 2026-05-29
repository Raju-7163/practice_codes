
'''n= int(input())
f = 0
for i in range(2,n):
    if n%i ==0:
        f +=1
        break
if f == 0:
    print("Its prime")
else:
    print("Not prime")'''

'''n = int(input())
for i in range(2,n):
    f = 0
    for j in range(2,i):
        if i%j == 0:
            f = 1
            break
    if f == 0:      
        print(i)'''

'''def large(nums):
    fl=float("-inf")
    sl=float('-inf')
    for i in nums:
        if i>fl:
            sl=fl
            fl=i
        if (i>sl and i!=fl):
            sl=i
    return sl
nums=[-3,-4,-2,-5]
print(large(nums))'''
'''

class Solution(object):
    def secondHighest(self, n):
        
        l = float("-inf")
        sl = float("-inf")
        for i in range(0,len(n)):
            if l < n[i]:
                sl = l
                l = n[i]
            if sl < n[i] and n[i] < l:
                sl = n[i]
        return sl
r=Solution()
nums=[-2,-3,-4,-1]
print(r.secondHighest(nums))'''

'''def duplicate(nums):
    dicct= {}
    for i in range(len(nums)):
        if nums[i] in dicct.keys():
            dicct[nums[i]]=dicct[nums[i]]+1
        else:
            dicct[nums[i]]=1
    for(key,value) in dicct.items():
        if value==1:
            return key
nums=[1,2,3,4,4,2]
print(duplicate(nums))
'''
    
'''for i in range(2,101):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=1
    if c==0:
        print(i)'''

'''def duplicate(nums):
    temp=[]
    j=0
    nums.sort()
    for i in range(1,len(nums)):
        if(nums[i]!=nums[j]):
            nums[j+1]=nums[i]
            j+=1
        else:
            temp.append(nums[i])
    return nums[:j]
nums=[1,1,2,3,4,2,5]
print(duplicate(nums))'''

'''def largest(nums):
    max=nums[0]
    second_max=float('inf')
    for i in range(len(nums)):
        if(nums[i]>max):
            second_max=max
            max=nums[i]
    for j in range(len(nums)):
        if(nums[j]<max and nums[j]>second_max):
            second_max=nums[j]
    return second_max
nums=[1,2,7,3,4]
print(largest(nums))'''

'''def smallest(nums):
    small=nums[0]
    second_smallest=float('-inf')
    for i in range(len(nums)):
        if(nums[i]<small):
            second_smallest=small
            small=nums[i]
    for j in range(len(nums)):
        if(nums[j]>small and nums[j]<second_smallest):
            second_smallest=nums[j]
    return second_smallest
nums=[1,4,5,3,6,4]
print(smallest(nums))'''


'''def Sorted(nums):
    for i in range(1,len(nums)):
        if(nums[i]<nums[i-1]):
            return False
        return True
nums=[1,3,4,5]
print(Sorted(nums))'''

'''def duplicates(nums):
    nums.sort()
    temp=[]
    for i in range(len(nums)):
        if(nums[i]==nums[i-1]):
            temp.append(nums[i])
    return temp
nums=[1,1,2,3,3,4]
print(duplicates(nums))'''


'''def duplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1     
    return arr[:i+1] #return i+1
arr=[1,1,1,2,2,3,3,4]
print(duplicates(arr))'''

'''def left_shift(nums):
    temp=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[len(nums)-1]=temp
    return nums
nums=[1,2,3,4]
print(left_shift(nums))'''

'''def right_shift(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-1,0,-1):
        nums[i]=nums[i-1]
    nums[0]=temp
    return nums
nums=[1,2,3,4]
print(right_shift(nums))'''

'''def rotate(nums,k):
    n=len(nums)
    k=k%n
    temp=[]
    for i in range(k):
        temp.append(nums[i])
    for i in range(k,n):
        nums[i-k]=nums[i]
    j=0
    for i in range(n-k,n):
        nums[i]=temp[j]
        j+=1
    return nums
nums=[1,2,3,4,5]
print(rotate(nums,3))
'''
'''def zero(nums):
    j=-1
    n=len(nums)
    for i in range(n):
        if(nums[i]==0):
            j=i
            break
    for i in range(j+1,n):
        if(nums[i]!=0):
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
    return nums
nums=[1,0,2,3,0,0,4]
print(zero(nums))'''


'''def zero(nums):
    n=len(nums)
    ze=-1
    for i in range(n):
        if(nums[i]==0):
            ze=i
            break
    for i in range(ze+1,n):
        if(nums[i]!=0):
            nums[i],nums[ze]=nums[ze],nums[i]
            ze+=1
    return nums
nums=[1,2,0,3,0,4,0]
print(zero(nums))'''

'''def union(nums1,nums2):
    temp=set()
    n1=len(nums1)
    n2=len(nums2)
    for i in range(n1):
        temp.add(nums1[i])
    for j in range(n2):
        temp.add(nums2[j])
    return list(temp)
nums1=[1,2,3,4,5]
nums2=[2,6,7,4,3]
print(union(nums1,nums2))'''

'''def intersection(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)
    temp=[]
    for i in range(n1):
        for j in range(n2):
            if(nums1[i]==nums2[j]):
                temp.append(nums1[i])
    return temp
nums1=[1,2,3,4,5]
nums2=[2,6,7,5,8]
print(intersection(nums1,nums2))'''

'''def missing(nums):
    n=len(nums)+1
    n1=n*(n+1)//2
    sum=0
    for i in nums:
        sum+=i
    return n1-sum
nums=[1,2,3,4,6]
print(missing(nums))'''

'''def twice(nums):
    n=len(nums)
    for i in range(n):
        num=nums[i]
        count=0
        for j in range(n):
            if(nums[j]==num):
                count+=1
        if count==1:
            return num
nums=[1,1,2,2,3,4,4]
print(twice(nums))'''


'''def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left_arr=merge_sort(nums[:mid])
    right_arr=merge_sort(nums[mid:])
    return merge(left_arr,right_arr)
def merge(left_arr,right_arr):
    i=0
    j=0
    temp=[]
    while(i<len(left_arr) and j<len(right_arr)):
        if(left_arr[i]<right_arr[j]):
            temp.append(left_arr[i])
            i+=1
        else:
            temp.append(right_arr[j])
            j+=1
    temp.extend(left_arr[i:])
    temp.extend(right_arr[j:])
    return temp
nums=[0,2,1,0,2,1,0,2,]
print(merge_sort(nums))'''


'''def intersection(lst1,lst2):
    result=[]
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if(lst1[i]==lst2[j]):
                result.append(lst1[i])
    return result
lst1=[1,2,3,7,8]
lst2=[4,5,6,7,8]
print(intersection(lst1,lst2))
'''

'''def vowels(nums):
    vow="aeiouAEIOU"
    for str in nums:
        cont=0
        for i in str: 
            if i in vow:
                cont+=1
        print(f"{str}: {cont}")
nums=["raju","kumar","egg"]
print(vowels(nums))'''


'''def twice(nums):
    for i in range(len(nums)):
        cont=0
        num=nums[i]
        for j in range(len(nums)):
            if num==nums[j]:
                cont+=1
        if cont==1:
            return num
nums=[1,1,2,2,3,4,4]
print(twice(nums))
'''
'''def twice(nums):
    xor=0
    for i in range(len(nums)):
        xor=xor^nums[i]
    return xor
nums=[1,1,2,2,3,4,4]
print(twice(nums))'''


'''class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create(root,data):
    if(root==None):
        return Tree(data)
    if(root.data>data):
        root.left=create(root.left,data)
    elif(root.data<data):
        root.right=create(root.right,data)
    return root
def inorder(root):
    if(root==None):
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
def height(root):
    if(root==None):
        return 0
    left=height(root.left)
    right=height(root.right)
    if(left>=right):
        return left+1
    else:
        return right+1
def leaf(root):
    if(root==None):
        return 0
    if(root.left==None and root.right==None):
        print(root.data)
    leaf(root.left)
    leaf(root.right)
def mirror(root):
    if(root==None):
        return
    root.left,root.right=root.right,root.left
    mirror(root.left)
    mirror(root.right)


def solve(root,ans,level):
    if root==None:
        return
    if level==len(ans):
        ans.append(root.data)
    solve(root.left,ans,level+1)
    solve(root.right,ans,level+1)
def leftview(root):
    ans=[]
    solve(root,ans,0)
    return ans

def leaf(root,ans):
        if(root==None):
            return
        if(root.left==None and root.right==None):
            ans.append(root.data)
        leaf(root.left,ans)
        leaf(root.right,ans)
def leftside(root,ans):
        if root==None:
            return 
        if root.left==None and root.right==None:
            return
        ans.append(root.data)
        if(root.left!=None):
            leftside(root.left,ans) 
        else:
            leftside(root.right,ans)
def rightside(root,ans):
        if root==None:
            return 
        if root.left==None and root.right==None:
            return
        ans.append(root.data)
        if(root.right!=None):
            rightside(root.right,ans)
        else:
            rightside(root.left,ans)

def boundry_traversal(root):
    ans=[]
    ans.append(root.data)
    leftside(root.left, ans)
    leaf(root.left, ans)
    leaf(root.right, ans)
    rightside(root.right, ans)
    return ans

root=None
arr=[4,2,6,5,7,1]
for i in arr:
    root=create(root,i)
print(f"height: {height(root)}")
inorder(root)
mirror(root)
print(f"leaf:")
leaf(root)
print(leftview(root))
print(boundry_traversal(root))'''


'''def Sort(nums):
    low=0
    mid=0
    high=len(nums)-1
    while (mid<=high):
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
nums=[1,2,0,2,0,1,2,0]
print(Sort(nums))'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def add(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            n.next=newnode
    def display(self):
        n=self.head
        while n!=None:
            print(n.data,"-->",end="")
            n=n.next
        print("None")

    def reverse(self):
        temp=self.head
        prev=None
        while temp!=None:
            nextnode=temp.next
            temp.next=prev
            prev=temp
            temp=nextnode
        self.head=prev
        return prev
l=Linked_list()
for i in range(4):
    data=int(input())
    l.add(data)
l.reverse()
l.display()'''

'''def merge(arr1,arr2):
    merged=[]
    i=0
    j=0
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]<arr2[j]):
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        merged.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        merged.append(arr2[j])
        j+=1
    return merged
arr1=[1,2,3,4]
arr2=[2,3,4,5]
print(merge(arr1,arr2))'''

'''def subarr(nums):
    sum=0
    maxi=float("-inf")
    for i in range(len(nums)):
        sum+=nums[i]
        if(sum>maxi):
            maxi=sum
        if sum<0:
            sum=0
    return maxi
nums=[-2,-3,4,-1,-2,1,5,-3]
print(subarr(nums))'''

'''def stock(nums):
    profit=0
    max_profit=0
    buy=nums[0]
    for i in range(1,len(nums)):
        sell=nums[i]-buy
        max_profit=max(max_profit,sell)
        buy=min(nums[i],buy)
    return max_profit
nums=[7,1,5,3,6,4]
print(stock(nums))'''

'''def two_sum(nums,k):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i==j):
                continue
            if(nums[i]+nums[j]==k):
                return nums[i],nums[j]
nums=[1,2,3,4,5,6]
print(two_sum(nums,11))'''

'''def two_sum(nums,k):
    seen={}
    for i in range(len(nums)):
        need=k-nums[i]
        if need in seen:
            return seen[need],nums[i]
        else:
            seen[nums[i]]=nums[i]
nums=[1,2,3,4,5,6]
print(two_sum(nums,11))'''

'''def twice(nums):
    xor=0
    for i in range(len(nums)):
        xor=xor^nums[i]
    return xor
nums=[1,2,3,1,2,3,4]
print(twice(nums))'''

'''def consicutive(nums):
    maxi=0
    cont=0
    for i in range(len(nums)):
        if(nums[i]==1):
            cont+=1
            maxi=max(cont,maxi)
        else:
            cont=0
    return maxi
nums=[1,1,0,1,1,1,0,0,1,1,1,1]
print(consicutive(nums))'''

'''def missing(nums):
    n=len(nums)+1
    total=0
    # for i in range(n):
    sum=n*(n+1)//2
    for i in nums:
        total+=i
    return sum-total
nums=[1,2,3,5,6]
print(missing(nums))'''

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

'''def majority(nums):
    size=len(nums)//2
    cont={}
    for i in nums:
        if i in cont:
            cont[i]+=1
        else:
            cont[i]=1
    for key,value in cont.items():
        if value>=size:
            return key
nums= [7, 0, 0, 1, 7, 7, 2, 7, 7]
print(majority(nums))'''
    
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
print(consucutive(nums))  '''

def rotete(nums,k):
    n=len(nums)
    dict={}
    for i in range(n):
        need=k-nums[i]
        if need in dict:
            return [dict[need],i]
        else:
            dict[nums[i]]=i
nums=[1,3,4,5,6]
# nums1=[4,5,6,7,8]
print(rotete(nums,7))