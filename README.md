# esercizio
find a route from a root

# Problem
Given:
1. a map of connected rooms that have inside them a series of objects
2. a starting room
3. a list of objects to collect

Find:
* a possible path to collect all objects given at point 3 in all rooms, starting as root from room at point 2

# Solution

Our problem can be easily catgorized into a common graph traversal case; 
in particular our solution is a (non performant) implementation of a dfs [(depth first searching)](https://it.wikipedia.org/wiki/Ricerca_in_profondit%C3%A0).
Briefly it consist in two simple steps:

1. visit a node
2. visit (recursively) all connected nodes (that have not been visited yet) to the one at point 1 

# Limitations
The graph must be connected to react every node 

# Data structure


