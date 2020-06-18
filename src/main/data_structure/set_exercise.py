"""
{} - this is an empty dict, but
{0, 1} - this is a set; 0, 1 are elements
set() - to define an empty set
"""


# return new set containing common and uncommon items between set_a and set_b
def find_union(set_a, set_b) -> set:
    new_set = set_a
    for item in set_b:
        new_set.add(item)

    return new_set


# return a new set containing common items between set_a & set_b
def find_intersection(set_a, set_b) -> set:
    new_set = set()
    for item in set_a:
        if item in set_b:
            new_set.add(item)

    return new_set


# return True of self.set is disjoint with set_b
def find_disjoint(set_a, set_b) -> bool:
    for item in set_a:
        if item in set_b:
            return False

    return True


# return a new set containing only items of set_a that are not in set_b
def find_differences(set_a, set_b) -> set:
    new_set = set()
    for item in set_a:
        if item not in set_b:
            new_set.add(item)

    return new_set


# return True if set_a is subset of set_b
def find_subsets(set_a, set_b) -> bool:
    for item in set_a:
        if item not in set_b:
            return False

    return True


# return True if set_a is superset of set_b
def find_supersets(set_a, set_b) -> bool:
    for item in set_b:
        if item not in set_a:
            return False

    return True
