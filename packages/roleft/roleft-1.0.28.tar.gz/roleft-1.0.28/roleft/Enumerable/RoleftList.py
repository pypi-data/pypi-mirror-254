import random
from typing import Dict, List, Generic, MutableSequence, TypeVar, Callable, Union
import copy
import json

from roleft.Entities.RoleftKeyValue import KeyValue


T = TypeVar("T")
TOut = TypeVar("TOut")


# class xList(MutableSequence[T], Generic[T]):
class xList(Generic[T]):
    # def __init__(self, list: List[T] = []) -> None:
    #     self.__items: List[T] = list

    # 来自 chatgpt: 这是因为在 Python 中，函数默认参数的默认值在函数定义时被计算，
    # 而不是每次函数调用时重新计算。对于可变对象（如列表、字典等），
    # 如果将其作为默认参数，它只会在函数定义时被创建一次，并且之后所有调用该函数的实例都会共享同一个默认对象。
    def __init__(self, list: List[T] = []) -> None:
        self.__items: List[T] = list if len(list) > 0 else []

    def Add(self, item: T):
        self.__items.append(item)
        return self

    def Exists(self, predicate: Callable[[T], bool]) -> bool:
        for x in self.__items:
            if predicate(x):
                return True

        return False

    def AddRange(self, others: list[T]):
        self.__items += others
        return self

    def RemoveAt(self, index: int):
        del self.__items[index]  # 【闻祖东 2023-07-26 102651】其实 self.__items.pop(index) 也可以
        return self

    def Remove(self, item: T):
        self.__items.remove(item)
        return self

    @property
    def Count(self):
        return len(self.__items)

    def Clear(self):
        self.__items = []
        return self

    def FindAll(self, predicate: Callable[[T], bool]):
        lst = []
        for x in self.__items:
            if predicate(x):
                lst.append(x)

        return xList[T](lst)

    def First(self, predicate: Callable[[T], bool]):
        newItems = self.FindAll(predicate).ToList()
        return newItems[0] if len(newItems) > 0 else None
    
    def Find(self, predicate: Callable[[T], bool]):
        return self.First(predicate)

    def FirstIndex(self, predicate: Callable[[T], bool]):
        index = 0
        for x in self.__items:
            if predicate(x):
                return index
            index += 1

        return -1

    def ToList(self):
        return self.__items

    def InsertAt(self, item: T, index: int):
        self.__items.insert(index, item)
        return self

    def RemoveAll(self, predicate: Callable[[T], bool]):
        indexes = list[int]()
        index = 0
        for item in self.__items:
            if predicate(item):
                indexes.append(index)
            index += 1

        indexes.reverse()
        for idx in indexes:
            self.RemoveAt(idx)

        return self

    def Shuffle(self):
        random.shuffle(self.__items)
        return self

    def Print(self):
        print(self.__items)

    def Select(self, predicate: Callable[[T], TOut]):
        lst = []
        for x in self.__items:
            temp = predicate(x)
            lst.append(temp)

        return xList[TOut](lst)

    def OrderByAsc(self, predicate: Callable[[T], str]):
        xstKts = self.Select(lambda x: KeyValue(predicate(x), x))
        lstKeys = xstKts.Select(lambda x: x.key).ToList()
        lstKeys.sort()

        lstFin = []
        # copy.deepcopy
        xstTemp = xList[T](copy.copy(self.__items))
        for key in lstKeys:
            item = xstTemp.First(lambda x: key == predicate(x))
            lstFin.append(item)
            xstTemp.Remove(item)

        return xList[T](lstFin)
    
    def OrderByDesc(self, predicate: Callable[[T], str]):
        xstAsc = self.OrderByAsc(predicate)
        return xstAsc.Reverse()
    
    def Reverse(self):
        lst = copy.copy(self.__items)
        lst.reverse()
        return xList[T](lst)

    def DistinctBy(self, predicate: Callable[[T], TOut]):
        lst = []
        keys = set()
        for item in self.__items:
            key = predicate(item)
            if key not in keys:
                keys.add(key)
                lst.append(item)

        return xList[T](lst)

    # 【闻祖东 2024-01-19 183900】python应该是不支持这种ForEach，暂时算了吧
    def ForEach(self, predicate: Callable[[T], None]):
        for x in self.__items:
            predicate(x)
    
    def Contains(self, item: T):
        for x in self.__items:
            if x == item:
                return True
        
        return False

    def Take(self, count: int):
        lst = self.__items[:count]
        return xList[T](lst)
    
    def Skip(self, count: int):
        lst = copy.copy(self.__items)
        cnt = min(lst.__len__(), count)
        for i in range(0, cnt):
            lst.pop(0)
        
        return xList[T](lst)


class Student:
    def __init__(self, id=0, name="", age=0) -> None:
        self.Id = id
        self.Name = name
        self.Age = age
        pass







stus = xList[Student]()
stus.Add(Student(1, "jack", 54))
stus.Add(Student(2, "pony", 47))
stus.Add(Student(3, "雷军", 35))
stus.Add(Student(4, "冯仑", 67))
stus.Add(Student(5, "王大爷", 67))

def AddAge(item: Student):
    item.Age = item.Age + 1
    
stus.ForEach(AddAge)



# new = stus.OrderByAsc(lambda x: x.Age)
# other = stus.OrderByDesc(lambda x: x.Age)

# disct = stus.DistinctBy(lambda x: x.Age)
pass