class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
    
    if list1.val < list2.val:
        temp = head = list1
        list1 = list1.next
    else:
        temp = head = list2
        list2 = list2.next
    
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
             temp.next = list1
             temp = list1
             list1 = list1.next
        else:
            temp.next =list2
            temp = list2
            list2 = list2.next
    
    if list1 is not None:
        temp.next = list1
    elif list2 is not None:
        temp.next = list2
    display(head)


def insert(node, n):
    for i in range(n):
        temp_node = ListNode()
        temp_val = int(input())
        temp_node.val = temp_val
        temp_node.next = None
        if i==0:
            node.val = temp_val
            node.next = None
        else:
            node.next = temp_node
            node =temp_node

def display(node):
    temp_node = node
    while temp_node:
        print(temp_node.val)
        temp_node= temp_node.next


node1 = ListNode()
node2 = ListNode()
temp_node1, temp_node2 = node1, node2
n1 = int(input("No of 1st linked list values : "))
print("Enter the sorted array : ")
insert(temp_node1, n1)
n2 = int(input("No of 2nd linked list values : "))
print("Enter the sorted array : ")
insert(temp_node2, n2)
mergeTwoLists(node1, node2)
