# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, x):
        if isinstance(x, self.__class__):
            return self.val == x.val and self.next == x.next
        else:
            return False

    def compare(self, x):
        cur_l, cur_r = self, x
        while cur_l is not None or cur_r is not None:
            if cur_l != cur_r:
                return False

            cur_l = cur_l.next
            cur_r = cur_r.next

        return True

    def __str__(self):
        s = '{}'.format(self.val)
        cur = self.next
        while cur is not None:
            s += '->{}'.format(cur.val)
            cur = cur.next
        else:
            s += '->None'
        return s


class Solution:
    def merge2Lists(self, x: ListNode, y: ListNode) -> ListNode:
        if x is None:
            return y
        if y is None:
            return x

        res, cur, cur_1, cur_2 = None, None, x, y
        if cur_1.val < cur_2.val:
            res = cur_1
            cur_1 = cur_1.next
        else:
            res = cur_2
            cur_2 = cur_2.next

        cur = res

        while cur_1 is not None or cur_2 is not None:
            if cur_1 is None:
                cur.next = cur_2
                break
            if cur_2 is None:
                cur.next = cur_1
                break

            if cur_1.val < cur_2.val:
                cur.next = cur_1
                cur_1 = cur_1.next
            else:
                cur.next = cur_2
                cur_2 = cur_2.next
            cur = cur.next

        return res

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        res = lists[0]
        for i in lists[1:]:
            if i is not None:
                res = self.merge2Lists(res, i)

        return res
