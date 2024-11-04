import numpy as np

n = int(input("enter no. of nodes: "))
adjacency = []
for _ in range(n):
    row = list(map(int, input().split()))
    adjacency.append(row)
d = float(input("enter dumping: "))
i = int(input("enter iterations: "))

matrix = np.array(adjacency)

pagerank = np.ones(n) / n
print(pagerank)

for x in range(i):
    newpagerank = np.zeros(n)
    for y in range(n):
        links = np.where(matrix[:, y] > 0)[0]
        rank = sum(pagerank[z] / np.sum(matrix[z]) for z in links if np.sum(matrix[z]) > 0)
        newpagerank[y] = (1 - d) + d * rank
        pagerank = newpagerank
    pagerank = newpagerank
    print(pagerank)
print(pagerank)
