class A:
    def show(self):
        print("It is A's Show")

class B(A):
    def show(self):
        print("It is B's show")


b = B()
b.show()