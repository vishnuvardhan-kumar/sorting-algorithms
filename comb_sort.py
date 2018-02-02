# Python implementation of Comb Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

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




 
