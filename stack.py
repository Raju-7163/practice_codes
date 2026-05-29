'''class stack:
    def __init__(self):
        self.array=[]
        self.top=-1
        self.max=100
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.top==self.max-1:
            return True
        else:
            return False
    def push(self,data):
        if self.isFull():
            print('stack is overflow')
        else:
            self.top+=1
            self.array.append(data)
            print(self.array)
    def pop(self):
        if self.isEmpty():
            print("stack is underflow")
        else:
            self.top-=1
            self.array.pop()
            print(self.array)
    def peek(self):
        print(self.array[self.top])
s=stack()
print(s.isEmpty())
print(s.isFull())
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.pop()
s.peek()  
s.peek()  '''

'''a={1:"raju",2:"rani",3:"ram"}
for i in a.values():
    print(i)
for i in a.keys():
    print(i)
for i in a.items():
    print(i)'''

# s={6,7,8,9,6,6}
# print(a.union(s))
# print(a.intersection(s))
# print(a.difference(s))
# print(a.symmetric_difference(s))

'''sum=0
l=[3,7,1,2,4,8,]
print(max(l))
print(min(l))
for i in l:
    sum=sum+i
print(sum)'''

'''l=[1,2,3,4,3,2,1,4]
s=set(l)
a=list(s)
nl=[]
for i in l:
    if i in nl:
        continue
    else:
        nl.append(i)
print(nl)
print(a)'''


'''sum=0
n=input()
a=[int(c) for c in input().split(",")]
for i in a:
    if i==n:
        sum+=1
print(sum)'''

'''s1={2,1,3,4,5,3,2} 
s2={9,7,6,5,2,3,4,1}
iset=s1.union(s2)
uset=s1.intersection(s2)
print(iset,uset)'''

'''d={"name":"raju","age":18,"city":"gujarat"}
print(d['name'])
print(d["age"])
print(d["city"])
d["city"]="ap"
print(d)
for i,j in d.items():
    print(i,j)
'''

'''d={}
a= input("enter name")
b=input("enter age")
c=input("city")
d["name"]=a
d["age"]=b
d["city"]=c
print(d)'''

'''p=input("enter num:")
reverse=p[::-1]
if reverse==p:
    print("it is a palindrome")
else:
    print("its not")'''

'''class stack:
    def __init__(self):
        self.array=[]
        self.top=-1
        self.max=100
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.top==self.max-1:
            return True
        else:
            return False
    def push(self,data):
        if self.isFull():
            print('stack is overflow')
        else:
            self.top+=1
            self.array.append(data)
            print(self.array)
    def pop(self):
        if self.isEmpty():
            print("stack is underflow")
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
    print('\n----stack operations-----')
    print("1:push")
    print("2:pop")
    print("3:peek")
    print("4:traverse")
    print("5:exit")
    choice=input("enter a value b/w 1 to 5: ")
    if choice=='1':
        val=int(input("enter a value for push: "))
        s.push(val)
    elif choice=='2':
        s.pop()
    elif choice=='3':
        s.peek()
    elif choice=='4':
        s.traverse()
    elif choice=='5':
        print("existing....")
        break
    else:
        print('invalid')'''

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
        print("Invalid input")


        
'''

'''def large(s):
    s=set(s)
    nums=[]
    numbers="1234567890"
    for i in s:
        if i in numbers:
            nums.append(i)
    if len(nums)<=1:
        return -1
    nums.sort()
    return int(nums[-2])
s='abc234b9n'
print(large(s))
'''
        

'''def large(nums):
    fl=-1
    sl=-1
    for i in nums:
        if i>fl:
            sl=fl
            fl=i
        if (i>sl and i!=fl):
            sl=i
    return sl
nums=[8,6,7,3,9]
print(large(nums))'''

'''class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1
        self.size = 100

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top += 1
            self.arr.append(data)
            print(f"{data} pushed to stack")

    def pop(self):
        if self.isEmpty():
            print("Stack underflow! Cannot pop element.")
        else:
            popped = self.arr.pop()
            self.top -= 1
            print(f"{popped} popped from stack")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(f"Top element is {self.arr[self.top]}")

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements (top to bottom):", self.arr[::-1])


# Menu-driven program
s = Stack()
while True:
    print("\n1. Push\n2. Pop\n3. Peek\n4. Check Empty\n5. Check Full\n6. Display\n7. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value to push: "))
        s.push(val)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        print("Stack is empty" if s.isEmpty() else "Stack is not empty")
    elif choice == 5:
        print("Stack is full" if s.isFull() else "Stack is not full")
    elif choice == 6:
        s.display()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")'''


# balancing symabols
'''def is_matching(open,close):
    return (open=="(" and close==")") or (open=="[" and close=="]") or (open=="{" and close=="}")
def is_balanced(exp):
    stack=[]

    for ch in exp:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack:
                return False
            open=stack.pop()
            if not is_matching(open,ch):
                return False
        else:
            continue
    
    return len(stack)==0
exp="()[{}()]}"
if is_balanced(exp):
    print("balanced")
else:
    print("its not balanced")
            '''

'''def Sum(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    left=0
    for i in range(len(arr)):
        right=total-left-arr[i]
        if(right==left):
            return i
        left+=arr[i]
    return -1
arr=[3,2,-1,8,4]
print(Sum(arr))'''


'''def set_min():
    print(s2.pop())
    s1.pop()
    # s1.pop()
# def get_min(nums):
nums=[1,4,3,5,6]
min_val=1000
s1=[]
s2=[]
for i in nums:
    s1.append(i)
    if(i<min_val):
        min_val=i
    s2.append(min_val)
set_min()
set_min()
set_min()
set_min()'''


'''def greater(nums,s,ans):
    for i in range(len(nums)-1,-1,-1):
        while s and nums[i]>=s[-1]:
            s.pop()
        if len(s)==0:
            ans.append(-1)
        else:
            ans.append(s[-1])
        s.append(nums[i])
    print(ans[::-1])
nums=[4,3,8,7,1]
s=[]
ans=[]'''




        