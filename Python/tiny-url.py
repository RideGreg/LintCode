'''
Given a long url, make it shorter. To make it simpler, let's ignore the domain name.

You should implement two methods:
- longToShort(url). Convert a long url to a short url.
- shortToLong(url). Convert a short url to a long url starts with http://tiny.url/.

You can design any shorten algorithm, the judge only cares about two things:
1. The short key's length should equal to 6 (without domain and slash). And the acceptable characters are [a-zA-Z0-9]. For example: abcD9E. 
2. No two long urls mapping to the same short url and no two short urls mapping to the same long url.

Example:
Given url = http://www.lintcode.com/faq/?id=10, run the following code (or something similar):
short_url = longToShort(url) // may return http://tiny.url/abcD9E
long_url = shortToLong(short_url) // return http://www.lintcode.com/faq/?id=10

The short_url you return should be unique short url and start with http://tiny.url/ and 6 acceptable characters. For example "http://tiny.url/abcD9E" or something else.
The long_url should be http://www.lintcode.com/faq/?id=10 in this case.

Solution:
design a hash funciton to convert long url to a number in [0, 62^6)
which can be expressed in 6-char base62 number; save in key-value pair.
'''


class TinyUrl:
    def __init__(self):
        # Store by id saves space, compared to store 6-char short url.
        # Python int is 24 bytes: n=62**10, n.__sizeof__() ==> 24
        # long is 36 bytes: n=62**11, n.__sizeof__() ==> 36
        # str is 37+#ofChar: 'abcd'.__sizeof__() ==> 41
        self.id2l = {}

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        # 62^6 = 56800235584L, L just labels a larger number than normal 32 or 64 bit interger, no actual difference
        threshold = 62 ** 6
        id = 0
        for c in url:
            id = (id * 256 + ord(c)) % threshold
        while id in self.id2l and self.id2l[id] != url: # hash collision
            id = (id + 1) % threshold

        self.id2l[id] = url

        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            id, key = divmod(id, 62)
            s = ch[key] + s

        s = 'a' * (6 - len(s)) + s
        return "http://tiny.url/" + s

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        id = 0
        for c in url[-6:]: # skip domain name
            if 'a' <= c <= 'z':
                id = id * 62 + (ord(c) - ord('a'))
            elif 'A' <= c <= 'Z':
                id = id * 62 + (ord(c) - ord('A') + 26)
            else:
                id = id * 62 + (ord(c) - ord('0') + 52)

        return self.id2l.get(id)
