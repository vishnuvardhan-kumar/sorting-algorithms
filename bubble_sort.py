# Python implementation of Bubble Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

# Average performance on the data set
# Near : 16.61 seconds
# Random : 19.45 seconds
# Reverse : 23.91 seconds

from timeit import default_timer as timer

def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq


if __name__ == '__main__':

    time_taken = 0
    x = int(input("Enter number of trials : "))
    
    for n in range(1,x+1):
        with open("data/reverse.txt","r") as fileobj:
            list_to_sort = list(map(int, fileobj.readlines()))
            start = timer()
            l=bubble_sort(list_to_sort)
            current = timer()-start
            print(f"Running test {n} : {current:.2f} seconds")
            time_taken += current
    
    assert sorted(list_to_sort) == l

    time_taken /= 5
    print(f"Bubble sort: average time = {time_taken:.2f} seconds")       

 
