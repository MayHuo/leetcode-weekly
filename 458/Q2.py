# An undirected connected graph with n nodes
# Array of edges where edge[i] = [u, v, wi]
# You are allowd to remove any number of edges from graph such that the resulting graph has at most k connected components
# The cost of a component is defined as the maximum edge weight in that component. The cost is 0 if a component has no edges.
# Return the minimum possible value of the maximum cost among all components after such removal.

# greedy algorithm
# Each time we remove the largest weight edge in the graph
# Then check the resulting graph has at most k connected components
# joinset?

from typing import List
import heapq

class DisJoinSet:
    def __init__(self, n, edges):
        self._edges = edges
        self.nodes = [i for i in range(n)]
        self.size = [1] * n
        self.parents = [i for i in range(n)]
        self.removed = []
        
    @property
    def disjoint_sets(self):
        return len(set(self.parents))
        
    def find_parent(self, x):
        if x == self.parents[x]:
            return x
        return self.find_parent(self.parents[x])
    
    def union(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)
        if parent_x != parent_y:
            size_x = self.size[parent_x]
            size_y = self.size[parent_y]
            if size_x >= size_y:
                self.parents[parent_y] = parent_x
                self.size[parent_x] += self.size[parent_y]
            else:
                self.parents[parent_x] = parent_y
                self.size[parent_y] += self.size[parent_x]
    
    def remove(self, edge):
        self.removed.append(edge)
        for i in range(len(self.size)):
            self.size[i] = 1
            self.parents[i] = i
        for edge in self._edges:
            if edge in self.removed:
                continue
            _x, _y, _ = edge
            self.union(_x, _y)
            
        

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        disjoints = DisJoinSet(n, edges)
        heap = []
        for edge in edges:
            x, y, w = edge
            for node in (x, y):
                if node not in disjoints.nodes:
                    disjoints.nodes.append(node)
                    disjoints.size.append(1)
                    disjoints.parents.append(node)
                disjoints.union(x, y)
            heapq.heappush(heap, (-w, edge))
        while disjoints.disjoint_sets <= k:
            max_weight_edge = heapq.heappop(heap)
            _, edge = max_weight_edge
            print("---------break", edge)
            print("******", disjoints.disjoint_sets, disjoints.parents)
            # break x-y
            disjoints.remove(edge)
        min_costs = 0
        if heap:
            min_costs = heap[0][-1][-1]
        print(disjoints.disjoint_sets)
        print(disjoints.parents)
        print(disjoints.size)
        print(heap)
        return min_costs


                
if __name__ == '__main__':
    s = Solution()
    n = 3
    edges = [[0,1,80],[0,2,6],[1,2,46]]
    k = 1
    # n = 4
    # edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5]]
    # k = 1
    # n = 4
    # edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5]]
    # k = 4
    min_costs = s.minCost(n, edges, k)
    print(min_costs)
    

            
    
