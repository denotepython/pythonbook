import scipy.misc
import matplotlib.pyplot as plt

# This script demonstrates fancy indexing by setting values
# on the diagonals to 0.

# Load the ascent array
ascent = scipy.misc.ascent()
xmax = ascent.shape[0]
ymax = ascent.shape[1]

# Fancy indexing
# Set values on diagonal to 0
# x 0-xmax
# y 0-ymax
ascent[range(xmax), range(ymax)] = 0

# Set values on other diagonal to 0
# x xmax-0
# y 0-ymax
ascent[range(xmax-1,-1,-1), range(ymax)] = 0

# Plot ascent with diagonal lines set to 0
plt.imshow(ascent)
plt.show()
