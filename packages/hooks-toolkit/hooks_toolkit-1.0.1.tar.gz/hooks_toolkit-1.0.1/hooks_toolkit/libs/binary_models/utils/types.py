from typing import Union, TypedDict, List

# Type Aliases
Bool = bool
UInt8 = int
UInt16 = int
UInt32 = int
UInt64 = int
UInt224 = int
Hash256 = str
PublicKey = str
VarString = str
XFL = float
Currency = str
XRPAddress = str


# Forward declaration for recursive type
class Model(TypedDict, total=False):
    pass


# VarModelArray type
VarModelArray = List[Model]

# Completing the Model definition with possible types
Model.update(
    {
        str: Union[
            Bool,
            UInt8,
            UInt16,
            UInt32,
            UInt64,
            UInt224,
            Hash256,
            PublicKey,
            VarString,
            XFL,
            Currency,
            XRPAddress,
            Model,
            VarModelArray,
        ]
    }
)
