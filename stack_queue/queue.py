# coding=utf-8
# Author: Lishiyao
# CreatTime: 2021/2/24 17 06
# FileName: queue 
# Description: Simple introduction of the code

class Queue(object):
#队列
    def __init__(self):
        self.__list = []

    def enqueue(self,item): #根据适用的强度，确定尾部还是头部出或入
    #往队列中添加一个item元素
        self.__list.append(item)
        pass

    def dequeue(self):
        #从队列头删除一个元素
        return self.__list.pop(0)

    def is_empty(self):
    #判断一个队列是否为空
        return self.__list == [] #self.__list == None即使列表为空也是False

    def size(self):
    #返回队列大小
        return len(self.__list)

if __name__ == '__main__':
    print("队列的测试开始")
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.is_empty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
