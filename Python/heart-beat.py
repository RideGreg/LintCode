'''
In the Master-Slave architecture, slave server will ping master in every k seconds to tell master server he is alive.
If a master server didn't receive any ping request from a slave server in 2 * k seconds, the master will trigger an alarm
(for example send an email) to administrator.

Let's mock the master server, you need to implement the following three methods:
1 initialize(slaves_ip_list, k). salves_ip_list is a list of slaves' ip addresses. k is define above.
2 ping(timestamp, slave_ip). This method will be called every time master received a ping request from one of the slave server. timestamp is the current timestamp in seconds. slave_ip is the ip address of the slave server who pinged master.
3 getDiedSlaves(timestamp). This method will be called periodically (it's not guaranteed how long between two calls). timestamp is the current timestamp in seconds, and you need to return a list of slaves' ip addresses that died. Return an empty list if no died slaves found.

You can assume that when the master started, the timestamp is 0, and every method will be called with an global increasing timestamp.

Example:
initialize(["10.173.0.2", "10.173.0.3"], 10)
ping(1, "10.173.0.2")
getDiedSlaves(12) >> []
getDiedSlaves(20) >> ["10.173.0.3"]
getDiedSlaves(21) >> ["10.173.0.2", "10.173.0.3"]
ping(22, "10.173.0.2")
ping(23, "10.173.0.3")
getDiedSlaves(24) >> []
getDiedSlaves(42) >> ["10.173.0.2"]
'''

class HeartBeat:
    def __init__(self):
        self.ip2ts = {}

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    def initialize(self, slaves_ip_list, k):
        for ip in slaves_ip_list:
            self.ip2ts[ip] = 0
        self.k = k

    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    def ping(self, timestamp, slave_ip):
        if slave_ip in self.ip2ts:
            self.ip2ts[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    def getDiedSlaves(self, timestamp):
        ans = []
        for ip, ts in self.ip2ts.items():
            if timestamp - 2 * self.k >= ts:
                ans.append(ip)
        return ans