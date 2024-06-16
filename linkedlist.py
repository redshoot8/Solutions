class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

    def to_str_num(self) -> str:
        if self.next_node:
            return self.next_node.to_str_num() + str(self.value)
        return str(self.value)

    @staticmethod
    def from_str_num(num: str):
        if len(num) > 1:
            return ListNode(int(num[-1]), ListNode.from_str_num(num[:-1]))
        return ListNode(int(num))


if __name__ == '__main__':
    ll = ListNode(2, ListNode(4, ListNode(3)))
    print(ll.to_str_num())
