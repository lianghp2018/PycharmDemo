class Dog(object):
    def work(self):
        print('指哪打哪')


class ArmyDog(Dog):
    def work(self):
        print('追击敌人.....')


class DrugDog(Dog):
    def work(self):
        print('追查毒品....')


# 传入不同的对象,执行不同的代码,即不同的work函数
class Person(object):
    def work_with_dog(self, dog):
        dog.work()


ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
