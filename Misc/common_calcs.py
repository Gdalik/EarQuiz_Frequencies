def findAdjacentEl(l: list, element, num=1):
    element_ind = l.index(element)
    min_ind = max(0, element_ind - num)
    max_ind = min(len(l)-1, element_ind+num)
    return [l[i] for i in range(min_ind, max_ind + 1) if l[i] != element]
