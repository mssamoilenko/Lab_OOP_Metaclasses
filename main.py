#task1
class InstanceCounterMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instance_count = 0

    def __call__(cls, *args, **kwargs):
        cls._instance_count += 1
        return super().__call__(*args, **kwargs)

    @property
    def instance_count(cls):
        return cls._instance_count

class MyClass(metaclass=InstanceCounterMeta):
    pass

a = MyClass()
b = MyClass()
print(MyClass.instance_count)

#task2
class InstanceLimitMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._max_instances = dct.get("_max_instances", None)
        cls._current_instances = 0

    def __call__(cls, *args, **kwargs):
        if cls._max_instances is not None and cls._current_instances >= cls._max_instances:
            raise ValueError(f"Неможливо створити більше {cls._max_instances} екземплярів класу {cls.__name__}")
        cls._current_instances += 1
        return super().__call__(*args, **kwargs)

class LimitedClass(metaclass=InstanceLimitMeta):
    _max_instances = 3

try:
    obj1 = LimitedClass()
    obj2 = LimitedClass()
    obj3 = LimitedClass()
    obj4 = LimitedClass()
except ValueError as e:
    print(e)

#task3
class ClassRegistryMeta(type):
    registry = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        if name != "Base":
            ClassRegistryMeta.registry[name] = cls

class Base(metaclass=ClassRegistryMeta):
    pass

class ClassA(Base):
    pass

class ClassB(Base):
    pass

print(ClassRegistryMeta.registry)
