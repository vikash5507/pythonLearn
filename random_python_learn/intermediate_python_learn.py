"""

    --- Following this Tutorial - https://www.youtube.com/watch?v=HGOBQPFzWKo ---

"""

"""
    ***** STRING *****
"""


from typing import Union
from functools import reduce
from itertools import accumulate, combinations, combinations_with_replacement, count, cycle, repeat, groupby
from itertools import permutations
from itertools import product
from collections import defaultdict, deque
from collections import OrderedDict
from collections import namedtuple
from collections import Counter
import operator
from timeit import default_timer as timer, repeat
import math
from numpy import double
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

"""
    ***** ITERATORS  *****
        IterTools - collections of tools to handle iterators. Iterators are data types that can be used in a For Loop.
        most common iterators - List and offer some advance tools
    
    https://docs.python.org/3/library/itertools.html

    Few Iterator tools:
    1. Product ->
    2. Permutations ->
    3. Combinations ->
    4. Accumulate -> 
    5. GroupBy ->
    6. Infinite Iterators -> 
"""

# Product -> product(A, B) returns the same as: ((x,y) for x in A for y in B)

a = [1, 3]
b = [4]

_prd = product(a, b)
prd = product(a, b, repeat=2)  # repeatable of iterables
print(list(_prd), list(prd))


# Permutations


a = [1, 2, 3]
perm = permutations(a)
perm_custom_len = permutations(a, 2)
print(list(perm))
print(list(perm_custom_len))

# combinations and combinations_with_replacement (repeating with same)

a = [1, 2, 4, 5]
comb = combinations(a, 3)  # note - length mandatory unlike permutations
comb_custom_len = combinations(a, 4)

print(list(comb))
print(list(comb_custom_len))

rep_comb = combinations_with_replacement(a, 3)
print(list(rep_comb))

# Accumulate - returns accumulated sums (e.g cumulative sums, cumulative mul using operators - factorial)

a = [1, 2, 3, 8, 4, 5, 6]
accum = accumulate(a)
mul_accum = accumulate(a, func=operator.mul)  # e.g finding factorial
# return maxm num until now e.g [1, 2, 3, 8, 4, 5, 6] -> [1, 2, 3, 8, 8, 8, 8]
max = accumulate(a, func=max)
print(list(accum), list(mul_accum), list(max))

# GROUP BY - returns iterators for keys and groups
a = [1, 2, 3, 4]


def smaller_than_3(x):
    return x < 3


# group list into 2 groups < 3 and >= 3
group_obj_lamb = groupby(a, key=lambda d: d < 3)
group_obj = groupby(a, key=smaller_than_3)

for key, val in group_obj_lamb:
    print(key, list(val))

for key, val in group_obj:
    print(key, list(val))

persons = [
    {'name': 'Tim', 'age': 25}, {'name': 'Swq', 'age': 25},
    {'name': 'David', 'age': 29}, {'name': 'Koo', 'age': 28},
]

person_group_age = groupby(persons, key=lambda p: p['age'] <= 25)

person_auto_group_age = groupby(
    persons, key=lambda p: p['age'])  # no need to define key conditonal group
for key, val in person_group_age:
    print(key, list(val))

for key, val in person_auto_group_age:
    print(key, list(val))

# INFINITE Iteratoes - count, cycle, repeat

for i in count(10):  # runs infinite counter - break on some condition
    print(i)
    if i == 15:
        break

a = [1, 2, 3]

for idx, n in enumerate(cycle(a)):
    print(n)
    if idx == 3*len(a):
        break

# print(list(repeat(25, 4)))

"""
    ***** LAMBDA Functions  ***** -> use on the fly
        used when you need to use that function only once or pass function as argument to Higher Order Function 
        (e.g builtin method sorted_map, filter, reduce, map)
"""
def add10(x): return x + 10


print(add10(5))


def mult(x, y): return x*y


print(mult(3, 4))

# sorted
point2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
point2D_sorted = sorted(point2D, key=lambda x: x[0]+x[1])

print(point2D_sorted)

# map(func, seq)
a = [1, 2, 3, 4, 5]
double_a = map(lambda x: x*2, a)
double_a_using_list_comprehension = [x*2 for x in a]  # prefer this

print(list(double_a), double_a_using_list_comprehension)

# filter(func, seq)
a = [1, 2, 3, 4, 5, 6, 7, 8]
a_even_filter = filter(lambda x: x % 2 == 0, a)

print(list(a_even_filter))

# reduce(func, seq)
a = [1, 2, 3, 4, 5, 6, 7, 8]
product_a_reduce = reduce(lambda x, y: x*y, a)

print(product_a_reduce)

"""
    ***** EXCEPTION Functions  ***** -> python program terminates on exception or syntax error, so handle properly

Syntax-Error vs Exception : 
Exception - builtin exception and define your own by extending Exception class
        - Raise a exception when you want to force exception to occur
"""

x = 5
if x < 0:
    raise Exception("This is normal exception")

assert x >= 0, "This is another way to raise Assertion Error"
print('Wont run after exception raise')

# handle exception using catch
try:
    x = 5 / 0
except Exception as e:
    print(f"Exception caught! {e}")
    # raise Exception("Not divisible by 0 error") # if not raised program won't stop

print("Exception caught")

# compound exception handling - else(actual valid operation) and finally(used for clean up operation)
try:
    x = 5 / 1
    d = 5 + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("All fine - No exception catched")
finally:
    print("This will always run")

# defining custom Exception


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message: str, value: Union[int, float]) -> None:
        self.message = message
        self.value = value


def test_high_val(x):
    if x > 500:
        raise ValueTooHighError("value higher than 500")
    if x < 1:
        raise ValueTooSmallError("Value too small error", x)


try:
    test_high_val(-567)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

"""
    ***** LOGGING  *****
"""
