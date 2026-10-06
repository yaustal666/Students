# Question 2: Office Computer Network
# Connection Line (Quick-Union / Lazy Approach)
#
# You are building a network management system to
# track whether computers in an office are connected
# to each other with cables.
# You will use the Quick-Union (Lazy Approach) algorithm.
# In this system, each computer points to its own parent computer.
#
# Hints:
# Define a class named NetworkQU. At the beginning,
# each computer is its own parent (parent[i] = i).
#
# Write a find_root(self, i) method: Follow the parent
# pointers (while i != parent[i]) until you reach the
# root computer of the tree.
#
# Write a connect_cable(self, p, q) method: Find the
# root of computer p and the root of computer q, and
# connect the root of p to the root of q (parent[root_p] = root_q).
#
# Write an is_connected(self, p, q) method: Check whether
# computer p and computer q can transfer data by comparing
# their roots (find_root(p) == find_root(q)).
#
# Test the system with the following steps:
#
# Connect computers (0, 1) and (1, 2).
# Can computer 0 and computer 2 communicate with each other?
# Can computer 0 and computer 4 communicate with each other?
#
# Question to Think About:
# Why does the connect_cable operation only change a
# single value in the array, while Quick-Find had to
# update many values?


class NetworkQU:
    def __init__(self, n):
        self.n = n
        self.computers = list(range(n))

    def find_root(self, p):
        if self.computers[p] == p:
            return p

        while self.computers[p] != p:
            p = self.computers[p]

        return p

    def connect_cable(self, p, q) -> None:
        root_p = self.find_root(p)
        root_q = self.find_root(q)
        self.computers[root_p] = root_q

    def is_connected(self, p, q) -> bool:
        if self.find_root(p) == self.find_root(q):
            return True
        return False


test = NetworkQU(9)
test.connect_cable(0, 1)
test.connect_cable(1, 2)
print(test.is_connected(0, 2), test.is_connected(0, 4))
print(test.computers)
