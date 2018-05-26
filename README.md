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
The graph must be connected to reach every node 

# Data structures

Common mostly used data structure to represent a graph are:

* [adjacency matrix](https://it.wikipedia.org/wiki/Matrice_delle_adiacenze)
* [adjacency list](https://it.wikipedia.org/wiki/Lista_di_adiacenza)

In terms of **memory ocupation** the first (a.m.) is preferible when the most of the nodes are connected each other, in other terms when the number of links are big. Otherwise, the second (a.l.) is used when the graph is sparse.

In term of **elaboration time** a.l. have a O(V + E) complexity otherwise a.m. O(V*V). 

With :

1. `V = n. of nodes`
2. `E = n of links`

So even in this case, a.m. is preferible when E is very big and it is important have a costant responding time at the question "Does exist a link from A to B?".

For our problem we have preferred adjacency list because even in a big house (an hotel??) is unlikely that the rooms (V) are dense connected to each other and so E ~ V. So our assumptions are V=E and in term of elaboration time O(V+V) < O(V*V).
For the same reason even for memory occupation consideration adjacency lists could be preferred, but we do not think the dimension of our mjson map could be a problem.


# Implementation

# Usage

### Help

```
docker run -v $(pwd):/mnt -w /mnt mytest 
usage: main.py [-h] [-f FILENAME] [-i ROOT] [-o OBJECTS [OBJECTS ...]]

find a route from a root!

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME           your map (json format)
  -i ROOT               your root room id
  -o OBJECTS [OBJECTS ...]

```

### Run

```
docker run --name mytest -v $(pwd):/mnt -w /mnt mytest ./scripts/run.sh -f map.json -i 1 -o Pillow,Knife,"Potted Plant"
```

### Test

```
docker run --name mytest_pytest -v $(pwd):/mnt -w /mnt mytest ./scripts/tests.sh

```

