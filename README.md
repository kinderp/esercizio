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

![alt text](immagini/grafo.png "Mappa")

* datatype.Room is a room :)
* datatype.Route is a hop (room visitted + direction) in a completed route. So a completed route is a list of Route istances
* datatype.Router is the builder of the completed route. It implements dfs.
* datatype.Map is an implementation of a adjacency matrix. Is an array of lists: each elem in the array represent a room and link to a list taht holds all the neighbosr of that room 
* datatype.Node is an element into an adjacency matrix. It is composed by a link to a Room and the direction.
* hashrooms is a simple Dict that holds all the Room istances created from json file. The Node instances (in a Map instance) holds Room pointing to this data memory.
```
├── datatype
│   ├── __init__.py
│   ├── map.py
│   ├── node.py
│   ├── room.py
│   ├── route.py
│   └── router.py
├── Dockerfile
├── immagini
│   └── grafo.png
├── main.py
├── map.json
├── parser
│   ├── __init__.py
│   └── parser.py
├── README.md
├── requirements.txt
├── route
│   ├── __init__.py
│   └── router.py
├── scripts
│   ├── build.sh
│   ├── run.sh
│   └── tests.sh
└── test
    ├── datasource
    │   └── map.json
    ├── datatype
    │   ├── test_map.py
    │   ├── test_node.py
    │   ├── test_room.py
    │   └── test_route.py
    └── parser
        └── test_parser.py

```
The graph in json format is parsed by parser

module.file.class | Description
------------ | -------------
parser.parser.py.Parser | parsing json and creation map and hashroom data structure
Content in the first column | Content in the second column
# Usage
 :exclamation: Please insert below command in the root dir of the project you have cloned

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
### Build

We have nothing to build in python so scripts/build.sh is used to build docker image

```
/scripts/build.sh 
```
### Run

Find your route

```
docker run --name mytest -v $(pwd):/mnt -w /mnt mytest ./scripts/run.sh -f map.json -i 1 -o Pillow,Knife,"Potted Plant"
```

### Test

Some test

```
docker run --name mytest_pytest -v $(pwd):/mnt -w /mnt mytest ./scripts/tests.sh

```

