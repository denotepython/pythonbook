import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

# Load the ascent array
ascent = scipy.misc.ascent()

# def get_indices(size):
#    arr = np.arange(size)
#    return arr % 4 == 0

# Plot ascent
ascent1 = ascent.copy()
length = range(ascent.shape[0])
width = range(ascent.shape[1])
#xindices = get_indices(ascent.shape[0])

#yindices = get_indices(ascent.shape[1])
ascent1[length[::4], width[::4]] = 0
plt.subplot(211)
plt.imshow(ascent1)

ascent2 = ascent.copy() 
# Between quarter and 3 quarters of the max value
ascent2[(ascent > ascent.max()/4) & (ascent < 3 * ascent.max()/4)] = 0
plt.subplot(212)
plt.imshow(ascent2)


plt.show()
