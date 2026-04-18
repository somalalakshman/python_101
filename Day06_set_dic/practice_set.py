my_set = {1, 2, 3, 4}
print(my_set)

my_set.add(20)
print(my_set)

my_set.remove(2)
print(my_set)

my_set.discard(3)
print(my_set)

#set methods

# union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)

# intersection

set_a = {1,2,3}
set_b = {2,3,4}

intersection_set = set_a.intersection(set_b)
print(intersection_set)

# Difference

set_a = {1,2,3,4}
set_b = {3,4,5}

difference_set = set_a.difference(set_b)
print(difference_set)


#symmetric difference

set_a = {1,2,3}
set_b = {3,4,5}

sym_diff_set = set_a.symmetric_difference(set_b)
print (sym_diff_set)


#set operations
fruits = {"apple", "banana", "cherry"}
print(fruits)

# adding an element 
fruits.add("orange")
print(fruits)

#removing an element
fruits.remove("banana")
print(fruits)

#removing an element using discard
fruits.discard("grape") # it will not show error if the element is not in the set list
print(fruits)