class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def findMergeNode(headA: SinglyLinkedListNode, headB: SinglyLinkedListNode) -> int:
    current_node_A = headA
    current_node_B = headB
    search_position_A = headA
    search_position_B = headB

    while current_node_A.next is not None and current_node_B.next is not None:
        current_node_A = current_node_A.next
        current_node_B = current_node_B.next

    while current_node_A.next is not None:
        current_node_A = current_node_A.next
        search_position_A = search_position_A.next

    while current_node_B.next is not None:
        current_node_B = current_node_B.next
        search_position_B = search_position_B.next

    merge_node = None

    while search_position_A is not None and search_position_B is not None:
        if search_position_A.data == search_position_B.data and merge_node is None:
            merge_node = search_position_A
        elif search_position_A.data != search_position_B.data:
            merge_node = None

        search_position_A = search_position_A.next
        search_position_B = search_position_B.next

    return -1 if merge_node is None else merge_node.data
