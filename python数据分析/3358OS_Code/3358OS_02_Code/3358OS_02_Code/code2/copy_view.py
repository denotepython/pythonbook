import scipy.misc
import matplotlib.pyplot as plt

ascent = scipy.misc.ascent()
print ascent.shape
acopy = ascent.copy()
aview = ascent.view()

# Plot the ascent array
plt.subplot(221)
plt.imshow(ascent)

#Plot the copy
plt.subplot(222)
plt.imshow(acopy)

#Plot the view
plt.subplot(223)
plt.imshow(aview)

# Plot the view after changes
aview.flat = 0
plt.subplot(224)
plt.imshow(aview)

plt.show()

