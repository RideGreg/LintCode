'''
Cassandra is a NoSQL storage. The structure has two-level keys.
Level 1: raw_key. The same as hash_key or shard_key.
Level 2: column_key.
Level 3: column_value

raw_key is used to hash and can not support range query. let's simplify this to a string.
column_key is sorted and support range query. let's simplify this to integer.
column_value is a string. you can serialize any data into a string and store it in column value.

implement the following methods:
- insert(raw_key, column_key, column_value)
- query(raw_key, column_start, column_end) // return a list of entries

Example:
insert("google", 1, "haha")
query("google", 0, 1) >> [（1, "haha")]
'''

#Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

import collections
class MiniCassandra:
    
    def __init__(self):
        self.ht = collections.defaultdict(dict)

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    def insert(self, raw_key, column_key, column_value):
        self.ht[raw_key][column_key] = column_value

    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, raw_key, column_start, column_end):
        # items() returns a list of k-v tuples for dict, then sort for range query
        dd = sorted(self.ht[raw_key].items())
        return [Column(k, v) for k,v in dd \
            if column_start <= k <= column_end]

obj = MiniCassandra()

obj.insert("Linkedin", 7, "DGFINL")
print obj.query("Apple", 7, 8)

obj.insert("Airbnb", 8, "BOKAQP")
obj.insert("Linkedin", 3, "ODAMGH")
obj.insert("Linkedin", 3, "KELFJN")
obj.insert("Facebook", 2, "HJPQEG")
obj.insert("Airbnb", 0, "OFACBI")
print obj.query("Linkedin", 0, 1)

obj.insert("Facebook", 6, "QHPMCI")
obj.insert("Facebook", 6, "KOPBFL")
obj.insert("Linkedin", 4, "EAKNIF")
print obj.query("Facebook", 0, 1)

obj.insert("Google", 3, "GNQCEK")
obj.insert("Facebook", 5, "NBEJIQ")
obj.insert("Linkedin", 8, "NOMCAD")
obj.insert("Airbnb", 1, "DPHKNG")
print obj.query("Linkedin", 2, 7)
print obj.query("Google", 4, 4)

print obj.query("Facebook", 2, 2)
print obj.query("Facebook", 2, 4)
print obj.query("Linkedin", 3, 7)
print obj.query("Linkedin", 0, 8)
obj.insert("Apple", 3, "PKJNHF")
obj.insert("Facebook", 3, "OMIJPQ")
