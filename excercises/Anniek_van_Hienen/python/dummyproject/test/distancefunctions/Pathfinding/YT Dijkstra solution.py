
import heapq

n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
source = 0

class Solution:
    def dijkstra(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        adjacent = {}
        for i in range(n):
                adjacent[i] = []

        for src, destination, weight in edges:
                adjacent[src].append([destination, weight])

        shortest = {} # map a vertex to distance of smallest path

        minHeap = [[0, source]]
        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in shortest:
                continue
            shortest[node1] = weight1

            for node2, weight2 in adjacent[node1]:
                if node2 not in shortest:
                    heapq.heappush(minHeap, [weight1 + weight2, node2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest

# Test the implementation
solution = Solution()
result = solution.dijkstra(n, edges, source)
print(result)

