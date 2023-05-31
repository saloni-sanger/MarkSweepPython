# Python Project: Simulate Mark-Sweep Algorithm

### Background
I made this project in Languages and Computation with Professor Eric
Larson at Seattle University.

#### Functionality
1. Get input file from command line
2. Process the file. 
    - The first line contains n, the number of heap blocks.
    - The heap blocks will be identified through n-1.
    - Each subsequent line contains an ordered pair in either form:
        - named pointer, heap block
        - heap block, heap block
3. Perform Mark-Sweep.
4. Out which heap blocks are marked and reclaimed/swept.

### Sample I/O    

**Sample Input File**   
10   
p,0   
0,1   
1,7   
r,2   
2,0   
4,1   
4,5   
5,4   
5,9   
s,6   
8,4   
9,8   

**Sample Output**   
Marked nodes: 0 1 2 6 7    
Swept nodes: 3 4 5 8 9    

#### Other   
Comments are present in the code for further technical understanding.