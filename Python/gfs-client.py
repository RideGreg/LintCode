'''
Implement a simple client for GFS (Google File System, a distributed file system), it provides the following methods:
1 read(filename). Read the file with given filename from GFS.
2 write(filename, content). Write a file with given filename & content to GFS.

There are two private methods that already implemented in the base class:
1 readChunk(filename, chunkIndex). Read a chunk from GFS.
2 writeChunk(filename, chunkIndex, chunkData). Write a chunk to GFS.

To simplify this question, we can assume that the chunk size is chunkSize bytes. (In a real world system, it is 64M).
The GFS Client's job is splitting a file into multiple chunks (if need) and save to the remote GFS server. chunkSize
will be given in the constructor. You need to call these two private methods to implement read & write methods.

Example:
GFSClient(5)
read("a.txt") >> null
write("a.txt", "World")
>> You don't need to return anything, but you need to call writeChunk("a.txt", 0, "World") to write a 5 bytes chunk to GFS.
read("a.txt") >> "World"
write("b.txt", "111112222233")
>> You need to save "11111" at chink 0, "22222" at chunk 1, "33" at chunk 2.
write("b.txt", "aaaaabbbbb")
read("b.txt") >> "aaaaabbbbb"
'''

'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''

class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        BaseGFSClient.__init__(self)
        self.chunkSize = chunkSize
        self.chunkNum = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        if filename not in self.chunkNum:
            return None
        ans = [self.readChunk(filename, i) for i in xrange(self.chunkNum[filename])]
        return ''.join(ans)

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        cnts = (len(content)-1)/self.chunkSize + 1
        self.chunkNum[filename] = cnts

        for i in xrange(cnts):
            self.writeChunk(filename, i, content[i*self.chunkSize:(i+1)*self.chunkSize])