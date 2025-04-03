# set is the collection of the unordered items.
# each element in the set must be unique & immutable.
#  it ignore the duplicate elements from the set.


collection = {1,2,3,3,3,3,4,5}
print(collection)
print(type(collection))
print(len(collection))

# creating empty set
collection = set()
print(type(collection))

# methods of set
# 1) set.add(element)  = add an element
# 2) set.remove(element) = remove the element
# 3) set.clear()  == empties the set
# 4) set.pop() == remove a random value

collection = set()
collection.add(2)
collection.add(4)
collection.add(8)
collection.add((1,2,3,4))
collection.remove(4)
collection.clear()
collection.pop()