
x=list(range(100))

s=set(range(100))

from shutil import which
import sys
print(sys.getsizeof(x))
print(sys.getsizeof(s))

# Which of the two is more memory efficient? Why?
# The set is more memory efficient because it only stores unique elements, whereas the list stores all elements including duplicates.


