import time
import random

def rough_max_subarray(A,left,right):
    low = high = max_sum = 0
    n = right - left + 1
    for i in range(n):
        for j in range(i,n):
            cur_sum = 0
            for k in range(i,j+1):
                cur_sum += A[left+k]
            if cur_sum > max_sum:
                max_sum = cur_sum
                low = left+i
                high = left+j
    return(low,high,max_sum)

def get_random(low,high,n):
    A = [None]*n
    for i in range(n):
        A[i] = random.randint(low,high)
    return A

def recurr_max_cross_subarray(A,low,mid,high):
    low_sum = high_sum = cur_sum =0
    max_low = max_high = mid
    for i in range(mid,low-1,-1):
        cur_sum += A[i]
        if(cur_sum > low_sum):
            max_low = i
            low_sum = cur_sum
    cur_sum = 0
    for i in range(mid+1,high+1):
        cur_sum += A[i]
        if(cur_sum > high_sum):
            max_high = i
            high_sum = cur_sum
    return(max_low,max_high,high_sum+low_sum)

def recurr_max_subarray(A,low,high):
    if high == low:
        return(low,high,A[low])
    else:
        mid = (high+low)//2
        set_low = recurr_max_subarray(A,low,mid)
        set_high = recurr_max_subarray(A,mid+1,high)
        set_cross = recurr_max_cross_subarray(A,low,mid,high)
        set_max = max(set_low,set_high,set_cross,key = lambda x: x[2])
        return set_max

def mix(A,low,high):
    if high == low:
        return(low,high,A[low])
    elif high-low+1 <= 6:
        return rough_max_subarray(A,low,high)
    else:
        mid = (high+low)//2
        set_low = recurr_max_subarray(A,low,mid)
        set_high = recurr_max_subarray(A,mid+1,high)
        set_cross = recurr_max_cross_subarray(A,low,mid,high)
        set_max = max(set_low,set_high,set_cross,key = lambda x: x[2])
        return set_max

def max_subarray(A,low,high):
    cur_sum = max_sum = left = right = 0
    temp_left = 0
    for i in range(low,high+1):
        cur_sum += A[i]
        if cur_sum < 0:
            cur_sum = 0
            temp_left = i+1
        else:
            if(cur_sum > max_sum):
                max_sum = cur_sum
                right = i
                left = temp_left
    return(left,right,max_sum)

def test(low,high,n):
    A = get_random(low,high,n)
    start_time = time.clock()
    rough_res = rough_max_subarray(A,0,n-1)
    end_time = time.clock()
    rough_time = end_time - start_time
    start_time = time.clock()
    recurr_res = recurr_max_subarray(A,0,n-1)
    end_time = time.clock()
    recurr_time = end_time - start_time
    start_time = time.clock()
    mix_res = mix(A,0,n-1)
    end_time = time.clock()
    mix_time = end_time - start_time

    start_time = time.clock()
    res = max_subarray(A,0,n-1)
    end_time = time.clock()
    linear_time = end_time - start_time
    print("rough : %d  %d  %d  %fs" % (rough_res[0],rough_res[1],rough_res[2],rough_time))
    print("recurr: %d  %d  %d  %fs" % (recurr_res[0],recurr_res[1],recurr_res[2],recurr_time))
    print("mix   : %d  %d  %d  %fs" % (mix_res[0],mix_res[1],mix_res[2],mix_time))
    print("linear: %d  %d  %d  %fs" % (res[0],res[1],res[2],linear_time))

test(-10,10,500)
# A = get_random(-10,10,100)
# res1 = recurr_max_subarray(A,0,99)
# res2 = rough_max_subarray(A,100)
# for i in res1:
#     print(i)
# for i in res2:
#     print(i)
# start = time.clock()
# s = rough_max_subarray(A,1000)
# end = time.clock()
# print(end-start)

# for a in s:
#     print(a)
