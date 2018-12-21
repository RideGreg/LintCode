# Time: O(nlogk)
# Space: O(k)

# Given a List, each element in the list represents a student's StudentId and GPA.
# Return the StudentId and GPA of the top K GPA,in the original order.

# 1.if k > the number of students, Return all student information.
# 2.Both StudentId and GPA are String.
# 3.The GPA between two students is different

# Dobule Heap

class Solution(object):
    def topKgpa(self, list, k):
        if len(list) <= k: return list

        import heapq
        h = []
        for i in range(len(list)):
            heapq.heappush(h, (list[i][1], list[i][0], i))
            if len(h) > k:
                heapq.heappop(h)

        h2 = []
        for i in range(len(h)):
            heapq.heappush(h2, (h[i][2], h[i][1], h[i][0]))

        ans = []
        for _ in range(k):
            item = heapq.heappop(h2)
            ans.append([item[1], item[2]])
        return ans

        '''
        heapq.heapify(list) # this is pretty much useless, sorting by StudentId
        cutoff = heapq.nlargest(k, list, key=lambda x:x[1])[-1] # bad: original heap order not using this key
        return [i for i in list if i[1]>=cutoff[1]]
        '''

print(Solution().topKgpa([["001","4.53"],["002","4.87"],["003","4.99"]], 2))
# [["002","4.87"],["003","4.99"]]
