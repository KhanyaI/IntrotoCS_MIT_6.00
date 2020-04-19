# 6.00 Problem Set 11
#
# ps11.py
#
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
#from graph import Digraph, Edge, Node, WeightedEdge

class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)
    def __hash__(self):
        return self.name.__hash__()

class Edge(object):
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
   def __init__(self, src, dest, totaldistance, outdistance):
       self.src = src
       self.dest = dest
       self.totaldistance = totaldistance
       self.outdistance = outdistance
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def getTotalDistance(self):
    return self.totaldistance
   def getOutDistance(self):
    return self.outdistance


class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       self.nodes = set([])
       self.edges = {}
   def addNode(self, node):
       if node in self.nodes:
           raise ValueError('Duplicate node')
       else:
           self.nodes.add(node)
           self.edges[node] = []
   def addEdge(self, edge):
       src = edge.getSource()
       dest = edge.getDestination()
       if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
       self.edges[src].append(dest,edge.getTotalDistance(),edge.getOutDistance())
   def childrenOf(self, node):
       return self.edges[node]
   def hasNode(self, node):
       return node in self.nodes
   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]


#
# Problem 2: Building up the Campus Map
#
# Write a couple of sentences describing how you will model the
# problem as a graph)
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    #TODO
    print ("Loading map from file...")
    frompoint = []
    trydigraph = Digraph()
    
    with open(mapFilename) as f:
        read_file = f.readlines()
    
    for line in read_file:
        data = line.split(" ")
        src = Node(data[0])
        #print(src)
        dest = Node(data[1])
        #print(dest)
        totaldistance = int(data[2])
        outdoordistance= int(data[3])

        try:
            trydigraph.addNode(src)
        except TypeError:
            pass
        try:
            trydigraph.addNode(dest)
        except TypeError:
            pass


        trydigraph.addEdge(WeightedEdge(src,dest,totaldistance,outdoordistance))

        #graph.addEdge(edge)

    print(trydigraph)



#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and the constraints
#

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    finalpath = []
    visited = []

    if not (digraph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    if start == end:
        return path
    shortest = None
    totaldistance = 0
    totaloutdoor = 0
    #itireate through children

    for child in digraph.childrenOf(start):
        if (child not in visited): 
            visited = visited + [child.getName()]

            for i in range(len(visited)):
                totaldistance += int(digraph.getEdge(visited[k], visited[k+1])[1])
                totaloutdoor += int(digraph.getEdge(visited[k], visited[k+1])[2])  

            if totaldistance <= maxTotalDist and totaloutdoor <= maxDistOutdoors:  
                if child[0].getName() == end: 
                    finalpath.append((visited, totaldistance, totaloutdoor)) 
                else: 
                    bruteForceSearch(digraph, child.getName(), end, maxTotalDist, maxDistOutdoors)
    return finalpath


if __name__ == '__main__':
    datafile = load_map('/Users/ifrahkhanyaree/Desktop/HomeDS/Code/MIT_guttag/todo/ps11-fastestwaymit_graphtheroy/ps11/mit_map.txt')
    bruteForceSearch(datafile,32,56,1000000,0)

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    pass

# Uncomment below when ready to test
##if __name__ == '__main__':
##    # Test cases
##    digraph = load_map("mit_map.txt")
##
##    LARGE_DIST = 1000000
##
##    # Test case 1
##    print "---------------"
##    print "Test case 1:"
##    print "Find the shortest-path from Building 32 to 56"
##    expectedPath1 = ['32', '56']
##    brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
##    dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
##    print "Expected: ", expectedPath1
##    print "Brute-force: ", brutePath1
##    print "DFS: ", dfsPath1
##
##    # Test case 2
##    print "---------------"
##    print "Test case 2:"
##    print "Find the shortest-path from Building 32 to 56 without going outdoors"
##    expectedPath2 = ['32', '36', '26', '16', '56']
##    brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
##    dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
##    print "Expected: ", expectedPath2
##    print "Brute-force: ", brutePath2
##    print "DFS: ", dfsPath2
##
##    # Test case 3
##    print "---------------"
##    print "Test case 3:"
##    print "Find the shortest-path from Building 2 to 9"
##    expectedPath3 = ['2', '3', '7', '9']
##    brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
##    dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
##    print "Expected: ", expectedPath3
##    print "Brute-force: ", brutePath3
##    print "DFS: ", dfsPath3
##
##    # Test case 4
##    print "---------------"
##    print "Test case 4:"
##    print "Find the shortest-path from Building 2 to 9 without going outdoors"
##    expectedPath4 = ['2', '4', '10', '13', '9']
##    brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
##    dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
##    print "Expected: ", expectedPath4
##    print "Brute-force: ", brutePath4
##    print "DFS: ", dfsPath4
##
##    # Test case 5
##    print "---------------"
##    print "Test case 5:"
##    print "Find the shortest-path from Building 1 to 32"
##    expectedPath5 = ['1', '4', '12', '32']
##    brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
##    dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
##    print "Expected: ", expectedPath5
##    print "Brute-force: ", brutePath5
##    print "DFS: ", dfsPath5
##
##    # Test case 6
##    print "---------------"
##    print "Test case 6:"
##    print "Find the shortest-path from Building 1 to 32 without going outdoors"
##    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
##    brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
##    dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
##    print "Expected: ", expectedPath6
##    print "Brute-force: ", brutePath6
##    print "DFS: ", dfsPath6
##
##    # Test case 7
##    print "---------------"
##    print "Test case 7:"
##    print "Find the shortest-path from Building 8 to 50 without going outdoors"
##    bruteRaisedErr = 'No'
##    dfsRaisedErr = 'No'
##    try:
##        bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
##    except ValueError:
##        bruteRaisedErr = 'Yes'
##    
##    try:
##        directedDFS(digraph, '8', '50', LARGE_DIST, 0)
##    except ValueError:
##        dfsRaisedErr = 'Yes'
##    
##    print "Expected: No such path! Should throw a value error."
##    print "Did brute force search raise an error?", bruteRaisedErr
##    print "Did DFS search raise an error?", dfsRaisedErr
##
##    # Test case 8
##    print "---------------"
##    print "Test case 8:"
##    print "Find the shortest-path from Building 10 to 32 without walking"
##    print "more than 100 meters in total"
##    bruteRaisedErr = 'No'
##    dfsRaisedErr = 'No'
##    try:
##        bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
##    except ValueError:
##        bruteRaisedErr = 'Yes'
##    
##    try:
##        directedDFS(digraph, '10', '32', 100, LARGE_DIST)
##    except ValueError:
##        dfsRaisedErr = 'Yes'
##    
##    print "Expected: No such path! Should throw a value error."
##    print "Did brute force search raise an error?", bruteRaisedErr
##    print "Did DFS search raise an error?", dfsRaisedErr

