'''
Using map reduce to count word frequency.
https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html#Example%3A+WordCount+v1.0

The MapReduce framework operates exclusively on <key, value> pairs, that is, the framework views
the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs
as the output of the job, conceivably of different types.

Mapper maps input key/value pairs to a set of intermediate key/value pairs.
- processes one line at a time
- splits the line into tokens separated by whitespaces
- emits a key-value pair of < word, 1>

Combiner (not included) does LOCAL aggregation, after being sorted on the keys.

Reducer reduces a set of intermediate values which share a key to a smaller set of values.
- sums up the values, which are the occurence counts for each key

Input and Output types of a MapReduce job:
(input) <k1, v1> -> map -> <k2, v2> -> combine -> <k2, v2> -> reduce -> <k3, v3> (output)

Example
chunk1: "Google Bye GoodBye Hadoop code"
chunk2: "lintcode code Bye"

Get MapReduce result:
    Bye: 2
    GoodBye: 1
    Google: 1
    Hadoop: 1
    code: 2
    lintcode: 1
'''

class WordCount:
    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Please use 'yield key, value'
        for key in line.split():
            yield key, 1


    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Please use 'yield key, value'
        yield key, sum(values)
