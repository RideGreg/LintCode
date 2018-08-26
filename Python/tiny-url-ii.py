'''
As a follow up for Tiny URL, we are going to support custom tiny url, so that user can create their own tiny url.
Custom url may have more than 6 characters in path.

Example:
createCustom("http://www.lintcode.com/", "lccode")
>> http://tiny.url/lccode
createCustom("http://www.lintcode.com/", "lc")
>> error - the long url was shortened
longToShort("http://www.lintcode.com/problem/")
>> http://tiny.url/1Ab38c   // this is just an example, you can have you own 6 characters.
shortToLong("http://tiny.url/lccode")
>> http://www.lintcode.com/
shortToLong("http://tiny.url/1Ab38c")
>> http://www.lintcode.com/problem/
shortToLong("http://tiny.url/1Ab38d")
>> null
'''

class TinyUrl2: # USE THIS
    def __init__(self):
        # store id rather than urlString as much as we can for space optimization.
        # Only custom url mapping stores url string.
        self.id2url = {}
        self.url2id = {}
        self.custom_s2l = {}
        self.custom_l2s = {}

    def idToShortKey(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            id, key = divmod(id, 62)
            s = ch[key] + s

        return 'a' * (6 - len(s)) + s

    def shortKeyToid(self, short_key):
        id = 0
        for c in short_key:
            if 'a' <= c and c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c and c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c and c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52

        return id

    # @param long_url a long url
    # @param a short key
    # @return a short url starts with http://tiny.url/
    def createCustom(self, long_url, short_key):
        # if already store by hash, cannot createCustom
        id = self.shortKeyToid(short_key)
        if id in self.id2url and self.id2url[id] != long_url or \
                long_url in self.url2id and self.url2id[long_url] != id:
            return "error"

        short_url = "http://tiny.url/" + short_key
        if id in self.id2url or long_url in self.url2id:
            return short_url

        if short_url in self.custom_s2l and self.custom_s2l[short_url] != long_url or \
                long_url in self.custom_l2s and self.custom_l2s[long_url] != short_url:
            return "error"

        self.custom_l2s[long_url] = short_url
        self.custom_s2l[short_url] = long_url
        return short_url

    # @param {string} long_url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, long_url):
        # if already in customUrl, just return it
        if long_url in self.custom_l2s:
            return self.custom_l2s[long_url]

        id = 0
        if long_url in self.url2id:
            id = self.url2id[long_url]
        else:
            for a in long_url:
                id = (id * 256 + ord(a)) % 56800235584L
            while id in self.id2url and self.id2url[id] != long_url:
                id = (id + 1) % 56800235584L

        self.id2url[id] = long_url
        self.url2id[long_url] = id
        return "http://tiny.url/" + self.idToShortKey(id)

    # @param {string} short_url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, short_url):
        if short_url in self.custom_s2l:
            return self.custom_s2l[short_url]

        short_key = short_url[len("http://tiny.url/"):] # trim domain name
        return self.id2url.get(self.shortKeyToid(short_key))

class TinyUrl2_ming: # easy to understand: short url to long url mapping, takes more space than storing id.
    def __init__(self):
        self.s2l = {}
        self.l2s = {}

    """
    @param: long_url: a long url
    @param: key: a short key
    """
    def createCustom(self, long_url, key):
        key = 'http://tiny.url/' + key
        if key in self.s2l and self.s2l[key] != long_url or \
                long_url in self.l2s and self.l2s[long_url] != key:
            return 'error'

        self.s2l[key] = long_url
        self.l2s[long_url] = key
        return key

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        if url in self.l2s:
            return self.l2s[url]

        threshold = 62 ** 6
        id = 0
        for c in url:
            id = (id * 256 + ord(c)) % threshold

        s = "http://tiny.url/" + self.idToShortUrl(id)
        while s in self.s2l and self.s2l[s] != url:
            id = (id + 1) % threshold
            s = "http://tiny.url/" + self.idToShortUrl(id)

        self.s2l[s] = url
        self.l2s[url] = s

        return s

    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, short_url):
        return self.s2l.get(short_url)

    def idToShortUrl(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            id, key = divmod(id, 62)
            s = ch[key] + s

        s = 'a' * (6 - len(s)) + s
        return s


obj = TinyUrl2()
print obj.createCustom("http://www.lintcode.com/", "lccode") # http://tiny.url/lccode
print obj.longToShort("http://www.lintcode.com/problem/")
#>> http://tiny.url/dT4Lf1   // this is just an example, you can have you own 6 characters.
print obj.shortToLong("http://tiny.url/lccode") # http://www.lintcode.com/
print obj.shortToLong("http://tiny.url/dT4Lf1") # http://www.lintcode.com/problem/
print obj.shortToLong("http://tiny.url/1Ab38d") # None
print obj.createCustom("http://www.lintcode.com/", "lc") # 'error'
print obj.createCustom("http://www.lintcode.com/en/ladder/", "lccode") #'error'