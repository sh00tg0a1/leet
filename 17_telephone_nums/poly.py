class A(object):
    def aa(self, x, y):
        return x + y


class B(object):
    def aa(self, x, y):
        return x * y


def do_sth(a, x, y):
    return a.aa(x, y)


if __name__ == "__main__":
    a = A()
    b = B()

    print(do_sth(a, 2, 3))
    print(do_sth(b, 2, 3))


class Test(object):
    