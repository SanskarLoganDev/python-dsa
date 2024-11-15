# Collections
# Python has a builtin module named "collections". This module provides some useful collection data types that we can use. Before using any of these data types we must import collections.

# import collections
# Counter
# Within the collections module there is a data type called a counter. The counter will count every instance of a certain element from any collection data type. We can create and use a new counter object like so:

from collections import Counter

c = Counter("hello")
print(c)

# This will print Counter({'h':1, 'e':1, 'l':2, 'o':1})
# The Counter object is similar to a dictionary. It will store as a key the letter and as the value the frequency of that key in the item it was passed.

# Like dictionaries we can find the values associated with each key by typing the counter name and then the key enclosed in square brackets.


c = Counter("hello")
print(f"Number of times h has occured: {c['h']}")
# This will print 1

# Counter Methods

# The Counter object has some useful methods that can be seen below.

# .most_common(n): This will return the n most common items along with the amount of times they occur.

c = Counter([1,1,1,3,4,5,6,7,7,7])
# Takes the arguments for how many most commons do you want to find
print(c.most_common(1))  # returns [(1, 3)]
print(c.most_common(2)) # returns [(1, 3), (7, 2)]

# .subtract(collection): This will subtract the count of items from the collection passed from the Counter object.

c = Counter([1,1,1,3,4,5,6,7,7])
d = [1,1,3, 4, 4]

c.subtract(d) # does it in c itself, no need to assign it to a variable

print(c)  # prints Counter({1:1, 3:0, 4:-1, 5:1, 6:1, 7:2})

# .update(collection): This will add all of the counts of the collection to the Counter object.


c = Counter([1,1,1,3,4,5,6,7, 7])
d = [1,1,3]

c.update(d)

print(c)  # prints Counter({1:5, 3:2, 4:1, 5:1, 6:1, 7:2})

# .clear(): This will simply clear all of the counts from the Counter object.


c = Counter([1,1,1,3,4,5,6,7, 7])

c.clear()
print(c)  # prints Counter()

# Practice

t = Counter({'a':1, 'a':2, 'a':100, 'a':80, 'b':1, 'b': 20})
print(t) # prints {'a': 80, 'b': 20} the last one of each

t = Counter({'a':1, 'a':1, 'a':1, 'a':1, 'b':2, 'b': 2})
print(t) # prints {'b': 2, 'a': 1} the last one of each
if 'a' in t:
    print(True)
else:
    print(False)

c = Counter(cats=4, dogs=7)
print(c)
print(c['cats'])

c = Counter(a=4, b=2, c=0, d=2)
d = Counter(['a','b','b','c'])

print(c+d)
print(c-d)
print(c & d) # Union (min elements shown in either)
print( c | d) # intersection (max elements shown in either)
 