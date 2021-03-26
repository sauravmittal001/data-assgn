# Assignment 4 Report
### Brief Overview of approach used for Stage D to B+:
- First we represented the 7 LEDs of a single digit dispaly in an array of array. To get the function the number of different bits between different digits were counted. 
- For calculating cost of a given cycle, we defined a function, which cumulatively sums up all cost involved in jumping through the sequence. 
- A dictionary was also maintained simultaneously for all possible permutations, storing the number of sequences as the value for a particular cost as key.
- This dictionary can be used to find least and worst cost of iterating over all digits exactly once in some particular order
- The graph to be plotted used the csv file generated, as it stored the mapping from some cost to number of sequences having that cost

### Explanation for Additional Letter Grade
##### _Why is the problem very difficult for hexadecimal display_

The fundamental problem in solving these kind of problem is that to find minimum/maximum cost is actually a NP problem, ie., there cannot be an algorithm which guarantees to solve it in a polynomial time. This makes the time taken to execute the code blowing up after a certain limit. We have used an O(n!) complexity approach here and still it takes suffieciently long to run completely. This is when we are working with numbers of 10! order. Using the same technique for a hexadecimal system of digit represenattion will make the number of nodes and hence the tital number of permutations possible very large to be handled by the compiler. The execution time will be exhausted and the problem cannot be solved at all. Some other approach might be useful which bring down the complexity slightly. But this will also save us only a little farther, and after that this algorithm will burst up and fall short of run time. There has been no found algorithm to solve these sorts of problems in reasonable time bound and hence it is difficult to imagine it in case of alphabets switching, around 26! sequences to be processed. The standard algorithms like DFS, BFS, dijkstra's etc might be improved to work upon covering all nodes kind of problem.

### Files Attached
| Name | Details |
| ------ | ------ |
| main.py | Contains all functions relevant for individual stages with proper comments |
| README.md | Contains basic information about code interpretation |
| cost.csv | Contains cost distribution as asked in Stage B+ |
| Cycles vs cost.xlsx | Contains the table of distribution of cost vs no. of sequences |
|Assignment4_Report.md | Code explained and Additional Grade Stage |


