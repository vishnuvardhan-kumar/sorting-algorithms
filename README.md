# Sorting Algorithms
A comparison of all deterministic sorting algorithms on a standard data set.<br>

The data set consists of 3 dynamically generated Python3 lists:
+ near.txt : Nearly sorted array
+ random.txt : Random integer array
+ reverse.txt : Nearly sorted array in reverse order


<h4>Performance analysis</h4>

| n=10000        | Bubble Sort | Comb Sort | Cycle Sort | Heap Sort | Insertion Sort | Merge Sort | Quick Sort | 
|----------------|-------------|-----------|------------|-----------|----------------|------------|------------|
| Visualisation  | ![gif](https://github.com/vishnuvardhan-kumar/sorting-algorithms/raw/master/media/bubble-sort.gif?raw=true) | ![gif](https://github.com/vishnuvardhan-kumar/sorting-algorithms/raw/master/media/cycle-sort.gif?raw=true) |  ![gif](https://github.com/vishnuvardhan-kumar/sorting-algorithms/raw/master/media/comb-sort.gif?raw=true) | ![gif](https://github.com/vishnuvardhan-kumar/sorting-algorithms/raw/master/media/heap-sort.gif?raw=true) | ![gif](https://github.com/vishnuvardhan-kumar/sorting-algorithms/raw/master/media/insertion-sort.gif?raw=true) | ![gif](https://github.com/vishnuvardhan-kumar/sorting-algorithms/raw/master/media/merge-sort.gif?raw=true) |  ![gif](https://github.com/vishnuvardhan-kumar/sorting-algorithms/raw/master/media/quick-sort.gif?raw=true) |
| Best Case Performance  | O(n)      | O(nlog n)     | O(n<sup>2</sup>)     | O(n)     | O(n)         | O(nlog n)      | O(nlog n)      |
| Worst Case Performance  | O(n<sup>2</sup>)     | O(n<sup>2</sup>)     | O(n<sup>2</sup>)      | O(nlog n)     | O(n<sup>2</sup>)         | O(nlog n)      | O(n<sup>2</sup>)      |
| Nearly Sorted  | 16.61s      | 1.72s     | 8.45s      | 0.09s     | 1.20s          | 0.05s      | 0.06s      |
| Randomly Ordered | 19.45s      | 2.03s     | 10.36s     | 0.13s     | 2.46s          | 0.09s      | 0.03s      |
| Reversed Order | 23.91s      | 1.82s     | 9.40s      | 0.08s     | 2.25s          | 0.07s      | 0.04s      |

<h4>Implementation Details:</h4>

+ As the functions are written in Python3, they will, in general, perform worse than the built-in Timsort (sorted).
+ Using proper optimisations and a lower-level language (C++11), Quicksort can hit 0.002s on randomly ordered lists. 

<h4>Benchmarking System:</h4>

+ Intel Core i5 5520U @ 2.6GHz x64 with 8GB memory
+ Python 3.6 + Cython CC

<h4>Credits</h4>

+ common.wikimedia.org
+ rosettacode.org
