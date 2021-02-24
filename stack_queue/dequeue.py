# coding=utf-8
# Author: Lishiyao
# CreatTime: 2021/2/24 17 17
# FileName: dequeue 
# Description: Simple introduction of the code

class Dequeue(object):
#队列
    def __init__(self):
        self.__list = []

    def add_front(self,item):
        #从头部添加
        self.__list.insert(0,item)
        pass

    def add_rear(self,item):
        #从尾部添加
        self.__list.append(item)
        pass

    def pop_front(self):
        #从队列头删除一个元素
        return self.__list.pop(0)
        pass

    def pop_rear(self):
        #从尾部删除一个元素
        return self.__list.pop()
        pass

    def is_empty(self):
    #判断一个队列是否为空
        # print(dq.__list)
        return self.__list == []    #注意，这里self.__list is [] 仍然是False

    def size(self):
    #返回队列大小
        return len(self.__list)
        pass

if __name__ == '__main__':
    print("双队列的测试开始")
    dq = Dequeue()
    dq.add_front(1)
    dq.add_rear(2)
    dq.add_rear(3)
    dq.add_rear(4)
    print(dq.is_empty())
    print(dq.pop_rear())
    print(dq.pop_front())
    print(dq.pop_front())
    print(dq.pop_front())
    print(dq.is_empty())
