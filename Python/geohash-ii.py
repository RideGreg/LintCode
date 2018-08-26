'''
Convert a Geohash string to latitude and longitude.

Example
Given "wx4g0s", return lat = 39.92706299 and lng = 116.39465332.
Return double[2], first double is latitude and second double is longitude.
'''

class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        def getCoord(bits, l, r):
            for c in bits:
                if c == '0':
                    r = (l+r) / 2.0
                else:
                    l = (l+r) / 2.0
            return (l+r) / 2.0

        code2val = {c: i for i, c in enumerate("0123456789bcdefghjkmnpqrstuvwxyz")}
        bits = ''
        for c in geohash:
            bit = ''
            index = code2val[c]
            for _ in xrange(5):
                bit = ('1' if index&1 > 0 else '0') + bit
                index >>= 1
            bits += bit

        ans = [getCoord(bits[1::2], -90, 90), getCoord(bits[::2], -180, 180)]
        return map(lambda x:round(x, 8), ans)

print GeoHash().decode("wx4g0s")


