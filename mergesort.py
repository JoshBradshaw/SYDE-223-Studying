
def merge(L, R):
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



def bottom_up_mergesort(List):
    section_size = 1
    while section_size < len(List):
        l_idx = 0
        r_idx = l_idx + section_size
        while r_idx < len(List):
            L = List[l_idx:r_idx]
            R = List[r_idx:r_idx+section_size]
            List[l_idx:r_idx+section_size] = merge(L, R)
            l_idx = r_idx
            r_idx = r_idx + section_size
            
        section_size *= 2
    return List

print bottom_up_mergesort([3,1,4, 5, 9, 11, 33, 2223, 2211, 456, 21, 90])