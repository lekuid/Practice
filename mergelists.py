#return a new sorted merged list from K sorted lists, each with size N

def merge(lists):
    merged = []
    for x in lists:
        for y in x:
            merged.append(y)
    return sorted(merged)

print(merge([[1, 2 , 8], [0], [5, 6, 1, 3]]))
