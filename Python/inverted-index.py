'''
Create an inverted index with given documents. Ensure that data does not include punctuation.

Example
Given a list of documents with id and content. (class Document)
[
  {
    "id": 1,
    "content": "This is the content of document 1 it is very short"
  },
  {
    "id": 2,
    "content": "This is the content of document 2 it is very long bilabial bilabial heheh hahaha ..."
  },
]

Return an inverted index (HashMap with key is the word and value is a list of document ids).
{
   "This": [1, 2],
   "is": [1, 2],
   ...
}
'''

'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''

class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        import collections, re
        ans = collections.defaultdict(list)

        for doc in docs:
            words = re.split(r'\s+|[,;.]\s*', doc.content)
            #words = re.split('\W+', doc.content) #split by all non-words char, bug on word 'self-motivated'
            words = set(words)
            words.discard('')
            for w in words:
                ans[w].append(doc.id)
        return ans
