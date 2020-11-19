
class A:
    pass


class B(A):
    def b(self): pass


class C(B):
    def c(self): f()


def f(): pass
def g(): return B()


class X:
    def x(self): pass


class Y(X, B):
    def y(self): g()

