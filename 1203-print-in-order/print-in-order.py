class Foo:
    def __init__(self):
        self.order = 1


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while self.order != 1:
            pass
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.order = 2

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.order != 2:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.order = 3

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.order != 3:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.order = 1