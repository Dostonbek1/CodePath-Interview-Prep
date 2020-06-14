def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    last_building = []
    res = []

    for curr_building in buildings:
        # if the first building
        if not last_building:
            res.append([curr_building[0], curr_building[2]])
        # if they intersect
        elif last_building[1] >= curr_building[0]:
            if curr_building[2] > last_building[2]:
                res.append([curr_building[0], curr_building[2]])
            elif curr_building[2] < last_building[2]:
                res.append([last_building[1], curr_building[2]])
        # they don't intersect
        else:
            res.append([last_building[1], 0])
            res.append([curr_building[0], curr_building[2]])
        # else:
        #     last_building = []
        #     res.append([last_building[1], 0])
        last_building = curr_building
        # print(last_building)
    res.append([buildings[-1][1], 0])
    return res


import heapq
def getSkyline2(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    v_lines = {l for b in buildings for l in (b[0], b[1])}
    heap, i, res = [], 0, []
    for v1 in sorted(v_lines):
        while i < len(buildings) and buildings[i][0] <= v1:
            heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
            i += 1
        while heap and heap[0][1] <= v1:
            heapq.heappop(heap)
        h = len(heap) and -heap[0][0]
        if not res or res[-1][1] != h:
            res.append((v1, h))
    
    return res