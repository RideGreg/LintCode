'''
Geohash is a hash function that convert a location coordinate pair (latitude, longitude) into a base32 string.

Example
Given lat = 39.92816697, lng = 116.38954991 and precision = 12 which indicate how long the hash string
should be. You should return wx4g0s8q3jf9.
'''

class GeoHash:
    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        def getBits(coord, l, r, N):
            if N <= 0: return ''
            m = (l+r) / 2.0
            if coord <= m:
                return '0' + getBits(coord, l, m, N-1)
            else:
                return '1' + getBits(coord, m, r, N - 1)

        latN, lngN = precision * 5 / 2, (precision * 5 +1) / 2
        latBits = getBits(latitude, -90, 90, latN)
        lngBits = getBits(longitude, -180, 180, lngN)
        bits = [i + j for i, j in zip(lngBits, latBits)]
        bits = ''.join(bits)

        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        ans = []
        for i in xrange(0, precision * 5, 5):
            index = int(bits[i:i+5], 2)
            ans.append(_base32[index])
        return ''.join(ans)

print GeoHash().encode(39.92816697, 116.38954991, 12) # wx4g0s8q3jf9


