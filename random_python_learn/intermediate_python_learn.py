"""

    --- Following this Tutorial - https://www.youtube.com/watch?v=HGOBQPFzWKo ---

"""

"""
    ***** STRING *****
"""

from collections import defaultdict, deque
from collections import OrderedDict
from collections import namedtuple
from collections import Counter
from timeit import default_timer as timer
import math
my_list = ['a'] * int(math.pow(10, 6))


# bad
start = timer()
my_string = ''
for c in my_list:
    my_string += c

end = timer()

# print(my_string)
print(end-start)

# good
start = timer()
my_string = ''.join(my_list)
end = timer()

# print(my_string)
print(end-start)


### FORMATTED String ###
# 3 ways of doing it - % , format method, f string (very powerful and important since python3.6)

# using `%`
var1, var2, var3 = 34, "tim", 3.14
my_string1 = "the variable is %d" % var1
my_string2 = "the variable is %s" % var2
my_string3 = "the variable is %.1f" % var3

print("Using % _operator:", my_string1, my_string2, my_string3)

# using `format method`
var1, var2, var3 = 34, "tim", 3.146
my_string1 = "the variable is {};".format(var1)
my_string2 = "the variable is {} and {};".format(var2, var1)
my_string3 = "the variable is {:.1f}, {} and {};".format(var3, var2, var1)

print("Using Format method: ", my_string1, my_string2, my_string3)

# using `f-string`
var1, var2, var3 = 34, "tim", 3.14
my_string1 = f"the variable is {var1};"
my_string2 = f"the variable is {var2} and {var1};"
my_string3 = f"the variable is {var3:.5f}, {var2} and {(var1 / 3):.3f};"

print("Using F-String: ", my_string1, my_string2, my_string3)


"""
    ***** COLLECTIONS *****

    5 types:
    1. Couter ->
    2. NamedTuples ->
    3. OrderedDict ->
    4. DefaultDict -> 
    5. deque -> 
"""
# Counter

a = "cccccccccbbbbbbaaaa"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(2))  # 2 most common element
# Note -> returns iterables
print(my_counter.elements(), list(my_counter.elements()))

# NamedTuple -> easy way to create light weight object type (like struct)

Point = namedtuple('Point', 'x,y')  # defining light weight class schema
pt = Point(-1, 3)

print(pt, pt.x, pt.y)

# OrderedDict -> like normal dict but it remembers the order of item insertion
# Note - less usage now as since builtin dictionary class dictionary also have this feature since python3.7


ordered_dict = OrderedDict()  # since 3.7 just normal dict {} will also do the same
ordered_dict['b'] = 1
ordered_dict['c'] = 2
ordered_dict['d'] = 3
ordered_dict['a'] = 5

print(ordered_dict)

# DefaultDict -> like normal dict but will have Default Value for missing keys (Avoid Key error)


default_dict = defaultdict(int)
default_dict_list = defaultdict(list)
default_dict_float = defaultdict(float)

print(default_dict['missing_key'])
print(default_dict_list['missing_key'])
print(default_dict_float['missing_key'])

# Deque -> double ended queue (efficient)
d = deque()

d.append(1)
d.append(2)

d.appendleft(-1)
print(d)

d.pop()

d.popleft()
print(d)

d.clear()  # clears all

d.extend([4, 5, 6])
d.extendleft([1, 2, 3])
print(d)

d.rotate(2)  # rotate right
print(d)
d.rotate(-2)  # rotate left
print(d)
