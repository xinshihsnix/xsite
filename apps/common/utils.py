# coding: utf-8


def section_list(list, rows):
    """
    [1,2,3,4,5,6,7,8]  -->  [[1,2,3],[4,5,6],[7,8]]
    """
    section = []
    step = 0
    steps = (len(list)/rows) + 1

    for s in xrange(steps):
        section.append(list[s*rows: (s+1)*rows])
    return section