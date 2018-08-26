'''
Support follow & unfollow, getFollowers, getFollowings.
follow(1, 3)
getFollowers(1) // return [3]
getFollowings(3) // return [1]
follow(2, 3)
getFollowings(3) // return [1,2]
unfollow(1, 3)
getFollowings(3) // return [2]

NOTE: 1. following relationship uses set data structure!!
      2. set.discard is better than set.remove
'''

class FriendshipService:
    
    def __init__(self):
        self.following = collections.defaultdict(set)
        self.follower = collections.defaultdict(set)

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        return sorted(list(self.follower[user_id]))

    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        return sorted(list(self.following[user_id]))

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, to_user_id, from_user_id):
        if to_user_id != from_user_id:
            self.following[from_user_id].add(to_user_id)
            self.follower[to_user_id].add(from_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, to_user_id, from_user_id):
        self.following[from_user_id].discard(to_user_id)
        self.follower[to_user_id].discard(from_user_id)
