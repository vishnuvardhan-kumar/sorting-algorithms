# Python implementation of Insertion Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

def insertion_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]



 
