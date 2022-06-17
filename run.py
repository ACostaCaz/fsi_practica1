# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

ac = search.GPSProblem('A', 'C'
                       , search.romania)

au = search.GPSProblem('A', 'U'
                       , search.romania)

ap = search.GPSProblem('A', 'P'
                       , search.romania)
print("---------- FROM ARAD TO BUCHAREST ----------")
print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_graph_search(ab).path())

print("---------- FROM ARAD TO CRAIOVA ----------")
print(search.breadth_first_graph_search(ac).path())
print(search.depth_first_graph_search(ac).path())
print(search.branch_and_bound_graph_search(ac).path())

print("---------- FROM ARAD TO URZICENI ----------")
print(search.breadth_first_graph_search(au).path())
print(search.depth_first_graph_search(au).path())
print(search.branch_and_bound_graph_search(au).path())

print("---------- FROM ARAD TO PITESTI ----------")
print(search.breadth_first_graph_search(ap).path())
print(search.depth_first_graph_search(ap).path())
print(search.branch_and_bound_graph_search(ap).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
