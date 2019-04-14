from A import A
class B(A):
    def __init__(self):
        print("init in B")
        super().__init__()
ob=B()
print(ob.a)