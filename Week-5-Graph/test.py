class Solution:

    def findItinerary(self, tickets):
        
        if not tickets:
            return tickets
        
        length = len(tickets) + 1
        # construct a map 
        dct = dict()
        for start, end in tickets:
            if start in dct:
                dct[start].append(end)
            else:
                dct[start] = [end]
        
        for key, value in dct.items():
            value.sort()
        # start from the given edge in the map
        print(dct)
        starting_p = 'JFK'
        ans = ['JFK']
        print(dct)
        while dct:
            # - if multiple: pick the one with a smaller lexical order
            if starting_p in dct and len(dct[starting_p]) > 1:
                print(starting_p)
                print("cur", dct[starting_p])
                ans.append(dct[starting_p][0])
                tmp = dct[starting_p][0]
                dct[starting_p] = dct[starting_p][1:]
                starting_p = tmp
            # - else: just pick the one
            elif starting_p in dct and len(dct[starting_p]) == 1:
                ans.append(dct[starting_p][0])
                tmp = dct[starting_p][0]
                dct[starting_p] = []
                starting_p = tmp
            if length == len(ans):
                break
            print(starting_p)
            print(ans)
            print(dct)
        
        return ans

input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
test = Solution()
print("Ans: ", test.findItinerary(input))