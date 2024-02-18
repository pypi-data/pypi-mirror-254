from typing import Generic, TypeVar
from roleft.Entities.RoleftKeyValue import KeyValue
# from roleft.Entities import KeyValue
from roleft.Enumerable.RoleftList import xList
# from roleft.Enumerable import xList


TKey = TypeVar('TKey')
TValue = TypeVar('TValue')

class xDict(Generic[TKey, TValue]):
    def __init__(self) -> None:
        self.__kvs: xList[KeyValue[TKey, TValue]] = xList()

    def SureAdd(self, key: TKey, value: TValue):
        curr = self.__kvs.First(lambda x: x.key == key)
        if curr != None:
            self.__kvs.Remove(curr)
        
        self.__kvs.Add(KeyValue(key, value))
        return self
    
    def ContainsKey(self, key: TKey) -> bool:
        return self.GetValue(key) != None
    
    def Keys(self):
        return self.__kvs.Select(lambda x: x.key)
    
    def Values(self):
        return self.__kvs.Select(lambda x: x.value)
    
    def Clear(self):
        self.__kvs.Clear()
        return self
    
    def GetValue(self, key: TKey):
        first = self.__kvs.First(lambda x: x.key == key)
        if first != None:
            return first.value
        else:
            return None
    
    def Remove(self, key: TKey):
        curr = self.GetValue(key)
        if (curr != None):
            self.__kvs.Remove(curr)
            
        return self
    
    def Print(self):
        dic = {}
        for kv in self.__kvs.ToList():
            dic[kv.key] = kv.value
        
        print(dic)