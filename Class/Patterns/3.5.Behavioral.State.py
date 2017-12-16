# -*- coding: utf-8 -*-
#

class NetworkCardState(object):
    """基类"""
    def send(self):
        raise NotImplementedError

    def receive(self):
        raise NotImplementedError

class Online(NetworkCardState):
    """在线"""
    def send(self):
        print "sending Data"

    def receive(self):
        print "receiving Data"

class Offline(NetworkCardState):
    """离线"""
    def send(self):
        print "cannot send...Offline"

    def receive(self):
        print "cannot receive...Offline"

class NetworkCard(object):
    def __init__(self):
        self.online = Online()
        self.offline = Offline()
        # 修改内部属性currentState，默认是离线，直接传入类
        self.currentState = self.offline

    def startConnection(self):
        # 修改状态成在线
        self.currentState = self.online

    def stopConnection(self):
        self.currentState = self.offline

    def send(self):
        # 去掉用这个可变的属性的方法，达到看起来是操作了类的属性的改变
        self.currentState.send()

    def receive(self):
        self.currentState.receive()

def main():
    myNetworkCard = NetworkCard()
    print "without connection:"
    myNetworkCard.send()
    myNetworkCard.receive()
    # without connection:
    # cannot send...Offline
    # cannot receive...Offline


    print "starting connection"
    myNetworkCard.startConnection()
    myNetworkCard.send()
    myNetworkCard.receive()
    # starting connection
    # sending Data
    # receiving Data

if __name__ == '__main__':
    main()

