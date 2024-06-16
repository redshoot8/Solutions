from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def to_str_num(linked_list: ListNode) -> str:
        if linked_list.next:
            return Solution.to_str_num(linked_list.next) + str(linked_list.val)
        return str(linked_list.val)

    @staticmethod
    def from_str_num(num: str):
        if len(num) > 1:
            return ListNode(int(num[-1]), Solution.from_str_num(num[:-1]))
        return ListNode(int(num))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return Solution.from_str_num(str(int(Solution.to_str_num(l1)) + int(Solution.to_str_num(l2))))
