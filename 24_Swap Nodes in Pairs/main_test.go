package main

import (
	"testing"

	"github.com/magiconair/properties/assert"
)

func makeList(l []int) *ListNode {
	var head *ListNode
	for i := len(l) - 1; i >= 0; i-- {
		node := ListNode{
			Val:  l[i],
			Next: nil,
		}

		node.Next = head
		head = &node
	}
	return head
}

func Test1(t *testing.T) {
	tc := []int{1, 2, 3, 4}
	n1 := makeList(tc)
	nh := swapPairs(n1)

	var lv []int
	cur := nh
	for cur != nil {
		lv = append(lv, cur.Val)
		cur = cur.Next
	}

	assert.Equal(t, lv, []int{2, 1, 4, 3})
}

func Test2(t *testing.T) {
	tc := []int{}
	n1 := makeList(tc)
	nh := swapPairs(n1)

	var lv []int
	cur := nh
	for cur != nil {
		lv = append(lv, cur.Val)
		cur = cur.Next
	}

	assert.Equal(t, lv, tc)
}

func Test3(t *testing.T) {
	tc := []int{1, 2, 3}
	n1 := makeList(tc)
	nh := swapPairs(n1)

	var lv []int
	cur := nh
	for cur != nil {
		lv = append(lv, cur.Val)
		cur = cur.Next
	}

	assert.Equal(t, lv, []int{2, 1, 3})
}
