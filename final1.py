class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self.head = prev

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        def get_middle(node):
            slow = node
            fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(left, right):
            dummy = Node()
            tail = dummy
            while left and right:
                if left.data < right.data:
                    tail.next, left = left, left.next
                else:
                    tail.next, right = right, right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        middle = get_middle(head)
        right_head = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(right_head)

        return merge(left, right)

    def sort(self):
        self.head = self.merge_sort(self.head)

    def merge_two_sorted_lists(self, l1, l2):
        dummy = Node()
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next


llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.print_list()
llist.sort()
llist.print_list()

# Merging two sorted lists
l1 = LinkedList()
l2 = LinkedList()
l1.insert_at_end(1)
l1.insert_at_end(3)
l1.insert_at_end(5)
l2.insert_at_end(2)
l2.insert_at_end(4)
l2.insert_at_end(6)
merged_list_head = LinkedList().merge_two_sorted_lists(l1.head, l2.head)
while merged_list_head:
    print(merged_list_head.data, end=" -> ")
    merged_list_head = merged_list_head.next
print("None")
