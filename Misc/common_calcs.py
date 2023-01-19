def findAdjacentEl(L: list, element, num=1):  # num: the maximum number of adjacent elements from each side of given element
    element_ind = L.index(element)
    min_ind = max(0, element_ind - num)
    max_ind = min(len(L) - 1, element_ind + num)
    return [L[i] for i in range(min_ind, max_ind + 1) if L[i] != element]
