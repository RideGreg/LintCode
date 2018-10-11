''' 为一栋大楼设计电梯系统

- 不需要考虑超重的情况
- 该电梯系统目前只有1台电梯, 该楼共有n层
- 每台电梯有三种状态：上升，下降，空闲
- 当电梯往一个方向移动时，在电梯内无法按反向的楼层
- 我们提供了其他几个已经实现好的类，你只需要实现Elevator Class内的部分函数即可。

Example
5           // 电梯一共有5层
ExternalRequest(3, "Down")
ExternalRequest(2, "Up")
openGate()
InternalRequest(1)
closeGate()
openGate()
closeGate()
openGate()
closeGate()
// 注意每行命令之后我们都会调用elevatorStatusDescription 函数，用于测试你是否处于一个正确的状态。
你能看到的正确的内容应该是：

Currently elevator status is : DOWN.
Current level is at: 1.
up stop list looks like: [false, false, false, false, false].
down stop list looks like:  [false, false, true, false, false].
*****************************************

Currently elevator status is : DOWN.
Current level is at: 1.
up stop list looks like: [false, true, false, false, false].
down stop list looks like:  [false, false, true, false, false].
*****************************************

Currently elevator status is : DOWN.
Current level is at: 3.
up stop list looks like: [false, true, false, false, false].
down stop list looks like:  [false, false, false, false, false].
*****************************************

Currently elevator status is : DOWN.
Current level is at: 3.
up stop list looks like: [false, true, false, false, false].
down stop list looks like:  [true, false, false, false, false].
*****************************************

Currently elevator status is : DOWN.
Current level is at: 3.
up stop list looks like: [false, true, false, false, false].
down stop list looks like:  [true, false, false, false, false].
*****************************************

Currently elevator status is : DOWN.
Current level is at: 1.
up stop list looks like: [false, true, false, false, false].
down stop list looks like:  [false, false, false, false, false].
*****************************************

Currently elevator status is : UP.
Current level is at: 1.
up stop list looks like: [false, true, false, false, false].
down stop list looks like:  [false, false, false, false, false].
*****************************************

Currently elevator status is : UP.
Current level is at: 2.
up stop list looks like: [false, false, false, false, false].
down stop list looks like:  [false, false, false, false, false].
*****************************************

Currently elevator status is : IDLE.
Current level is at: 2.
up stop list looks like: [false, false, false, false, false].
down stop list looks like:  [false, false, false, false, false].
*****************************************
'''

class Direction: # used in ExternalRequest class
    UP = 'UP'
    DOWN = 'DOWN'

class Status: # used in Elevator class
    UP = 'UP'
    DOWN = 'DOWN'
    IDLE = 'IDLE'

class Request:
    def __init__(self,l = 0):
        self.level = l
        
    def getLevel(self):
        return self.level

class ExternalRequest(Request):
    def __init__(self,l = 0,d = None):
        Request.__init__(self,l)
        self.direction = d

    def getDirection(self):
        return self.direction

class InternalRequest(Request):
    def __init__(self,l = None):
        Request.__init__(self,l)

class ElevatorButton:
    def __init__(self,level,e):
        self.level = level
        self.elevator = e
        
    def pressButton(self):
        request = InternalRequest(self.level)
        self.elevator.handleInternalRequest(request);

class Elevator:
    def __init__(self, n):
        # Keep them, don't modify.
        self.buttons = []
        self.upStops = []
        self.downStops = []
        for i in xrange(n): # level in Request is 1-based, stop and currLevel are 0-based.
            self.upStops.append(False)
            self.downStops.append(False)
        self.currLevel = 0
        self.status = Status.IDLE

    def insertButton(self,eb):
        self.buttons.append(eb)

    def handleExternalRequest(self,r):
        # Set the stop requested; set Elevator status only when there is no outstanding opposite requests.
        if r.direction == Direction.UP:
            self.upStops[r.level - 1] = True
            if self.noRequests(self.downStops):
                self.status = Status.UP
        else:
            self.downStops[r.level - 1] = True
            if self.noRequests(self.upStops):
                self.status = Status.DOWN
        
    def handleInternalRequest(self,r):
        # Status is set by previous ExternalRequest; now reached the level,
        # only record the level from a valid InternalRequest.
        if self.status == Status.UP and r.level > self.currLevel:
            self.upStops[r.level - 1] = True
        elif self.status == Status.DOWN and r.level < self.currLevel:
            self.downStops[r.level - 1] = True
        
    def openGate(self):
        # Determine which level to stop and open gate
        if self.status == Status.UP:
            # The order of checkLevel: first check all levels above, then rewind to check from the bottom level
            # currLevel/i 0 1 2 3 4
            # 0 -->       0 1 2 3 4
            # 1 -->       1 2 3 4 0
            # 2 -->       2 3 4 0 1
            # 3 -->       3 4 0 1 2
            # 4 -->       4 0 1 2 3
            checkLevels = range(self.currLevel, len(self.upStops)) + range(0, self.currLevel)
            for checkLevel in checkLevels:
            #for i in xrange(len(self.upStops)):
            #    checkLevel = (self.currLevel + i) % len(self.upStops)
                if self.upStops[checkLevel]:
                    self.currLevel = checkLevel
                    self.upStops[checkLevel] = False
                    break

        elif self.status == Status.DOWN:
            # The order of checkLevel: first check all levels underneath, then rewind to check from the top level
            # currLevel/i 0 1 2 3 4
            # 0 -->       0 4 3 2 1
            # 1 -->       1 0 4 3 2
            # 2 -->       2 1 0 4 3
            # 3 -->       3 2 1 0 4
            # 4 -->       4 3 2 1 0
            checkLevels = range(self.currLevel, -1, -1) + range(len(self.downStops) - 1, self.currLevel, -1)
            for checkLevel in checkLevels:
            #for i in xrange(len(self.downStops)):
            #    checkLevel = (self.currLevel + len(self.downStops) - i) % len(self.downStops)
                if self.downStops[checkLevel]:
                    self.currLevel = checkLevel
                    self.downStops[checkLevel] = False
                    break
        
    def closeGate(self):
        # Set Elevator status
        if self.status == Status.IDLE:
            # should be
            # if any(self.upStops):
            #     self.status = Status.UP
            # 	  return
            # if any(self.downStops):
            #     self.status = Status.DOWN
            #     return
            if self.noRequests(self.downStops):
                self.status = Status.UP
                return
            
            if self.noRequests(self.upStops):
                self.status = Status.DOWN
                return

        elif self.status == Status.UP and self.noRequests(self.upStops):
            self.status = Status.DOWN if any(self.downStops) else Status.IDLE
        elif self.status == Status.DOWN and self.noRequests(self.downStops):
            self.status = Status.UP if any(self.upStops) else Status.IDLE

    def noRequests(self, stops):
        return not any(stops)
    
    def elevatorStatusDescription(self):
        description = "Currently elevator status is : " + self.status + \
                      ".\nCurrent level is at: " + str(self.currLevel + 1) + \
                      ".\nup stop list looks like: " + self.toString(self.upStops) + \
                      ".\ndown stop list looks like:  " + self.toString(self.downStops) + \
                      ".\n*****************************************\n"
        return description
        
    @classmethod
    def toString(cls, stops):
        return str(stops).replace("False", "false").replace("True", "true")
