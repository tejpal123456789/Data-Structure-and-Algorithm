
arr = [100, 200, 300, 400]
k=2

x=float('-inf')
def max_sum_subarray(arr,k):
 j=0
 i=0
 sum=0
 while j<len(arr):
    sum=sum+arr[j]      # summing elements of array
    if j-i+1<k:
         j=j+1          # increment of box

    elif j-i+1==k:
        
        mx=max(sum,x)         # finding max sum by previous sum of same sliding window
         
        sum=mx-arr[i]

        j=j+1
        i=i+1

 return mx
        
print(max_sum_subarray(arr,k))
