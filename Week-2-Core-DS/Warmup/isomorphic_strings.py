'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
'''

from collections import defaultdict

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return len(set(s)) == len(set(zip(s, t))) == len(set(t))
        # d1, d2 = {}, {}
        # for i, val in enumerate(s):
        #     d1[val] = d1.get(val, []) + [i]
        # for i, val in enumerate(t):
        #     d2[val] = d2.get(val, []) + [i]
        # return sorted(d1.values()) == sorted(d2.values())
        ns = len(s)
        nt = len(t)

        if ns != nt:
            return False

        h = {}
        mt = {}
        for i in range(ns):
            if s[i] not in h:
                if t[i] not in mt:
                    h[s[i]] = t[i]
                    mt[t[i]] = s[i]
                else:
                    return False
            elif h[s[i]] != t[i]:
                return False

        return True