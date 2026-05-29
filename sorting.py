# bubble sort
'''def bubble(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[4,2,3,1,5]
print(bubble(arr))'''

# selection sort
'''def selection(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if(arr[mini]>arr[j]):
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr
arr=[1,2,3,8,2,4]
print(selection(arr))'''

# insertion sort
'''def insertion(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while(j>0 and arr[j]<arr[j-1]):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
arr=[4,2,3,5,4,1]
print(insertion(arr))'''

# merge sort
''''def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_arr=merge_sort(arr[:mid])
    right_arr=merge_sort(arr[mid:])
    return merge(left_arr,right_arr)
    # merge_sort(right_arr)

    # merge_part
def merge(left_arr,right_arr):
    result=[]
    i=0
    j=0
    # k=0
    while(i<len(left_arr) and j<len(right_arr)):
        if left_arr[i]<right_arr[j]:
            result.append(left_arr[i])
            i+=1
        else:
            result.append(right_arr[j])
            j+=1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
    return result
arr=[3,2,4,6,5,1]
print(merge_sort(arr))'''

# quick sort
'''def quick_sort(arr,left,right):
    if left<right:
        partition_pos=partition(arr,left,right)
        quick_sort(arr,left,partition_pos-1)
        quick_sort(arr,partition_pos+1,right)
            
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]
    while(i<j):
        while(arr[i]<pivot and i<right):
            i+=1
        while(j>left and pivot<=arr[j]):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    if(arr[i]>pivot):
        arr[i],arr[right]=arr[right],arr[i]
    return i
arr=[6,5,4,3,2,1]
quick_sort(arr,0, len(arr)-1)
print(arr)
'''