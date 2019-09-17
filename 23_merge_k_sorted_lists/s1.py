# Definition for singly-linked list.
from typing import List


class Solution:
    def merge2Lists(self, x: List, y: List) -> List:
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
            res = self.merge2Lists(res, i)

        return res
