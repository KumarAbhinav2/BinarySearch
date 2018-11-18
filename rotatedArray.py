# Solution

# Trick: The simple trick to solve this problem is to get the index of smallest element in 
#        this array

input_array = [4, 5, 6, 7, 0, 1, 2]

def getRotations(arr, N):
        start = 0
        end = len(arr)-1        
        while start <= end:            
            # if array is already sorted
            if arr[start] <= arr[end]:
                return start
            mid = int((start+end)/2)
            # we need to calculate previous and next elements as pivot element should be less than prev and next elements
            # dividing by modulo as element might be the last one as well            
            prev = (mid + N - 1)%N
            nextt = (mid + 1)%N
            if arr[mid] <= arr[prev] and arr[mid] <= arr[nextt]:
                return mid
            elif arr[mid] <= arr[end]:
                end = mid - 1
            elif arr[mid] >= arr[start]:
                start = mid + 1
        return -1
