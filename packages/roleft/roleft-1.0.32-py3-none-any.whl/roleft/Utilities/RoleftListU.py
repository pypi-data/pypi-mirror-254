import copy
from typing import Callable, TypeVar

from roleft.Entities.RoleftKeyValue import KeyValue




T = TypeVar('T')
TOut = TypeVar('TOut')


class ListU:
    @classmethod
    def Add(cls, lst: list[T], item: T):
        lst.append(item)
        
    @classmethod
    def AddRange(cls, lst: list[T], others: list[T]):
        lst += others
        return lst

    @classmethod
    def RemoveAt(cls, lst: list[T], index: int):
        del lst[index] # 【闻祖东 2023-07-26 102651】其实 self.__items.pop(index) 也可以
    
    @classmethod
    def Remove(cls, lst: list[T], item: T):
        lst.remove(item)
        
    @classmethod
    def Exists(cls, lst: list[T], predicate: Callable[[T], bool]) -> bool:
        for x in lst:
            if (predicate(x)):
                return True
            
        return False

    @classmethod
    def Count(cls, lst: list[T]):
        return len(lst)
    
    @classmethod
    def Clear(cls, lst: list[T]):
        lst = []
        
    @classmethod
    def FindAll(cls, lst: list[T], predicate: Callable[[T], bool]):
        newList: list[T] = []
        for x in lst:
            if (predicate(x)):
                newList.append(x)
            
        return newList

    @classmethod
    def First(cls, lst: list[T], predicate: Callable[[T], bool]):
        newItems = ListU.FindAll(lst, predicate)
        return newItems[0] if len(newItems) > 0 else None
        
    @classmethod
    def FirstIndex(cls, lst: list[T], predicate: Callable[[T], bool]):
        index = 0
        for x in lst:
            if (predicate(x)):
                return index
            index += 1
        
        return -1

    @classmethod
    def ToList(cls, lst: list[T]):
        return ListU.Select(lst, lambda x: x)
    
    @classmethod
    def ForEach(cls, lst: list[T], predicate: Callable[[T], None]):
        for x in lst:
            predicate(x)

    @classmethod
    def Select(cls, lst: list[T], predicate: Callable[[T], TOut]):
        newList = []
        for x in lst:
            temp = predicate(x)
            newList.append(temp)
        
        return newList

    @classmethod
    def OrderBy(cls, lst: list[T], predicate: Callable[[T], str]):
        kts = ListU.Select(lst, lambda x: KeyValue(predicate(x), x))
        keys = ListU.Select(kts, lambda x: x.key).ToList()
        keys.sort()

        newList = list()
        newItems = copy.deepcopy(lst)
        for key in keys:
            index = ListU.FirstIndex(lst, lambda x: key == predicate(x))
            newList.append(newItems[index])
            ListU.RemoveAt(lst, index)
        
        return newList

    @classmethod
    def InsertAt(cls, lst: list[T], item: T, index: int):
        lst.insert(index, item)

    @classmethod
    def RemoveAll(cls, lst: list[T], predicate: Callable[[T], bool]):
        indexes = list[int]()
        index = 0
        for item in lst:
            if (predicate(item)):
                indexes.append(index)
            index += 1
        
        indexes.reverse()
        for idx in indexes:
            ListU.RemoveAt(lst, idx)


