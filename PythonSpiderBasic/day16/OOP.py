# # 创建一个类，有3个函数功能
# class stuOOP:
#     # 创建对象时，给对象传递一些信息
#     def __init__(self, name, age, height, weight):
#         # print("self", self)
#         # print(name, age, height, weight)
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#
#     def func1(self):
#         print(self.name, "has", self.age)
#
#     def func2(self):
#         pass
#
#     def func3(self, cishu):
#         for i in range(cishu):
#             self.func1()
#             self.func2()
#
#
# if __name__ == '__main__':
#     # 创建一个oop1对象
#     oop1 = stuOOP("Alex", 18, 170, 70)
#
#     oop1.func1()
#     oop1.func2()
#     oop1.func3(3)
#     # oop1.func4()
#     # 类决定了对象的功能
#
#     # 创建一个oop2对象
#     oop2 = stuOOP("Bob",20, 155, 60)
#
#     # print(id(oop1),id(oop2))
#     # oop1和oop2共享一个类的空间，有相同的功能，但有各自独立的内存空间
#
#     oop2.func1()

# 继承:子类会自动拥有父类中的所有内容，私有内容除外
class Animal:
    def dong(self):
        print("是动物")
    def run(self):
        self.dong()
    def __siyou(self):
        print("私有内容")

class Dog(Animal):
    def jiao(self):
        print("汪汪")
    def dong(self):
        print("是狗")

class Cat(Animal):
    def jiao(self):
        print("喵喵")
    def dong(self):
        print("是猫")
    # 就近原则(MRO)：自己有就执行自己的，没有再去父类找

if __name__ == '__main__':
    d = Dog()
    d.dong()
    d.jiao()
    c = Cat()
    c.dong()
    c.jiao()

    d.run()
    # 对象一直是d

    # d.__siyou()