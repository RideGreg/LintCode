'''
Implement a simple twitter. Support the following method:

1 postTweet(user_id, tweet_text). Post a tweet.
2 getTimeline(user_id). Get the given user's most recently 10 tweets posted by himself, order by timestamp from most recent to least recent.
3 getNewsFeed(user_id). Get the given user's most recently 10 tweets in his news feed (posted by his friends and himself). Order by timestamp from most recent to least recent.
4 follow(from_user_id, to_user_id). from_user_id followed to_user_id.
5 unfollow(from_user_id, to_user_id). from_user_id unfollowed to to_user_id.

Example:
postTweet(1, "LintCode is Good!!!") >> 1
getNewsFeed(1) >> [1]
getTimeline(1) >> [1]
follow(2, 1)
getNewsFeed(2) >> [1]
unfollow(2, 1)
getNewsFeed(2) >> []

NOTE: following relationship uses set data structure!!

Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

import collections, heapq

class MiniTwitter:
    
    def __init__(self):
        self.msg = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        self.time = 0

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        self.time += 1
        tweet = Tweet.create(user_id, tweet_text)
        self.msg[user_id].append((self.time, tweet))
        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        ans, maxHeap = [], []
        for u in self.following[user_id]:
            if self.msg[u]:
                heapq.heappush(maxHeap, [-self.msg[u][-1][0], u, -1])
        if self.msg[user_id]:
            heapq.heappush(maxHeap, [-self.msg[user_id][-1][0], user_id, -1])
            
        while maxHeap and len(ans) < 10:
            tm, uid, pos = heapq.heappop(maxHeap)
            ans.append(self.msg[uid][pos][1])
            if abs(pos) < len(self.msg[uid]):
                pos -= 1
                heapq.heappush(maxHeap, [-self.msg[uid][pos][0], uid, pos])
        return ans

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        return map(lambda x:x[1], self.msg[user_id][-10:][::-1])
        ''' or
        ans = []
        for time, tweet in reversed(self.msg[user_id]):
            if len(ans) >= 10: break
            ans.append(tweet)
        return ans
        '''

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        if from_user_id != to_user_id:
            self.following[from_user_id].add(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        self.following[from_user_id].discard(to_user_id)
