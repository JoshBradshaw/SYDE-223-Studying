# -*- coding: utf-8 -*- 

"""
http://en.wikipedia.org/wiki/Heapsort

function heapsort(a, count) is
    input: an unordered array a of length count
 
    (: Build the heap in array a so that largest value is at the root :)
    heapify(a, count)

    (: The following loop maintains the invariants that a[0:end] is a heap and every element
     : beyond end is greater than everything before it (so a[end:count] is in sorted order).
     :)
    end ← count - 1
    while end > 0 do
        (: a[0] is the root and largest value. The swap moves it in front of the sorted elements.:)
        swap(a[end], a[0])
        (: the heap size is reduced by one :)
        end ← end - 1
        (: the swap ruined the heap property, so restore it :)
        siftDown(a, 0, end)          
 
(: Put elements of a in heap order, in-place :)
function heapify(a, count) is
    (start is assigned the index in a of the last parent node)
    (the last element in a 0-based array is at index count-1; find the root of that element )
    start ← floor ((count - 2 ) / 2)
    
    while start ≥ 0 do
        (sift down the node at index start to the proper place such that all nodes below
         the start index are in heap order)
        siftDown(a, start, count-1)
        (go to the next parent node)
        start ← start - 1
    (after sifting down the root all nodes/elements are in heap order)

function siftDown(a, start, end) is
    root ← start

    while root * 2 + 1 ≤ end do    (: While the root has at least one child :)
        child ← root * 2 + 1       (: left child :)
        swap ← root                (: keeps track of child to swap with :)

        if a[swap] < a[child]
            swap ← child
        (: if there is a right child and that child is greater :)
        if child+1 ≤ end and a[swap] < a[child+1]
            swap ← child + 1
        if swap ≠ root
            swap(a[root], a[swap])
            root ← swap            (: repeat to continue sifting down the child now :)
        else
            return
"""

def heapsort(a):
    # in place sort
    heapify(a)

    end = len(a) - 1
    while end > 0:
        swap(a, end, 0)
        end = end -1
        siftDown(a, 0, end)
    # by python STD lib convention, in place methods have return value

def heapify(a):
    # create an array based representation of a heap
    # from bottom up
    start = (len(a) - 2) // 2
    while start >= 0:
        siftDown(a, start, len(a)-1)
        start = start - 1

def siftDown(a, start, end):
    root = start

    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap_index = root

        # sift down if child is larger
        if a[swap_index] < a[child]:
            swap_index = child
        # in odd numbered arrays, the last parent can only have one child
        # so we have to check if there is a second child
        # this could be optimized using sentinals
        if child + 1 <= end and a[swap_index] < a[child+1]:
            swap_index = child + 1
        if swap_index != root:
            swap(a, root, swap_index)
            root = swap_index
        else:
            return

def swap(a, s, e):
    a[s], a[e] = a[e], a[s]
    return

a = [0,2,3,4,5,3,2,1,1,2]
heapsort(a)
print a
