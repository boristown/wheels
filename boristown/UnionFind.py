class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
        self.num_sets = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        self.num_sets -= 1
        if self.rank[i] > self.rank[j]:
            self.parent[j] = i
            self.size[i] += self.size[j]
        else:
            self.parent[i] = j
            self.size[j] += self.size[i]
            if self.rank[i] == self.rank[j]:
                self.rank[j] += 1

    def set_size(self, i):
        return self.size[self.find(i)]
    
    def is_same_set(self, i, j):
        return self.find(i) == self.find(j)
    
    def set_count(self):
        return self.num_sets

    def __len__(self):
        return self.num_sets

    def __str__(self):
        return "UnionFind(num_sets = {}, parent = {}, rank = {}, size = {})".format(self.num_sets, self.parent, self.rank, self.size)