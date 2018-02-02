# Python implementation of Bubble Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in xrange(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq




 
