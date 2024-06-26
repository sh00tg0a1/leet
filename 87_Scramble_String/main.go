package main

import (
	"sort"
)

/**
We can scramble a string s to get a string t using the following algorithm:

1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
	a. Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
	b. Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
	c. Apply step 1 recursively on each of the two substrings x and y.
3. Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at ranom index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now and the result string is "rgeat" which is s2.
As there is one possible scenario that led s1 to be scrambled to s2, we return true.

Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

Example 3:

Input: s1 = "a", s2 = "a"
Output: true


Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lower-case English letters.
*/

type str []rune

func (a str) Len() int           { return len(a) }
func (a str) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a str) Less(i, j int) bool { return a[i] < a[j] }

func letters(s string) string {
	l := str(s)
	sort.Sort(l)

	return string(l)
}

func isScramble(s1 string, s2 string) bool {
	if s1 == s2 {
		return true
	}

	if letters(s1) != letters(s2) {
		return false
	}

	if len(s1) <= 3 {
		return true
	}

	for i := 1; i < len(s1); i++ {
		if isScramble(s1[0:i], s2[0:i]) && isScramble(s1[i:], s2[i:]) {
			return true
		}

		if isScramble(s1[0:i], s2[len(s1)-i:]) && isScramble(s1[i:], s2[0:len(s1)-i]) {
			return true
		}
	}

	return false
}
