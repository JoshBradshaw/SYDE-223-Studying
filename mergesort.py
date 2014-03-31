from itertools import islice, chain

def section(List, size):
    ii = 0
    while ii < len(List):
        yield List[ii:ii+size]
        ii += size

def batch(List, size, section_size):
    sourceiter = iter(section(List, 1))
    while True:
        batchiter = islice(sourceiter, size)
        yield chain([batchiter.next()], batchiter)


def merge(L, R=[]):
    # basic merge that treats lists as stacks
    l_index = 0
    r_index = 0
    merged_list = []
    while l_index < len(L) or r_index < len(R):
        if l_index < len(L) and r_index < len(R):
            if L[l_index] < R[r_index]:
                merged_list.append(L[l_index])
                l_index += 1
            else:
                merged_list.append(R[r_index])
                r_index += 1
        elif l_index < len(L):
            merged_list.append(L[l_index])
            l_index += 1
        else:
            merged_list.append(R[r_index])
            r_index += 1
    return merged_list


def top_down_mergesort(List):
    if len(List) == 1:
        return List
    else:
        mid = len(List) // 2
        left = top_down_mergesort(List[:mid])
        right = top_down_mergesort(List[mid:])
        return merge(left, right)


print bottom_up_mergesort([4, 3, 2, 1, 5, 7, 9])


# for eventual bottom up implementation

def batch(iterable, size):
    sourceiter = iter(iterable)
    while True:
        batchiter = islice(sourceiter, size)
        yield chain([batchiter.next()], batchiter)