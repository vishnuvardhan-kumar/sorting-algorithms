# Python implementation of Cycle Sort adapted from RosettaCode
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

# Average performance on the data set
# Near : 8.45 seconds
# Random : 10.36 seconds
# Reverse : 9.40 seconds

from timeit import default_timer as timer

def cycle_sort(vector):
    writes = 0
    for cycleStart, item in enumerate(vector):
        pos = cycleStart
        for item2 in vector[cycleStart + 1:]:
            if item2 < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == vector[pos]:
            pos += 1
        vector[pos], item = item, vector[pos]
        writes += 1
        while pos != cycleStart:
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if item2 < item:
                    pos += 1
            while item == vector[pos]:
                pos += 1
            vector[pos], item = item, vector[pos]
            writes += 1
 
    return writes


if __name__ == '__main__':

    time_taken = 0
    x = int(input("Enter number of trials : "))
    
    for n in range(1,x+1):
        with open("data/reverse.txt","r") as fileobj:
            list_to_sort = list(map(int, fileobj.readlines()))
            start = timer()
            w = cycle_sort(list_to_sort)
            current = timer()-start
            print(f"Running test {n} : {current:.2f} seconds")
            time_taken += current

    assert sorted(list_to_sort) == w

    time_taken /= x
    print(f"Cycle sort: average time = {time_taken:.2f} seconds")       



 
