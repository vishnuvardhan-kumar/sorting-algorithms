# Sorting Algorithms
A comparison of all deterministic sorting algorithms on a standard data set.<br>

The data set consists of 3 dynamically generated Python3 lists:
+ near.txt : Nearly sorted array
+ random.txt : Random integer array
+ reverse.txt : Nearly sorted array in reverse order


<h4>Performance analysis</h4>

| n=10000        | Bubble Sort | Comb Sort | Cycle Sort | Heap Sort | Insertion Sort | Merge Sort | Quick Sort | 
|----------------|-------------|-----------|------------|-----------|----------------|------------|------------|
| Visualisation  | 
| Nearly Sorted  | 16.61s      | 1.72s     | 8.45s      | 0.09s     | 1.20s          | 0.05s      | 0.06s      |
| Randomly Order | 19.45s      | 2.03s     | 10.36s     | 0.13s     | 2.46s          | 0.09s      | 0.03s      |
| Reversed Order | 23.91s      | 1.82s     | 9.40s      | 0.08s     | 2.25s          | 0.07s      | 0.04s      |

