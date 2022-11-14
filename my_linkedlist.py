"""
Author: Erutaner
Date: 2022.11.14
"""
import random
class Node():
    def __init__(self,data):
        self.next = None
        self.data = data
class Linkedlist():
    def __init__(self):
        self.head = None
    def insert_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node #new_node其实可以看作一个结构体指针
    def insert_end(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        else:
            tmp_p = self.head
            while tmp_p.next != None:
                tmp_p = tmp_p.next
            tmp_p.next = new_node
            return
    def insert_after(self,position,new_data):
        tmp_p = self.head
        i = 0
        while i < position and tmp_p: #运行position次，结束后让tmp_p指向position节点处
            tmp_p = tmp_p.next
            i += 1
        if not tmp_p: #tmp_p为None则进入
            return False
        else:
            new_node = Node(new_data)
            new_node.next = tmp_p.next
            tmp_p.next = new_node
            return True
    def print_Linkedlist(self):
        print("The current Linkedlist:",end=" ")
        tmp_p = self.head
        while tmp_p:
            print(str(tmp_p.data),"->", end=" ")
            tmp_p = tmp_p.next
        print("None")
        print()
    def delete_node(self,position):
        tmp_p = self.head
        if self.head is None:           #这里不加这个的话会直接进入下一个if，出错
            return False
        if position == 0:               #这里不加这个，若position为零，且链表只有一个节点，则会跳过循环进入下一个if, 返回False，无法删掉这个节点
            self.head = self.head.next
            return True
        i = 0
        while i < position - 1 and tmp_p is not None: #正常情况，循环进行Position-1次，找到position的前一个节点
            i += 1
            tmp_p = tmp_p.next
        if tmp_p is None or tmp_p.next is None:
            return False
        else:
            tmp_p.next = tmp_p.next.next
            return True
    def search_node(self,item):
        tmp_p = self.head
        i = 0
        ind_ls = []
        while tmp_p is not None:
            if tmp_p.data == item:
                ind_ls.append(i)
                i += 1
                tmp_p = tmp_p.next
            else:  #不管有没有在当前下标处找到该数据项，都要自增下标
                i += 1
                tmp_p = tmp_p.next
                continue
        return ind_ls
    def ls_len(self):
        i = 0
        tmp_p = self.head
        while tmp_p is not None:
            tmp_p = tmp_p.next
            i += 1
        return i
    def sort_node(self):
        tmp_p = self.head
        cur = Node(None)
        if tmp_p is None:
            return
        elif tmp_p.next is None:
            return
        else:
            l = self.ls_len()
            i = 0
            while i < l-1:
                flag = False
                j = 0
                tmp_p = self.head
                cur = tmp_p.next
                while j < l - i - 1:
                    if tmp_p.data > cur.data:
                        tmp_p.data, cur.data = cur.data, tmp_p.data
                        tmp_p = tmp_p.next
                        cur = cur.next
                        j += 1
                        flag = True
                    else:
                        tmp_p = tmp_p.next
                        cur = cur.next
                        j += 1
                if flag is False:
                    break
                i += 1

def main():
    test_ls = Linkedlist()
    test_ls.insert_end(0)
    test_ls.insert_beginning(1)
    print("The origin linked list is:",end = " ")
    test_ls.print_Linkedlist()
    for i in range(20):

        choice = random.randint(0,4) #增，删，查，排

        if choice == 0 or choice == 1: #执行插入操作
            subchoice = random.randint(0,2)

            if subchoice == 0: #执行头部插入
                item = random.randint(0,10)
                print("Insert",item,"at the beginning:",end=" ")
                test_ls.insert_beginning(item)
                test_ls.print_Linkedlist()

            elif subchoice == 1:#执行中部插入，after参数可取0到len

                position = random.randint(0,test_ls.ls_len())
                item = random.randint(0,10)
                ret = test_ls.insert_after(position,item)

                if ret:
                    print("Insert",item,"after the node index",position,":",end=" ")
                    test_ls.print_Linkedlist()
                else:
                    print("Insert error: The destination does not exist.")
                    print()
            else: #执行尾部插入
                item = random.randint(0,10)
                print("Insert",item,"at the end:",end=" ")
                test_ls.insert_end(item)
                test_ls.print_Linkedlist()

        elif choice == 2: #执行删除操作，下标可取0，len
            position = random.randint(0,test_ls.ls_len())
            ret = test_ls.delete_node(position)
            if ret == False:
                print("Delete error: The destination index",position,"doesn't exist.")
                print()
            else:
                print("Deleted node at position",position,"successfully:",end = " ")
                test_ls.print_Linkedlist()

        elif choice == 3: #执行查找操作
            search_item = random.randint(0,10)
            index_ls = test_ls.search_node(search_item)
            if index_ls: #列表不为空时进入
                    print("Item", search_item,"found at position:",end=" ")
                    for i in index_ls:
                        print(i,end=", ")
                    print("\b\b")
                    print()
            else:
                print("Searching failed: Item",search_item,"not found")
                print()

        else: #执行排序操作
            print("Sort this linked list in asending order:",end = " ")
            test_ls.sort_node()
            test_ls.print_Linkedlist()


main()
