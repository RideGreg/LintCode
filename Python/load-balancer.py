'''
Implement a load balancer for web servers. It provide the following functionality:
- Add a new server to the cluster => add(server_id).
- Remove a bad server from the cluster => remove(server_id).
- Pick a server in the cluster randomly with equal probability => pick().

Example
At beginning, the cluster is empty => {}.

add(1)
add(2)
add(3)
pick() >> 1         // the return value is random, it can be either 1, 2, or 3.
pick() >> 2
pick() >> 1
pick() >> 3
remove(1)
pick() >> 2
pick() >> 3
pick() >> 3
'''

class LoadBalancer:
    def __init__(self):
        self.ids = set()

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        self.ids.add(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        self.ids.discard(server_id)

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        if not self.ids:
            return None
        import random
        return random.choice(list(self.ids))