# Python implementation of Quick Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

# Average performance on the data set
# Near : 0.06 seconds
# Random : 0.03 seconds
# Reverse : 0.04 seconds

from timeit import default_timer as timer

def quick_sort(array):
    _quicksort(array, 0, len(array) - 1)
 
def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)


if __name__ == '__main__':

    time_taken = 0
    x = int(input("Enter number of trials : "))
    
    for n in range(1,x+1):
        with open("data/random.txt","r") as fileobj:
            list_to_sort = list(map(int, fileobj.readlines()))
            start = timer()
            l = quick_sort(list_to_sort)
            current = timer()-start
            print(f"Running test {n} : {current:.2f} seconds")
            time_taken += current
    
    assert sorted(list_to_sort) == l
    
    time_taken /= x
    print(f"Quick sort: average time = {time_taken:.2f} seconds")
