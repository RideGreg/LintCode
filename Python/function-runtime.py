'''
Given a series of descriptions of when the function enters and exits, ask how long each function will run.

Example
Give s=["F1 Enter 10","F2 Enter 18","F2 Exit 19","F1 Exit 20"]，return["F1|10","F2|1"].
'''
class Solution:
    """
    @param a: The Descriptions
    @return: Every functions' runtime
    """

    def getRuntime(self, a):
        import collections
        enter, dur = {}, collections.defaultdict(int)
        for s in a:
            desp = s.split()
            if desp[1] == 'Enter':
                enter[desp[0]] = int(desp[2])
            elif desp[1] == 'Exit':
                dur[desp[0]] += int(desp[2]) - enter[desp[0]]

        ans = []
        for k, v in dur.items():
            ans.append("{}|{}".format(k, v))
        return sorted(ans, key=lambda s: s.split('|')[0])