# Question 1: Social Network "Mutual Friend Group"
# Analysis (Quick-Find Approach)
#
# There are 6 users on a social media platform.
# The system wants to check whether two users are
# in the same friend group/component instantly.
#
# To achieve this, they decide to use the
# Quick-Find (Eager Approach) algorithm.
#
# Hints:
# Create a class named SocialNetworkQF.
# In the init(self, n) method, set each user's
# id equal to their own index at the beginning.
#

# It should return True or False depending
# on whether the two users are in the same group.
#
# Write an add_friendship(self, p, q) method:
# When p and q become friends, write a loop
# that updates the group ID of everyone in p's group to q's group ID.
#
# Test the system with the following steps:
# Add friendship between (0, 1) and (1, 2).
# Add friendship between (3, 4).
# Are users 0 and 2 connected? Are users 0 and 3 connected?
#
# Question to Think About:
# • • Why do we have to iterate through the entire
# list step by step for every new friendship (O cost)?


class SocialNetworkQF:
    def __init__(self, n):
        self.n = n
        self.users = list(range(n))

    def connected(self, p, q) -> bool:
        if self.users[p] == self.users[q]:
            return True
        return False

    def add_friendship(self, p, q) -> None:
        if self.connected(p, q):
            return

        for i in range(len(self.users)):
            if self.users[i] == self.users[p]:
                self.users[i] = self.users[q]


s = SocialNetworkQF(9)
s.add_friendship(0, 1)
s.add_friendship(1, 2)
s.add_friendship(3, 4)
print(s.connected(0, 2), s.connected(0, 3))
print(s.users)
