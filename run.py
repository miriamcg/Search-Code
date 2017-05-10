# Search methods
# Authors: Miriam Cabrera & Geraldo Rodrigues

import search

ab = search.GPSProblem('A', 'N', search.romania)

print "Branch and bound"
print search.ramifica_graph_search(ab).path()
print "Branch and bound con subestimacion"
print search.ramifica_conh_graph_search(ab).path()
print "Anchura"
print search.breadth_first_graph_search(ab).path()
print "Profundidad"
print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

