'''#fabbanocci
def fab(n):
    # s=[]
    a,b=0,1
    for i in range(n):
        # print(a,end=" ")
        a,b=b,a+b
    return a
    
    #     s.append(a)
    #     a,b=b,a+b
    # return s
print(fab(5))

# factorial
def fact(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result
print(fact(5))

# palindrome
def palindrome(n):
    # m=str(n)
    if n==n[::-1]:
        return "palindrome"
    else:
        return "its not palindrome"
number=input("enter number: ")
print(palindrome(number))

# sum of numbers
def sumofnumber(n):
    result=0
    for i in n:
        result+=i
    return result
l=[1,2,3,4,5]
print(sumofnumber(l))

# prime numbers
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for num in range(2,50):
    if prime(num):
        print(num)'''

# leet code-747
'''def large(nums):
    num=nums[0]
    for i in range(1,len(nums)):
        if num<nums[i]:
            num=nums[i]
            k=i
    for j in range(len(nums)):
        if num<nums[j]*2:
            return -1
        return k
lst= [2,7,1,3]
print(large(lst))'''

'''ef reverse(num):
    result=0
    while num>0:
        last=num%10
        result=result*10+last
        num=num//10
    return result
print(reverse(456))'''

'''num=int(input("enter a num: "))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(f"sum of nums 1 to {num} is {sum}")
'''

'''nums=[1,2,3]
alpha=['a','b','c']
for i in nums:
    for j in alpha:
        print(j,end=" ")
    print(i,end=" ")'''

'''r=3
for i in range(4):
    for j in range(r):
        print("*",end=" ")
    print()
'''

'''for i in range(5):
        print("*"*3)
        # print()'''

'''r=10
for i in range(1,5):
    for j in range(i):
        print(r,end=" ")
        r-=1
    print()''' 

'''r=5
for i in range(r):
    for j in range(i):
        print(" ")
        for k in range'''


'''r=5
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''

'''
n=int(input("enter number: "))
l=1
for i in range(2,n+1):
    l+=i
print("factorial of n: ",l)'''

# squre
'''row=5
for i in range(row):
    for j in range(row):
        if i==0 or i==4 or j==0 or j==4:
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()'''
# triangle
'''row=5
for i in range(row):
    for j in range(i,row):
        print(' ',end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''
# reverse triange
'''row=5
for i in range(row):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,row):
        print("*",end=" ")
    for j in range(i,row-1):
        print("*",end=" ")
    print()'''

'''row=1
for i in range(1,5):
    for j in range(i):
        print(row,end=" ")
        row+=1
    print()'''


'''for i in range(1,11):
    print(i)
    i+=1
'''

'''row=5
for i in range(row):
    for j in range(i,row):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()

for i in range(1,4):
    for j in range(1,i+1):
        print(i,end=" ")
    print()'''
'''r=4
for i in range(r):
    for j in range(r):
        if i==0 or i==3 or j==0 or j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''row=5
for i in range(row):
    for j in range(row):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''row=5
for i in range(row):
    for j in range(row):
        if i==0 or j==0 or j==4 or i==2:
            print("*",end=" ")
        if(i>2 and j==2):
            print("*",end=" ")
            # if i== or j==2:
                # print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

'''r=5
for i in range(r):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()'''

# letter R
'''r=5
for i in range(r):
    for j in range(5):
        if i==0 or (i==j and i!=1) or j==0 or i==2 or (j==4 and i<3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
'''n = 5 
for i in range(5): 
    for j in range(5): 
        if i == 0 or (i == j and i !=1) or j == 0 or i == 2 or (j == 4 and i<3):
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print()'''

# letter J
'''r=5
for i in range(r):
    for j in range(r):
        if i==0 or j==2 or (i==4 and j<3) or (j==0 and i>2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


# letter u
'''r=5
for i in range(r):
    for j in range(r):
        if j==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''class stack:
    def __init__(self):
        self.array=[]
        self.top=-1
        self.max=100
    def isEmpty(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("its not empty")
    def isFull(self):
        if self.top==self.max-1:
            print("stack is full")
        else:
            print("stack is not full")
    def push(self,data):
        if self.isFull():
            print("stack is overflow")
        else:
            self.top+=1
            self.array.append(data)
            print(self.array)
    def pop(self):
        if self.isEmpty():
            print("stack id underflow")
        else:
            self.top-=1
            self.array.pop()
            print(self.array)
    def peek(self):
        print(self.array[self.top])
    def traverse(self):
        print(self.array[::-1])


s=stack()
while True:
    print("stack operations")
    print("1:push")
    print("2:pop")
    print("3:peek")
    print("4:traverse")
    print("5:exit")

    choice=input("enter a value: ")
    if choice=='1':
        val=int(input('enter a value: '))
        print(s.push(val))
    elif choice=='2':
        print("value is popped")
        s.pop()
    elif choice=='3':
        print("top value is")
        s.peek()
    elif choice=='4':
        print("elements in stack")
        s.traverse()
    elif choice=='5':
        print("exsting...")
        break
    else:
        print("invalid input")
    '''
'''class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.max = 100

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return self.rear == self.max - 1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            if self.isEmpty():
                self.front = self.rear = 0
            else:
                self.rear += 1
            self.queue.append(data)
            print("Queue:", self.queue)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Dequeued:", self.queue[self.front])
            self.front += 1
            if self.front > self.rear:
                self.front = self.rear = -1
                self.queue.clear()
            else:
                print("Queue:", self.queue[self.front:self.rear+1])

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front value:", self.queue[self.front])

    def traverse(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Elements in queue:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])

# 🚀 Menu-driven loop
q = Queue()
while True:
    print("\nQueue operations")
    print("1: Enqueue")
    print("2: Dequeue")
    print("3: Peek")
    print("4: Traverse")
    print("5: Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        val = int(input("Enter value to enqueue: "))
        q.enqueue(val)
    elif choice == '2':
        q.dequeue()
    elif choice == '3':
        q.peek()
    elif choice == '4':
        q.traverse()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid input")'''


'''class Queue:
    def __init__(self):
        self.queue=[]
        self.front=-1
        self.rear=-1
        self.max=100
    def isEmpty(self):
        return self.front==-1 and self.rear==-1
    def isFull(self):
        return self.rear==self.max-1
    def enqueue(self,data):
        if self.isFull():
            print("queue is full")
        else:
            if self.isEmpty():
                print("its empty")
            else:
                self.rear+=1
                self.queue.append(data)
                print(self.queue)
    def dequeue(self):
        if self.isEmpty():
            print("its empty")
        else:
            print("dequeued: ",self.queue[self.front])
            self.front+=1
            if self.front>self.rear:
                self.front=self.rear=-1
                self.queue.clear()
    def peek(self):
        print(f"top value is : {self.queue[self.front]}")
    def traverse(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i])
    
n=Queue()
while True:
    print("queue operations")
    print("1:enqueue")
    print("2:dequeue")
    print("3:peek")
    print("4:traverse")
    print("5:exit")

    choice=input("choose operation: ")
    if choice=='1':
        val=int(input("enter value: "))
        n.enqueue(val)
    elif choice=='2':
        print(f"{n.dequeue()} value is removed")
    elif choice=='3':
        print(f"top value is {n.peek()}")
    elif choice=='4':
        n.traverse()
    elif choice=='5':
        print("exsting from the queue")
        break
    else:
        print("invalid input")'''

#  find duplicate 
'''def duplicate(nums):
    seen=set()
    for i in nums:
        if i  in seen:
            return True
        seen.add(i)
    return False
nums=[1,1,1,3,3,4,3,2,4,2]
print(duplicate(nums))'''

# missing and repeated
'''def repeatedNumber(self, A):
        n=len(A)
        cnt=[0]*n+1
        for i in A:
            cnt[i]+=1
        repeated=-1
        missing=-1
        res=[]
        for i in cnt:
            if i==0:
                missing=i
                res.append(missing)
            elif i>1:
                repeated=i
                res.insert(0,repeated)
        return res'''


'''def duplicate(nums):
    n=len(nums)
    cnt=[0]*(n+1)
    for i in nums:
        cnt[i]+=1
    for i in range(1,n+1):
        if cnt[i]>1:
            return True
        else:
            return False
nums=[2,3,4,5,2,1]
print(duplicate(nums))'''


'''def duplicate(nums):
    n=len(nums)
    cnt=[0]*(n+1)
    for i in nums:
        cnt[i]+=1
    for i in range(1,n+1):
        if cnt[i]==1:
            return i
nums=[1,1,2,3,4,3,2]
print(duplicate(nums))'''

 

'''num=int(input())
for i  in range(2,num):
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
    if f==0:
        print(i)'''


'''def duplicate(nums):
    dicct={}
    for i in range(len(nums)):
        if nums[i] in dicct.keys():
            dicct[nums[i]] = dicct[nums[i]] + 1
        else:
            dicct[nums[i]] = 1
        
    for (key,value) in dicct.items():
        if value==1:
            return key
nums=[1,1,2,2,3,3,4]
print(duplicate(nums))'''

'''def largest(num):
    fl=float("-inf")
    sl=float("-inf")
    for i in range(0,len(num)):
        if fl<num[i]:
            sl=fl
            fl=num[i]
        if sl<num[i] and fl<num[i]:
            sl=num[i]
    return sl
num=[2,3,4,5,6]
print(largest(num))'''

# MISSING REPETED

'''def repeat(nums):
    res = []
    cnt = [0] * (max(nums) + 1)

    for i in nums:
        cnt[i] += 1

    repeatd = -1
    missing = -1

    for i in range(1,len(cnt)):
        if cnt[i] == 0:
            missing = i
        elif cnt[i] > 1:
            repeatd = i

    res.append(repeatd)
    res.append(missing)
    return res

nums = [1, 2, 3, 5, 3, 2]
print(repeat(nums))'''

'''def twice(nums):
    n=nums[0]
    k=0
    for i in range(1,len(nums)):
        if n<nums[i]:
            n=nums[i]
            k=i
    for j in range(0,len(nums)):
        if n==nums[j]:
            continue
        if n<nums[j]*2:
            return -1
    return k
nums=[1,2,3,4,9]
print(twice(nums))'''


# missing number
'''def missingNumber(nums):
         num=len(nums)
         dict={}
         for i in range(num+1):
             dict[i]=0
         for n in nums:
              dict[n]+=1
         for (key,value) in dict.items():
            if value==0:
                return key
nums=[0,1,2,4]
print(missingNumber(nums))'''

# missing and repeted
''''def mismatch(nums):
    dict={}
    n=len(nums)
    res=[]
    for i in nums:
        dict[i]=dict.get(i,0)+1
    repeted=-1
    missing=-1
    for i in range(1,n+1):
        if i not in dict:
            missing=i
        elif dict[i]>1:
            repeted=i
    return [missing,repeted]
nums=[8,9,11,12,13]
print(mismatch(nums))'''

'''def mismatch(nums):
    nums=[x for x in nums if x>0]
    nums.sort()
    var=1
    for n in nums:
        if n==var:
            var+=1
        elif n>var:
            break
    return var
nums=[8,9,11,12,13]
print(mismatch(nums))'''

'''for i in range(2,101):
    c=0
    for j in range(2,i+1):
        if i%j==0:
            c=1
    if c==0:
        print(i)'''


'''lst=[1,1,2,3,3]
dict={}
for i in lst:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1 
for i in lst:
    if dict[i]==1:
        print(i)'''        


# stack
'''lass stack:
    def __init__(self):
        self.arry=[]
        self.top=-1
        self.max=100
    def isEmpty(self):
        if self.top==-1:
            return "its empty"
    def isFull(self):
        if self.max-1==self.top:
            return "its full"
    def push(self,data):
        if self.isFull():
            print("stack is overflow")
        else:
            self.top+=1
            self.arry.append(data)
            print(self.arry)
    def pop(self):
        if self.isEmpty():
            print("stack is overflow")
        else:
            self.top-=1
            self.arry.pop()
            print(self.arry)
    def peek(self):
        print(self.arry[self.top])
    def traverse(self):
        print(self.arry[::-1])

s=stack()
while True:
    print("....stack operationds...")
    print("1:push\n")
    print("2:pop\n")
    print("3:peek\n")
    print("4:traverse\n")
    print("5:exit")

    choice=input("choose operation: ")
    if choice=="1":
        val=int(input("enter value to push: "))
        print(f"{val} pushed into stack:")
        s.push(val)
    elif choice=="2":
        print("top value is removed")
        s.pop()
    elif choice=="3":
        print("top of the stack is: ")
        s.peek() 
    elif choice=="4":
        s.traverse()
    elif choice=="5":
        print("terminate the program")
    else:
        print("invalid")'''

 
'''for i in range(2,101):
    count=0
    for j in range(2,i):
        if i%j==0:
            count=1
    if count==0:
        print(i)'''

'''n=int(input("enter num: "))
c=0
for i in range(2,n):
    if n%i==0:
        c=1
if c==0:
    print("its a prime")
else:
    print("its not prime")'''

'''import random
def guessing(num):
    rand_num=random.randint(1,num)
    guess=0
    while rand_num!=guess:
        guess=int(input(f"enter a value between 1 and {num}: "))
        if guess>rand_num:
            print("guess a lower number😒😒")
        elif guess<rand_num:
            print("guess a higher number😊😊")
    return "congrts🎉🎊!! its correct"
# num=int(input("enter lenth: "))
print(guessing(10))'''


'''def rev(n):
    num=str(n)
    rev=num[::-1]
    return rev
print(rev(123))'''

# reverse an integer
'''def reverse(n):
    result=0
    while(n>0):
        left=n%10
        result=result*10+left
        n=n//10
    return result
n=123
print(reverse(n))'''

'''# countdown timer
import time
start=int(input("enter time: "))
speed=int(input("enter speed: "))
while start>0:
    print(start)
    time.sleep(speed)
    start-=1
print("time up")'''

class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.max = 100

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return self.rear == self.max - 1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            if self.isEmpty():
                self.front = self.rear = 0
            else:
                self.rear += 1
                self.queue.append(data) 
                print("Queue:", self.queue)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Dequeued:", self.queue[self.front])
            self.front += 1
            if self.front > self.rear:
                self.front = self.rear = -1
                self.queue.clear()
            else:
                print("Queue:", self.queue[self.front:self.rear+1])

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front value:", self.queue[self.front])

    def traverse(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Elements in queue:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])

# 🚀 Menu-driven loop
q = Queue()
while True:
    print("\nQueue operations")
    print("1: Enqueue")
    print("2: Dequeue")
    print("3: Peek")
    print("4: Traverse")
    print("5: Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        val = int(input("Enter value to enqueue: "))
        q.enqueue(val)
    elif choice == '2':
        q.dequeue()
    elif choice == '3':
        q.peek()
    elif choice == '4':
        q.traverse()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid input")

