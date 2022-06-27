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

ar = search.GPSProblem('A', 'R'
                       , search.romania)

mf = search.GPSProblem('M', 'F'
                       , search.romania)

'''print("---------- FROM ARAD TO RIMINICU VILCEA ----------")
print("BFS search: " + str(search.breadth_first_graph_search(ar).path()))
print("DFS search: " + str(search.depth_first_graph_search(ar).path()))
print("Branch and Bound search: " + str(search.branch_and_bound_graph_search(ar).path()))
print("Branch and Bound search sub: " + str(search.ryasub_graph_search(ar).path()))

print("---------- FROM ARAD TO BUCHAREST ----------")
print("BFS search: " + str(search.breadth_first_graph_search(ab).path()))
print("DFS search: " + str(search.depth_first_graph_search(ab).path()))
print("Branch and Bound search: " + str(search.branch_and_bound_graph_search(ab).path()))
print("Branch and Bound sub search: " + str(search.ryasub_graph_search(ab).path()))

print("---------- FROM ARAD TO CRAIOVA ----------")
print("BFS search: " + str(search.breadth_first_graph_search(ac).path()))
print("DFS search: " + str(search.depth_first_graph_search(ac).path()))
print("Branch and Bound search: " + str(search.branch_and_bound_graph_search(ac).path()))
print("Branch and Bound sub search: " + str(search.ryasub_graph_search(ac).path()))

print("---------- FROM ARAD TO URZICENI ----------")
print("BFS search: " + str(search.breadth_first_graph_search(au).path()))
print("DFS search: " + str(search.depth_first_graph_search(au).path()))
print("Branch and Bound search: " + str(search.branch_and_bound_graph_search(au).path()))
print("Branch and Bound sub search: " + str(search.ryasub_graph_search(au).path()))

print("---------- FROM ARAD TO PITESTI ----------")
print("BFS search: " + str(search.breadth_first_graph_search(ap).path()))
print("DFS search: " + str(search.depth_first_graph_search(ap).path()))
print("Branch and Bound search: " + str(search.branch_and_bound_graph_search(ap).path()))
print("Branch and Bound sub search: " + str(search.ryasub_graph_search(ap).path()))'''

print("---------- FROM MEHAVIA TO FAGARAS ----------")
print("BFS search: " + str(search.breadth_first_graph_search(mf).path()))
print("DFS search: " + str(search.depth_first_graph_search(mf).path()))
print("Branch and Bound search: " + str(search.branch_and_bound_graph_search(mf).path()))
print("Branch and Bound sub search: " + str(search.ryasub_graph_search(mf).path()))


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
