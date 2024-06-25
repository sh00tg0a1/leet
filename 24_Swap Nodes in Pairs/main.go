package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	newHead, cur, next := head, head, head.Next

	var last *ListNode

	for cur != nil && next != nil {
		cur.Next, next.Next = next.Next, cur

		cur, next = next, cur

		// 第一次互换
		if next == head {
			newHead = cur
		}

		if last != nil {
			last.Next = cur
		}

		last = next
		cur = next.Next

		if cur == nil {
			break
		}

		next = cur.Next
	}

	return newHead
}
