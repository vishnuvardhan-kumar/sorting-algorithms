# Python implementation of Comb Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

# Average performance on the data set
# Near : 1.72 seconds
# Random : 2.03 seconds
# Reverse : 1.82 seconds

from timeit import default_timer as timer

def comb_sort(array):
    gap = len(array)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(array) - gap):
            j = i+gap
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True


if __name__ == '__main__':

    time_taken = 0
    x = int(input("Enter number of trials : "))
    
    for n in range(1,x+1):
        with open("data/reverse.txt","r") as fileobj:
            list_to_sort = list(map(int, fileobj.readlines()))
            start = timer()
            comb_sort(list_to_sort)
            current = timer()-start
            print(f"Running test {n} : {current:.2f} seconds")
            time_taken += current
    
    assert sorted(list_to_sort) == list_to_sort

    time_taken /= x
    print(f"Comb sort: average time = {time_taken:.2f} seconds")       



 
