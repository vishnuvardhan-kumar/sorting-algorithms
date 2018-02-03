# Python script to generate random lists for algorithm benchmarking.
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

import random
import time

def generate_data_set(skew = "random", length=10000, filename = "dataset.txt"):

    """
    The argument skew decides the distribution of numbers in the resultant
    data set. The valid options are:
    
    random = Python's default Mersenne Twister algorithm
    near = Nearly sorted data
    reverse = Nearly sorted but reversed data
    """

    start_stamp = time.time()
    
    try:
        with open(filename, "w") as fileobj:

            # Inefficient space usage when dealing with large length
            base_data = [random.randint(1,length) for _ in range(length)]

            if skew == "random":
                fileobj.write('\n'.join(map(str,base_data)))
                return time.time()-start_stamp
            
            elif skew == "near":
                partial_sort(base_data)
                fileobj.write('\n'.join(map(str,base_data)))
                return time.time()-start_stamp
            
            elif skew == "reverse":
                partial_sort(base_data)
                fileobj.write('\n'.join(map(str,base_data[::-1])))
                return time.time()-start_stamp
            
            else:
                raise ValueError
            
    except IOError:
        return -1
    except ValueError:
        return -1

def partial_sort(seq):
    """
    Uses a deterministic sort to order 3/4th of seq's elements.
    """
    for i in range(1, int(0.75 * len(seq))):
        key = seq[i]
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]


if __name__ == '__main__':
      pass
##    Uncomment the following lines for autotesting
##
##    passed = failed = 0
##    totaltime = 0
##    n = int(input("Enter number of tests to run : "))
##    
##    for _ in range(n):
##        try:
##            timed = generate_data_set(random.choice(['random','near','reverse']),random.randint(100,10000)) 
##            assert timed > 0
##            totaltime += timed
##        except AssertionError:
##            failed += 1
##        else:
##            passed += 1
##
##    print(f"Ran {n} tests in {totaltime:.2f} seconds.")
##    print("Passed {}/{} tests.".format(passed,n))
