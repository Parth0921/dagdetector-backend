# VectorShift Assessment - Parth Rathod

This project serves as the backend for VectorShift Assessment's take home assignment PART-4.

---

I will guide you through the files and my approach to building the backend. I have kept the backend fairly simple only focusing on the crucial aspects.

## Dependencies
- FastAPI

## Run Locally
I recommend creating a virtual env and using it to run the project

1. Extract the code
2. `pip install fastapi uvicorn` 
3. `uvicorn main:app --reload`

---

## Project Structure
There are only 3 files here is a brief description of each of them.

1. main - This serves as the entry point for our backend. It consists of cors configuration, a test route, and pipeline/parse endpoint.

2. models - Consists of the models that are defined for nodes and edges used by /pipeline/parse endpoint for parsing the body of request.

3. dag_helper - A helper file that consists of all the implementation required to calculate if the graph is dag or not. Consists of functions like adjacency list builder, DFS and BFS implementation.

---

### Explanation for PART-4

To detect if the graph formed is **Directed Acyclic Graph** or not, I already knew that the edges were directed, the only thing my algorithm should check was cycle detection in a directed graph. This could be done using DFS and BFS. I explain my implementation using both below!

**1. DFS**- The idea is that a node **should not** get visited **again** on the same path. If this condition ever occurs we are sure that there is a cycle. So we need to keep track of visited nodes and also the path along which we are visiting. Using this we can run a recursive function which explores all such paths on each node because there can be isolated graphs. 

**2. BFS**- Here I have used the concept of topological sort. Since it relies on the principle of DAG. I used Kahn's Algorithm with a slight modification that anytime a node is taken out of queue I increase the counter. In the end I simply compare this counter with total nodes. If they are equal then there was no cycle otherwise the indegree of some node was not set to 0 because a cycle existed at that node.

I am also getting the node name from the algorithms but before sending the response computing a boolean value as requested for the PART-4.

---

# Thank you!