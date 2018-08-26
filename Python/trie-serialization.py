'''
Serialize and deserialize a trie (prefix tree). You can specify your own serialization algorithm.
 str = serialize(old_trie)
 new_trie = deserialize(str)

Example: <a<b<e<>>c<>d<f<>>>>, denote the following structure:
     root
      /
     a
   / | \
  b  c  d
 /       \
e         f
'''

import collections

class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()

class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    @return a string
    '''
    def serialize(self, root):
        if not root: return ''

        data = ''
        for k, v in root.children.items():
            data += k + self.serialize(v)
        return '<{}>'.format(data)   # even data is empty, still return a <>, otherwise a bug for a Trie only has root 

    '''
    @param data: A string serialized by your serialize method.
    @return the root of a Trie
    '''
    def deserialize(self, data):
        if data is None or len(data) == 0:
            return None

        root = TrieNode()
        current = root
        stack =[]
        for c in data:
            if c == '<':
                stack.append(current)
            elif c == '>':
                stack.pop()
            else:
                current = TrieNode()
                stack[-1].children[c] = current

        return root

root = TrieNode()
root.children['a'] = TrieNode()
root.children['a'].children['b'] = TrieNode()
root.children['a'].children['c'] = TrieNode()
root.children['a'].children['d'] = TrieNode()
root.children['a'].children['b'].children['e'] = TrieNode()
root.children['a'].children['d'].children['f'] = TrieNode()

data = Solution().serialize(root)
print data
new_trie = Solution().deserialize(data)