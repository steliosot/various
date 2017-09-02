def compareLists(a,b):
    removed = [x for x in a if x not in b]
    added = [x for x in b if x not in a]
    overlap = [x for x in a if x in b]
    return [removed,added,overlap]

print(compareLists([1,2,3,4,5],[3,4,5,6,7]))
