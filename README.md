# Graph Traversal Algorithm (DFS and BFS) in Python

This program implements graph traversal algorithms - Depth-First Search (DFS) and Breadth-First Search (BFS) - in Python. It showcases the ability to traverse a graph and visit each node efficiently using these algorithms.

## How to Use the Program

1. Clone the repository or download the `graph_traversal.py` file.
2. Make sure you have Python installed on your machine.
3. Open the terminal or command prompt.
4. Navigate to the directory where `graph_traversal.py` is located.
5. Run the following command to execute the program:

    ```shell
    python graph_traversal.py
    ```

6. The program will display the traversal order for both DFS and BFS.

## Implementation Details

The program is written in Python and uses the following techniques:

- Data Structure: The program utilizes defaultdict from the collections module to represent the graph as an adjacency list, simplifying the process of adding neighbors to each node.

- Breadth-First Search (BFS): The BFS algorithm is implemented using a list as a queue, simulating a First-In-First-Out (FIFO) order for visiting nodes. The algorithm explores all neighbors at the same depth before moving to the next depth level.

- Depth-First Search (DFS): The DFS algorithm is implemented using a list as a stack, simulating a Last-In-First-Out (LIFO) order for visiting nodes. The algorithm explores a path as far as possible before backtracking.

- Test Case: The program includes a test case with a sample graph for demonstration purposes. Feel free to modify the graph or add your own test cases to explore different scenarios.

The program provides detailed output, including the nodes being visited and neighbors being added to the stack or queue, showcasing the traversal process and the order in which nodes are explored.

Feel free to explore and modify the code to further demonstrate your Python programming skills and experiment with different graphs and traversal algorithms.

