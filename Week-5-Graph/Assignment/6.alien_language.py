# https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/

def printOrder(words, alpha):
    s = 'abcdefghijklmnopqrstuvwxyz'
    n = len(words)
    graph = Graph(alpha)

    for i in range(n-1):
        word1, word2 = words[i], words[i+1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                graph.addEdge(s.find(word1[j]), s.find(word2[j]))
                break

    ans = graph.topologicalSort()  
    return ans