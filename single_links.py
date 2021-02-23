# coding=utf-8
# Author: Lishiyao
# CreatTime: 2021/2/23 11 04
# FileName: single_links 
# Description: Simple introduction of the code

class Node(object):
    "节点"
    def __init__(self,elem):
        self.elem = elem
        self.next = None


# node = Node(100)

class SingleLinkList(object):
    def __init__(self,node=None):
        # 初始化列表头
        self.__head = None
        self.next = node


#     单链表
    def is_empty(self):
        # 链表是否为空
        return self.__head == None


    def length(self):
        # 链表长度
        cur = self.__head    #确定游标
        count = 0  #记录熟练
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历整个链表
        cur = self.__head
        while cur:
            print(cur.elem,end=" ")
            cur = cur.next
        print("")

    def add(self,item):
        # 链表头部添加元素 "头插法" 注意顺序问题(一旦失去next,链表将会丢失)
        node = Node(item)
        node.next = self.__head #注意在python中,"="是将空间指向问题
        self.__head = node

        pass

    def append(self,item):
        # 链表尾部添加元素 "尾插法"
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node


    def insert(self,pos,item):
        # 链表的指定位置添加元素
        node = Node(item)   #且注意,next区域代表指向下一个空间,即self.__head 是指向了第一个节点而非"self.__head"
        cur = self.__head    #cur本身只是一个游标,需要控制的应该是是指向区域,即next(cur.next),
        if pos < 1:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            for i in range(pos-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
            pass

    def remove(self,item):
        # 删除节点
        cur = self.__head
        while cur:
            if item == cur.elem:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next    #深刻理解next的"双重含义" 两边虽然都是next但是含义不同
                break
            else:
                pre = cur
                cur = cur.next

        pass

    def search(self,item):
        # 查找列表是否存在
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    print("测试开始")
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.add(8)
    print('the travel\'s return: ',ll.travel())
    ll.insert(3,5)
    ll.travel()
    print("length:", ll.length())
    ll.remove(2)
    ll.travel()
    ll.append(2)
    ll.travel()
    print(ll.search(1))
    print(ll.search(9))
    print("length:",ll.length())
