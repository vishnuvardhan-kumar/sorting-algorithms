# Python implementation of Cycle Sort adapted from RosettaCode
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

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




 
