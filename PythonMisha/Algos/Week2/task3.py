# Question 3: Preventing Tall Trees
# (Weighted Quick-Union)
#
# In the standard Quick-Union algorithm,
# if connections are made in order (such as 0-1, 1-2, 2-3...),
# the tree grows like a single line and the find_root
# operation becomes slow (O).
#
# To prevent this, apply the Weighting rule from the slides:
# Always link the smaller tree to the root of the larger tree!
#
# Hints:
#
# Create a class named WeightedQU.
#
# Along with the parent array, add a
# size array that keeps track of the number of nodes in each tree.
#
# In the union(p, q) method, after finding the roots of both elements:
#
# If size[root_p] < size[root_q], link the
# root of p to q and increase the size of q: size[root_q] += size[root_p].
#
# Otherwise, link the root of q to p and
# increase the size of p: size[root_p] += size[root_q].
#
# Observe how this optimization keeps the tree
# depth at a maximum of O(log n) and keeps the find operation fast.
