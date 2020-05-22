# ===> Inheritance ( this is a concept of OOP )
# ===> Passing of the characteristics from one class to another (Parent and child relationship)

# There are 3 types of inheritance:
# ---> Single Level inheritance
# ---> Multi Level inheritance
# ---> Multiple inheritance

print('_______________________________________________________________________________________________________________________')
# _______________________________________________________________________________________________________________________

# Single Level inheritance
class A:
    @staticmethod
    def walking():
        print('Walking...')


class B(A):
    @staticmethod  # we are making this static because we are not using any instance or class variables in the method, if you remove that @staticmethod also it will work, but its best to not use static else no use of using objects to access it
    def running():
        print('Running...')


# main program
obj = B()
obj.running()
obj.walking()  # we are also able to access walking() from class B


# We also can override the methods of parent class from the child class, and this overriding effect applies to that particular child class
class C:
    def jumping(self):
        print('Jumping in C...')


class D(C):
    def rolling(self):
        print('Rolling in D...')

    def jumping(self):  # this have overridden the jumping method in class C
        print('Jumping in D...')


# main program
obj1 = D()
obj1.jumping()
obj1.rolling()


print('_______________________________________________________________________________________________________________________')
# _______________________________________________________________________________________________________________________

# Multi-Level inheritance

class X:
    def grandParent(self):
        print('GrandParent class X.....')


class Y(X):
    def parent(self):
        print('Parent class Y.....')


class Z(Y):
    def child(self):
        print('Child class Z.....')


# main program

# the child class Z extends only class Y, but also has access to class X because class Y extends class X
obj2 = Z()
obj2.grandParent()
obj2.parent()
obj2.child()


print('_______________________________________________________________________________________________________________________')
# _______________________________________________________________________________________________________________________

# multiple inheritance
class M:
    def mClass(self):
        print('This is the mClass....')


class N:
    def nClass(self):
        print('This is the nClass....')


class O(M, N): # this class O undergoes multiple inheritance
    def oClass(self):
        print('This is the oClass....')

# main program
obj3 = O()
obj3.mClass()
obj3.nClass()
obj3.oClass()
# but keep in mind that class N and M can't access each others features because they are not inherited

print('_______________________________________________________________________________________________________________________')
