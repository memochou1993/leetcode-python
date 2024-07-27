from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_list_node(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for ele in lst:
        current.next = ListNode(ele)
        current = current.next
    return dummy.next

def list_node_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
