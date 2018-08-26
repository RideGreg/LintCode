'''
Implement typeahead. Given a string and a dictionary, return all words that contains the string as a substring.
The dictionary will give at the initialize method and wont be changed.
The method to find all words with given substring would be called multiple times.

NOTE: we should store data in an optimized way during initialization, so search is fast.

Example
Given dictionary = {"Jason Zhang", "James Yu", "Bob Zhang", "Larry Shi"}

search "Zhang", return ["Jason Zhang", "Bob Zhang"].
search "James", return ["James Yu"].
'''

class Typeahead:
    """
    @param: dict: A list of words dictionary
    """
    def __init__(self, dict):
        import collections
        self.subs2word = collections.defaultdict(set)

        for word in dict:
            l = len(word)
            for i in xrange(l):
                for j in xrange(i+1, l+1):
                    self.subs2word[word[i:j]].add(word)

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        return list(self.subs2word[str])