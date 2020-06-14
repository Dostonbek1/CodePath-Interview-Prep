def sort_list(almost_sorted_list, m):
    min_heap, result = [], []
    for elem in almost_sorted_list[:m]:
        heapq.heappush(min_heap, elem)

    for elem in almost_sorted_list[m:]:
        heapq.heappush(min_heap, elem)
        result.append(heapq.heappop(min_heap))

    for i in range(len(min_heap)):
        result.append(heapq.heappop(min_heap))

    return result
print(sort_list(args[0], args[1]))