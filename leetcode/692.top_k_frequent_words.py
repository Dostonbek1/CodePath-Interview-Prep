'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up:

    Try to solve it in O(n log k) time and O(n) extra space.
'''

import heapq
import collections

class Solution:
    def topKFrequent(self, words, k):
        # 1. generate word count hash table
        # 2. turn the hash table into sortable list
        # 3. heapify the list
        # 4. pop top k items from the heap
        word_count = self.calc_count(words)
        word_count_pairs = []
        for word, count in word_count.items():
            word_count_pairs.append((-count, word))
        heapq.heapify(word_count_pairs)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(word_count_pairs)[1])
        return result        
    
    def calc_count(self, words):
        result = collections.defaultdict(int)
        for word in words:
            result[word] += 1
        return result


# Python 2 solution
class Solution2(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]