# SOURCE: https://leetcode.com/problems/course-schedule/


"""
TIME COMPLEXITY: O(N)
We visit each node once and perform O(1) array lookups in the visited and graph arrays.

SPACE COMPLEXITY: O(N)
The size of the visited array we are storing + the implicit size of the call stack in the DFS.

This approach uses the 'black, white, gray' node approach.
"""
def can_finish(num_courses, prerequisites):
	# Create an array to represent the graph (i = node/ course, graph[i] = node's children/ courses that you can take after course i)
	graph = [[] for _ in range(num_courses)]

	# Create array of length num_courses to keep track of if we have visited each node/ course already in the graph traversal
	visited = [0 for _ in range(num_courses)]

	# Populate the graph
	for child_node, ancestor_node in prerequisites:
		graph[ancestor_node].append(child_node)

	for node in range(num_courses):
		if not dfs(graph, visited, node):
			return False

	return True

def dfs(graph, visited, node):
	# -1 = node is currently on the recusion call stack (i.e. we have looped back aroung to an ancestor node) => back edge => loop => cant take the course
	if visited[node] == -1:
		return False

    # 1 = node has been visited and is not currently on the call stack (i.e. a course we already know we can take without any loops)
	if visited[node] == 1:
		return True

	# mark the node as currently on the call stack ("this node is currently being processed")
	visited[node] = -1

	# dfs all the child nodes
	for child_node in graph[node]:
		if not dfs(graph, visited, child_node):
			return False

	# now after there are no loops in the child nodes, its safe to mark the current node as fully processed/ visited
	visited[node] = 1

	return True
