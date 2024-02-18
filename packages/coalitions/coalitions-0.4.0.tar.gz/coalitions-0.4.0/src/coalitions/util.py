#!/usr/bin/env python
from collections import defaultdict
from copy import deepcopy
from itertools import chain, combinations, permutations, repeat, product

def tuple_from_dict(dict):
    """Create a tuple of tuples from a dictionary"""
    return tuple(sorted([(elm, dict[elm]) for elm in dict], key=lambda x: x[0]))

def list_from_dict(dict):
    """Create a list of lists from a dictionary"""
    return (sorted([[elm, dict[elm]] for elm in dict], key=lambda x: x[0]))

def dict_from_tuple(atuple):
    """Create a tuple of tuples from a dictionary"""
    return {elm[0]:elm[1] for elm in atuple}

def insert_zeros(counts_tuple, keys):
    """generate a new tuple with zero counts if it not there already"""
    adict = dict_from_tuple(counts_tuple)
    ml = [(key, adict[key]) if key in adict else (key, 0) for key in keys]
    return tuple(ml)

def get_type_count(counts_tuple, type_):
    """Get the count of a particular type from a counts_tuple"""
    for elm in counts_tuple:
        if elm[0] == type_:
            return elm[1]
    return 0

def powerset(iterable):
    """From itertools documentation"""
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def froze_remove_one(iterable):
    """Given an iterable, yield a frozenset with one element removed and the element removed."""
    ml = list(iterable)
    for ii in range(len(ml)):
        l2 = list(ml)
        removed = l2.pop(ii)
        yield frozenset(l2), removed


def zero_to_max(type_counts):
    """Given a counts iterable, generate tuples with zero to max e.g.
      given (('a',2), ('b':3), ('c':4)) will give all tuples with 0-2 of a, -4 of b, and 0-4 of c so
      3 * 4 * 5 = 60 elements"""
    types = [elm[0] for elm in type_counts]
    counts = [elm[1] for elm in type_counts]
    product_args = [range(count + 1) for count in counts]
    for aproduct in product(*product_args):
        aresult = tuple([(types[ii], aproduct[ii]) for ii in range(len(aproduct))])
        yield aresult

def one_less(coal, remove_zeros=False):
    """Given a types count tuple/list, yield a a pair:
        a tuple with one less of each member,
        the element removed"""
    coal = [[elm[0], elm[1]] for elm in coal]
    for ii, elm in enumerate(coal):
        coal2 = deepcopy(coal)
        if elm[1] == 0:
            continue
        if elm[1] == 1 and remove_zeros:
            del coal2[ii]
        else:
            coal2[ii][1] -= 1
        yield (tuple([(elm[0], elm[1]) for elm in coal2]), coal[ii][0])

def distinct_permutations(counts):
    total = sum([counts[key] for key in counts])
    positions = [ii for ii in range(total)]
    positions = set(positions)
    assigned = {}
    for tresult in _assign_distinct(assigned, positions, counts):
        # reformat from dict to sequence
        result = [None] * total
        for key in tresult.keys():
            for pos in tresult[key]:
                result[pos] = key
        yield result

def _assign_distinct(assigned, positions, counts):
    if len(counts):
        key0 = sorted(counts.keys())[0]
        count = counts[key0]
        tcounts = dict(counts)
        del tcounts[key0]
        for combo in combinations(positions, count):
            npositions = set(positions)
            npositions -= set(combo)
            assigned =  dict(assigned)
            assigned[key0] = combo
            for result in _assign_distinct(assigned, npositions, tcounts):
                    yield result
    else:
        yield assigned

def sequence_counts(iterable):
    """Get a dict indicating the number of times each element in the sequence occurs."""
    counts = defaultdict(int)
    for elm in iterable:
        counts[elm] += 1
    return dict(counts)

def sequence_from_types(type_counts):
    """Given a type_counts dictionary return a list with counts of each type."""
    result = []
    for key in type_counts.keys():
        result.extend([key] * type_counts[key])
    return result

def subtype_coalitions(type_counts):
    """Given a dictionary of types and counts, generate tuples with 0 up to n of each type"""
    keys = sorted([key for key in type_counts])
    for n in range(1, len(keys) + 1):
        for combo in combinations(keys, n):
            mytuple = tuple([(pt, type_counts[pt]) for pt in combo])
            for coal in zero_to_max(mytuple):
                yield coal


