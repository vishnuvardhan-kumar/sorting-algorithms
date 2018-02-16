# Python implementation of Heap Sort
# www.github.com/vishnuvardhan-kumar/sorting-algorithms

# Average performance on the data set
# Near : 0.09 seconds
# Random : 0.13 seconds
# Reverse : 0.08 seconds

from timeit import default_timer as timer

def heap_sort(lst):
  for start in range(int((len(lst)-2)/2), -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break


if __name__ == '__main__':

    time_taken = 0
    x = int(input("Enter number of trials : "))
    
    for n in range(1,x+1):
        with open("data/reverse.txt","r") as fileobj:
            list_to_sort = list(map(int, fileobj.readlines()))
            start = timer()
            w = heap_sort(list_to_sort)
            current = timer()-start
            print(f"Running test {n} : {current:.2f} seconds")
            time_taken += current

    assert sorted(list_to_sort) == w

    time_taken /= x
    print(f"Heap sort: average time = {time_taken:.2f} seconds")       



 
