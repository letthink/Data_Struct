# coding=utf-8
# Author: Lishiyao
# CreatTime: 2021/2/24 16 47
# FileName: stack 
# Description: Simple introduction of the code

class Stack(object):
    #栈
    def __init__(self):
        self.__list = [] #容器，用顺序表，对应python中的list

    def push(self, item):
        #添加新元素item到栈顶
        self.__list.append(item) #选择在尾部还是头部，可以具体分析，如顺序表选择尾部，链表选择头部（时间复杂度）
        pass

    def pop(self):
    #弹出栈顶元素
        return self.__list.pop()

    def peek(self):
        #返回栈顶元素
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
    #判断栈是否为空
        return self.__list is []
        pass

    def size(self):
#返回栈的元素个数
        return len(self.__list)
        pass

if __name__ == '__main__':
    print("栈的测试开始")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
