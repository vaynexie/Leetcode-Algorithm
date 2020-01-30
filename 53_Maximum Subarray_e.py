

"""
1) Divide the given array in two halves
2) Return the maximum of following three
….a) Maximum subarray sum in left half (Make a recursive call)
….b) Maximum subarray sum in right half (Make a recursive call)
….c) Maximum subarray sum such that the subarray crosses the midpoint

The lines 2.a and 2.b are simple recursive calls. How to find maximum subarray sum such that the subarray crosses the midpoint? 
The idea is simple, find the maximum sum starting from mid point and ending at some point on left of mid, 
then find the maximum sum starting from mid + 1 and ending with sum point on right of mid + 1. 
Finally, combine the two and return.

"""

#O(n) time
class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        currmax = arr[0]
        glomax = arr[0]
        for ii in range(1, len(arr)) :
            currmax = max(currmax + arr[ii], arr[ii])
            glomax = max(glomax, currmax)
        return glomax
        
 #my v
 def maxSub(nums):
    mid=round(len(nums)/2)
    left=nums[:mid]
    right=nums[mid+1:]


    right_value=0
    right_max=right_value

    k=0
    if len(right)==1:
        right_index=0
    for i in right:
        right_value+=i
        k+=1
        if right_value>right_max:
            right_index=k
            right_max=right_value
        else:
            right_index=0

    left_value=left_sum+nums[mid]
    left_max=left_value

    l=0
    if len(left)==1:
        left_index=0
    for j in left:
        left_value-=j
        l+=1
        if left_value>left_max:
            left_index=l
            left_max=left_value
        else:
            left_index=0

    cross_sum=left_max+right_max

    if cross_sum>left_sum and cross_sum>right_sum:
        newnums=nums[left_index:mid+1]+right[:right_index]
    else:
        if left_sum>right_sum:
            newnums=nums[:mid+1]
        else:newnums=right

    return newnums,max(cross_sum,left_sum,right_sum)
    
kk=9999
newValue=0
while kk>0:
    maxValue=newValue
    nums,newValue=maxSub(nums)
    if newValue>maxValue:
        break
    if len(nums)<2:
        break
print(newValue)

#better v
def maxCrossingArray(A, low, mid, high):
    left_sum = float("-inf")
    summ = 0
    for i in range(mid, -1, -1):
        summ = summ + A[i]
        if summ > left_sum:
            left_sum = summ
    right_sum = float("-inf")
    summ = 0
    for j in range(mid + 1, high + 1, 1):
        summ = summ + A[j]
        if summ > right_sum:
            right_sum = summ
    return left_sum + right_sum

def maxSubArray(A, low, high):
    if high == low:
        return A[low]
    else:
        mid = (low + high) // 2
        left_sum = maxSubArray(A, low, mid)
        right_sum = maxSubArray(A, mid + 1, high)
        cross_sum = maxCrossingArray(A, low, mid, high)
        return max(left_sum, right_sum, cross_sum)
