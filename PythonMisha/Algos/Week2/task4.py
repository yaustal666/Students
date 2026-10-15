# Question 4: Percolation Problemi
#
#
# A filter material is modeled as a 3 times 3 grid.
#
# Some pores in the grid are blocked, while others are open.
#
# For a liquid poured from the top to percolate to the bottom,
# there must be an uninterrupted path of open pores from any
# open pore in the top row to any open pore in the bottom row.
#
# Number the 9 cells in the 3 times 3 grid from 0 to 8
# using the formula: index = row * 3 + col.
#
# Add two extra virtual nodes as recommended in
# the slides: "Virtual Top" and "Virtual Bottom".
#
# Rules:
# Connect the open pores in the first row (0, 1, 2)
# directly to "Virtual Top" (index 9).

# Connect the open pores in the last row (6, 7, 8)
# directly to "Virtual Bottom" (index 10).

# Connect adjacent (up, down, left, right) open
# pores with each other using the union operation.
