# Python implementation of Merge Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

# Average performance on the data set
# Near : 0.05 seconds
# Random : 0.09 seconds
# Reverse : 0.07 seconds

from timeit import default_timer as timer
from heapq import merge
 
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


if __name__ == '__main__':

    time_taken = 0
    x = int(input("Enter number of trials : "))
    
    for n in range(1,x+1):
        with open("data/reverse.txt","r") as fileobj:
            list_to_sort = list(map(int, fileobj.readlines()))
            start = timer()
            r = merge_sort(list_to_sort, )
            current = timer()-start
            print(f"Running test {n} : {current:.2f} seconds")
            time_taken += current

    assert sorted(list_to_sort) == r

    time_taken /= x
    print(f"Merge sort: average time = {time_taken:.2f} seconds")

 
