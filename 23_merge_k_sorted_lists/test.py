from s import Solution, ListNode


class TestCase(object):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        pass

    def test1(self):
        ln = ListNode(1)
        assert(self.s.mergeKLists([ln]) == ln)

    def gen_list(self, x):
        head = ListNode(x[0])
        cur = head

        for v in x[1:]:
            ln = ListNode(v)
            cur.next = ln
            cur = ln
        cur.next = None

        return head

    def test_list(self):
        li = [1, 2, 3, 4]
        ln = self.gen_list(li)
        print(ln)

        li2 = [1, 2, 3, 3]
        ln2 = self.gen_list(li2)
        print(ln2)
        assert(ln2.compare(ln) == False)

    def test_list2(self):
        li = [1, 2, 3, 4]
        ln = self.gen_list(li)
        print(ln)

        li2 = [1, 2, 3, 4]
        ln2 = self.gen_list(li2)
        print(ln2)
        assert(ln.compare(ln2) == True)

    def test_merge2(self):
        li = [1, 2, 3, 4]
        ln = self.gen_list(li)
        print(ln)

        li2 = [3, 45, 56]
        ln2 = self.gen_list(li2)
        # print(self.s.merge2List(ln, ln2))

        nl = self.gen_list([1, 2, 3, 3, 4, 45, 56])

        assert(self.s.merge2Lists(ln, ln2).compare(nl))

    def test_merge3(self):

        l1 = self.gen_list([2, 3, 4, 5])
        l2 = self.gen_list([1, 2, 3])
        l3 = self.gen_list([4, 5, 6])

        nl = self.gen_list([1, 2, 2, 3, 3, 4, 4, 5, 5, 6])

        assert(self.s.mergeKLists([l1, l2, l3]).compare(nl))

    def test_edge(self):
        assert(self.s.mergeKLists([]) == None)
        assert(self.s.mergeKLists([]) == None)