import hashlib
from enum import Enum, unique
from typing_extensions import TypedDict
from typing import NewType

InputCate = Enum("InputCate222", ("String", "File"))
AlgorithmCate = Enum("AlgorithmCate", ("Md5", "Sha1", "Sha256"))

_algoDic = {
    AlgorithmCate.Md5: hashlib.md5,
    AlgorithmCate.Sha1: hashlib.sha1,
    AlgorithmCate.Sha256: hashlib.sha256,
}


def _loadContent(cate: InputCate, input: str) -> bytes:
    if cate == InputCate.File:
        with open(input, "rb") as file:
            return file.read()
    elif cate == InputCate.String:
        return input.encode()
    else:
        raise f"未定义的输入类型 - {cate}"

class AU:
    @classmethod
    def Calc(cls, algoCate: AlgorithmCate, inputCate: InputCate, input: str) -> str:
        func = _algoDic[algoCate]
        return func(_loadContent(inputCate, input)).hexdigest()

    @classmethod
    def Sha1Str(cls, input: str) -> str:
        return AU.Calc(AlgorithmCate.Sha1, InputCate.String, input)

    @classmethod
    def Sha1File(cls, path: str) -> str:
        return AU.Calc(AlgorithmCate.Sha1, InputCate.File, path)

    @classmethod
    def Sha256Str(cls, input: str) -> str:
        return AU.Calc(AlgorithmCate.Sha256, InputCate.String, input)

    @classmethod
    def Sha256File(cls, path: str) -> str:
        return AU.Calc(AlgorithmCate.Sha256, InputCate.File, path)

    @classmethod
    def Md5Str(cls, input: str) -> str:
        return AU.Calc(AlgorithmCate.Md5, InputCate.String, input)

    @classmethod
    def Md5File(cls, path: str) -> str:
        return AU.Calc(AlgorithmCate.Md5, InputCate.File, path)
